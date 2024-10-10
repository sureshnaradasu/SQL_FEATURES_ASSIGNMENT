import sqlite3

conn = sqlite3.connect('Items_Check_Constraint.db')
cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY, 
        item_name TEXT NOT NULL, 
        cost REAL NOT NULL CHECK (cost > 0)
    );
''')

cursor.execute(''' 
    INSERT INTO items (item_id, item_name, cost) 
    VALUES (1, 'Bluetooth Speaker', 49.99); 
''')
cursor.execute(''' 
    INSERT INTO items (item_id, item_name, cost) 
    VALUES (2, 'Fitness Tracker', 199.99); 
''')

cursor.execute('''SELECT * FROM items''')
print("\nItems Table\n")
print(cursor.fetchall())  

cursor.execute(''' 
    INSERT INTO items (item_id, item_name, cost) 
    VALUES (3, 'eBook Reader', 0);
''')

conn.commit()
conn.close()
