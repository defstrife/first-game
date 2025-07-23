import sqlite3
from typing import List, Optional, Tuple

class DatabaseManager:
    def __init__(self, db_name: str = ":memory"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._initialize_database()

    def _initialize_database(self):
        self.cursor.executescript("""CREATE TABLE IF NOT EXISTS levels (
            id INTEGER PRIMARY KEY,
            finishzoneX INTEGER,
            finishzoneY INTEGER,
            playerstartX INTEGER,
            playerstartY INTEGER
        );

        CREATE TABLE IF NOT EXISTS spikes (
	        id INTEGER PRIMARY KEY AUTOINCREMENT,
	        level_id INTEGER,
	        x INTEGER,
            y INTEGER,
            FOREIGN KEY (level_id) references levels(id)
        );

        CREATE TABLE IF NOT EXISTS coins (
	        id INTEGER PRIMARY KEY AUTOINCREMENT,
	        level_id INTEGER,
	        x INTEGER,
            y INTEGER,
            FOREIGN KEY (level_id) references levels(id)
        );
                                  
        CREATE TABLE IF NOT EXISTS barrels (
	        id INTEGER PRIMARY KEY AUTOINCREMENT,
	        level_id INTEGER,
	        x INTEGER,
            y INTEGER,
            content TEXT,
            FOREIGN KEY (level_id) references levels(id)
        );
                                  
        CREATE TABLE IF NOT EXISTS enemies (
	        id INTEGER PRIMARY KEY AUTOINCREMENT,
	        level_id INTEGER,
	        x INTEGER,
            y INTEGER,
            FOREIGN KEY (level_id) references levels(id)
        );
                                  
        CREATE TABLE IF NOT EXISTS sublevels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            level_id INTEGER,
            direction TEXT,
            target_level_id INTEGER,
            FOREIGN KEY (level_id) references levels(id)
        )
        """)
        self.connection.commit()

    def add_level(self, finishzoneX: int, finishzoneY: int, playerstartX: int, playerstartY: int) -> int:
        self.cursor.execute("INSERT INTO levels (finishzoneX, finishzoneY, playerstartX, playerstartY) VALUES (?, ?, ?, ?)", (finishzoneX, finishzoneY, playerstartX, playerstartY))
        self.connection.commit()
    
    def add_spike(self, level_id: int, x: int, y: int) -> int:
        self.cursor.execute("INSERT INTO spikes (level_id, x, y) VALUES (?, ?, ?)", (level_id, x, y))
        self.connection.commit()
    
    def add_coin(self, level_id: int, x: int, y: int) -> int:
        self.cursor.execute("INSERT INTO coins (level_id, x, y) VALUES (?, ?, ?)", (level_id, x, y))
        self.connection.commit()
    
    def add_barrel(self, level_id: int, x: int, y: int, content: str='') -> int:
        self.cursor.execute("INSERT INTO barrels (level_id, x, y, content) VALUES (?, ?, ?, ?)", (level_id, x, y, content))
        self.connection.commit()

    def add_enemy(self, level_id: int, x: int, y: int) -> int:
        self.cursor.execute("INSERT INTO enemies (level_id, x, y) VALUES (?, ?, ?)", (level_id, x, y))
        self.connection.commit()

    def add_sublevel(self, level_id: int, direction: str, target_level_id: int) -> int:
        self.cursor.execute("INSERT INTO sublevels (level_id, direction, target_level_id) VALUES (?, ?, ?)", (level_id, direction, target_level_id))
        self.connection.commit()

    def get_level(self, id: int):
        self.cursor.execute("SELECT * FROM levels where id = ?", (id,))
        level = self.cursor.fetchone()
        return
    
    def get_spikes(self, level_id: int):
        self.cursor.execute("SELECT x, y FROM spikes where level_id = ?", (level_id,))
        spikes = self.cursor.fetchall()
        return spikes
    
    def get_coins(self, level_id: int):
        self.cursor.execute("SELECT x, y FROM coins where level_id = ?", (level_id,))
        coins = self.cursor.fetchall()
        return coins
    
    def get_barrels(self, level_id: int, content: str=''):
        self.cursor.execute("SELECT x, y, content FROM barrels where level_id = ?", (level_id,))
        barrels = self.cursor.fetchall()
        return barrels
    
    def get_enemies(self, level_id: int):
        self.cursor.execute("SELECT x, y FROM enemies where level_id = ?", (level_id,))
        enemies = self.cursor.fetchall()
        return enemies

    def close(self):
        self.connection.close()