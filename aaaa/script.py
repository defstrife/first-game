import pygame
import spike as Spike
import coin as Coin
import finishzone as Finishzone
import player as Player
import enemy as Enemy
import bomb as Bomb
import barrel as Barrel
import wall as Wall
import heart as Heart
import levels as Levels

pygame.init()

WIDTH, HEIGHT = 800, 600
speed = 5
FPS = 60
score = 0
hearts = 2


start_position = []
spikes = []
coins = []
finishzone = Finishzone.Finishzone(0, 0)
player = Player.Player(0, 0, 50, 50)
barrels = []
enemies = []
walls = []
bombs = []
loot_list = []
not_picked_up_loot = []
current_level = 1
sublevels = []
start_position_x = 0
start_position_y = 0


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
running = True
background = pygame.image.load("images/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

clock = pygame.time.Clock()
bombs = []
font = pygame.font.Font(None, 36)
enemies = [Enemy.Enemy(300, 300)]

def load_level(level_number):
    level = Levels.levels.get(level_number)

    if not level:
        raise ValueError(f"Level {level_number} does not exist.")

    sublevels.clear()
    walls.clear()
    spikes.clear()
    coins.clear()
    barrels.clear()
    enemies.clear()
    start_position.clear()

    for i in range(0, int(WIDTH/50)):
        walls.append(Wall.Wall(i*100, 0))
        walls.append(Wall.Wall(i * 100, 600))

    for i in range(0, int(HEIGHT/50)):
        walls.append(Wall.Wall(0, i*100))
        walls.append(Wall.Wall(800, i*100))

    for spike_pos in level["spikes"]:
        spikes.append(Spike.Spike(*spike_pos))
    for coin_pos in level["coins"]:
        coins.append(Coin.Coin(*coin_pos))
    for enemy_pos in level["enemies"]:
        enemies.append(Enemy.Enemy(*enemy_pos))
    for barrel_info in level["barrels"]:
        if len(barrel_info) == 2:
            barrels.append(Barrel.Barrel(*barrel_info))
        else:
            barrels.append(Barrel.Barrel(*barrel_info[:2], loot_type = barrel_info[2]))

    if level["sublevels"]:
        if "up" in level["sublevels"]:
            walls[:] = [wall for wall in walls if not (wall.rect.x >= 350 and wall.rect.x <= 450  and wall.rect.y <= 0)]
            sublevels.append(("up", level["sublevels"]["up"]))
        if "down" in level["sublevels"]:
            walls[:] = [wall for wall in walls if not (wall.rect.x >= 350 and wall.rect.x <= 450  and wall.rect.y >= 550)]
            sublevels.append(("down", level["sublevels"]["down"]))

    if level["finishzoneX"]:
        finishzone.rect.x, finishzone.rect.y = level["finishzoneX"], level["finishzoneY"]

    start_position.append(level["playerstartX"])
    start_position.append(level["playerstartY"])
    player.rect.x, player.rect.y = level["playerstartX"], level["playerstartY"]
    print(start_position_x, start_position_y)

    for pos in start_position:
        print(f"{pos}")

def damage(hearts):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Не молодец", True, (0, 0, 0))
    screen.blit(score_text, (200, 300))
    hearts -= 1
    player.rect.x = start_position[0]
    player.rect.y = start_position[1]
    if hearts <= 0:
        return hearts, False
    return hearts, True

load_level(current_level)

while running:
    screen.blit(background, (0, 0))
    old_x, old_y = player.rect.x, player.rect.y


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and player.rect.x < WIDTH - player.width:
                player.speedx = speed
            if event.key == pygame.K_a and player.rect.x > 0:
                player.speedx = -speed
            if event.key == pygame.K_w and player.rect.y > 0:
                player.speedy = -speed
            if event.key == pygame.K_s and player.rect.y < HEIGHT -player.height:
                player.speedy = speed
            if event.key == pygame.K_SPACE:
                player.place_bomb(bombs)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_a:
                player.speedx = 0
            if event.key == pygame.K_s or event.key == pygame.K_w:
                player.speedy = 0
        if player.rect.x > WIDTH - player.width or player.rect.x < 0 or player.rect.y > HEIGHT - player.height or player.rect.y < 0:
            player.rect.x = 0
            player.rect.y = 0



    player.move()

    for direction, level_number in sublevels:
        if direction == "up" and player.rect.y <= 0:
            current_level = level_number
            load_level(current_level)
        elif direction == "down" and player.rect.y >= HEIGHT - player.rect.height:
            current_level = level_number
            load_level(current_level)
        elif direction == "left" and player.rect.y <= 0:
            current_level = level_number
            load_level(current_level)
        elif direction == "right" and player.rect.y >= WIDTH - player.rect.height:
            current_level = level_number
            load_level(current_level)

    for spike in spikes:
        screen.blit(spike.image, (spike.rect.x, spike.rect.y))
        if player.rect.colliderect(spike.rect):
            hearts, running = damage(hearts)

    for coin in coins:
        screen.blit(coin.image, (coin.rect.x, coin.rect.y))
        if player.rect.colliderect(coin.rect):
            coins.remove(coin)
            score += 1

    for barrel in barrels:
        screen.blit(barrel.image, barrel.rect)
        if player.rect.colliderect(barrel.rect):
            player.rect.x, player.rect.y = old_x, old_y

    for bomb in bombs:
        screen.blit(bomb.image, (bomb.rect.x, bomb.rect.y))
        if bomb.update():
            explosion_area = bomb.get_explosion_area()

            if player.rect.colliderect(explosion_area):
                hearts, running = damage(hearts)
                player.rect.x = 0
                player.rect.y = 0
            for enemy in enemies[:]:
                if enemy.rect.colliderect(explosion_area):
                    enemies.remove(enemy)
            for barrel in barrels[:]:
                if barrel.rect.colliderect(explosion_area):
                    loot = barrel.open()
                    if loot:
                        loot_list.append(loot)
                    barrels.remove(barrel)
            bombs.remove(bomb)
        if not bomb.exploded or bomb.explosion_duration > 0:
            if bomb.exploded:
                bomb.draw_explosion(screen)
            else:
                screen.blit(bomb.image, bomb.rect)

        if bomb.exploded and bomb.explosion_duration <= 0:
            bombs = []

    for loot_item in loot_list[:]:
        screen.blit(loot_item.image, loot_item.rect)
        if player.rect.colliderect(loot_item.rect):
            if isinstance(loot_item, Heart.Heart):
                hearts += 1
            elif isinstance(loot_item, Coin.Coin):
                score += 1
            loot_list.remove(loot_item)



    for enemy in enemies:
        screen.blit(enemy.image, (enemy.rect.x, enemy.rect.y))
        enemy.move()
        if player.rect.colliderect(enemy.rect):
            hearts, running = damage(hearts)


    for wall in walls:
        screen.blit(wall.image, (wall.rect.x, wall.rect.y))
        if player.rect.colliderect(wall.rect):
            player.rect.x, player.rect.y = old_x, old_y

    if player.rect.colliderect(finishzone.rect) and finishzone.the_end(enemies, coins):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Молодец", True, (0, 0, 0))
        screen.blit(score_text, (200, 300))
        current_level += 1
        try:
            load_level(current_level)
            score = 0
        except ValueError as e:
            print (e)
            running = False


    if finishzone.the_end(enemies, coins):
        screen.blit(finishzone.image, (finishzone.rect.x, finishzone.rect.y))


    screen.blit(player.image, (player.rect.x, player.rect.y))

    score_text = font.render(f"Score: {score}", True, (0,200,0))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 100, 50))
    screen.blit(score_text, (0, 0))
    hearts_text = font.render(f"Hearts: {hearts}", True, (200, 0, 0))
    pygame.draw.rect(screen, (0, 0, 0), (680, 0, 110, 50))
    screen.blit(hearts_text, (680, 0))
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()