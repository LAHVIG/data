import sqlite3

conn = sqlite3.connect('guessing_game.db')
c = conn.cursor()

c.execute('''CREATE TABLE game_data
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             start_time TEXT,
             end_time TEXT,
             points INTEGER)''')

conn.commit()
conn.close()
