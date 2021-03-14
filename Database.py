import sqlite3
conn = sqlite3.connect('Recipes.db', timeout=10)
c = conn.cursor()

