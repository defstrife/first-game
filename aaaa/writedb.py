import sqlite3
import databasemanager

db_manager = databasemanager.DatabaseManager("game_database.db")

#"spikes": [(500, 500), (200, 500), (325, 200)]
db_manager.add_level(325, 250, 100, 100)
db_manager.add_spike(1, 500, 500)
db_manager.add_spike(1, 200, 500)
db_manager.add_spike(1, 325, 200)
db_manager.add_coin(1, 100, 250)
db_manager.add_coin(1, 600, 105)
db_manager.add_coin(1, 625, 450)
db_manager.add_barrel(1, 300, 400)
db_manager.add_barrel(1, 400, 400, 'heart')
db_manager.add_enemy(1, 300, 300)

print(db_manager.get_spikes(1))
print(db_manager.get_coins(1))
print(db_manager.get_barrels(1))
print(db_manager.get_barrels(1))
