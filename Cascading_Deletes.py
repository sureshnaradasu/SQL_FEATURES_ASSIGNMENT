import sqlite3

conn = sqlite3.connect('Items_Cascading_Deletes.db')
cursor = conn.cursor()

cursor.execute('PRAGMA foreign_keys = ON;')

cursor.execute('''
CREATE TABLE types (
    type_id INTEGER PRIMARY KEY,
    type_name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE items (
    item_id INTEGER PRIMARY KEY,
    item_name TEXT NOT NULL,
    type_id INTEGER,
    FOREIGN KEY (type_id) REFERENCES types(type_id) ON DELETE CASCADE
)
''')

types = [
    (1, 'Electronics'), 
    (2, 'Clothing'),        
    (3, 'Books')    
]
cursor.executemany('INSERT INTO types (type_id, type_name) VALUES (?, ?)', types)

items = [
    (1, 'Television', 1),    
    (2, 'Refrigerator', 1),
    (3, 'T-Shirt', 2),       
    (4, 'Mystery Novel', 3)
]
cursor.executemany('INSERT INTO items (item_id, item_name, type_id) VALUES (?, ?, ?)', items)

print("Initial data in types table:")
cursor.execute('SELECT * FROM types')
print(cursor.fetchall())

print("\nInitial data in items table:")
cursor.execute('SELECT * FROM items')
print(cursor.fetchall())

cursor.execute('DELETE FROM types WHERE type_id = 1')

print("\nData in types table after deleting type_id = 1 (Electronics):")
cursor.execute('SELECT * FROM types')
print(cursor.fetchall())

print("\nData in items table after deleting type_id = 1 (Electronics):")
cursor.execute('SELECT * FROM items')
print(cursor.fetchall())

conn.commit()
conn.close()
