import sqlite3

conn = sqlite3.connect('Clients_Violating_Foreign_Key_Constraint.db')
cursor = conn.cursor()

cursor.execute('PRAGMA foreign_keys = ON;')

cursor.execute('''CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY, 
    client_name TEXT NOT NULL
);''')

cursor.execute('''CREATE TABLE purchases (
    purchase_id INTEGER PRIMARY KEY, 
    client_id INTEGER, 
    purchase_date TEXT, 
    FOREIGN KEY (client_id) REFERENCES clients(client_id)
);''')

cursor.execute('''INSERT INTO clients (client_id, client_name) VALUES (1, 'John Doe');''')
cursor.execute('''INSERT INTO clients (client_id, client_name) VALUES (2, 'Jane Smith');''')

cursor.execute('''SELECT * FROM clients;''')
print(cursor.fetchall())

cursor.execute('''INSERT INTO purchases (purchase_id, client_id, purchase_date) VALUES (1, 5, '2024-09-20');''')  

cursor.execute('''SELECT * FROM purchases;''')
print(cursor.fetchall())

conn.commit()
conn.close()
