import sqlite3
import databasemanager
import levels

db_manager = databasemanager.DatabaseManager("game_database.db")

def add_level_data(level_id, level_data):

    finishX = level_data.get("finishzoneX", 0)
    finishY = level_data.get("finishzoneY", 0)

    db_manager.add_level(
        finishzoneX= finishX,
        finishzoneY= finishY,
        playerstartX= level_data["playerstartX"],
        playerstartY= level_data["playerstartY"]
    )

    for spike in level_data["spikes"]:
        db_manager.add_spike(level_id, spike[0], spike[1])
    for coin in level_data["coins"]:
        db_manager.add_coin(level_id, coin[0], coin[1])
    for enemy in level_data["enemies"]:
        db_manager.add_enemy(level_id, enemy[0], coin[1])
    for barrel in level_data["barrels"]:
        if len(barrel) == 3:
            db_manager.add_barrel(level_id, barrel[0], barrel[1], barrel[2])
        else:
            db_manager.add_barrel(level_id, barrel[0], barrel[1])

    for direction, target_level_id in level_data["sublevels"].items():
        db_manager.add_sublevel(level_id, direction, target_level_id)


for level_id, level_data in levels.levels.items():
    add_level_data(level_id, level_data)



db_manager.close()
