import sqlite3

conn = sqlite3.connect('Clients_Natural_Join.db')
cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE clients (
        client_id INTEGER PRIMARY KEY,
        client_name TEXT NOT NULL
    );
''')

cursor.execute(''' 
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        client_id INTEGER,
        order_date TEXT NOT NULL,
        FOREIGN KEY (client_id) REFERENCES clients(client_id)
    );
''')

cursor.executemany(''' 
    INSERT INTO clients (client_id, client_name) 
    VALUES (?, ?);
''', [
    (1, 'Alice Brown'),
    (2, 'Bob Johnson'),
    (3, 'Charlie Davis')
])

cursor.execute("SELECT * FROM clients")
print("\n Clients Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.executemany(''' 
    INSERT INTO orders (order_id, client_id, order_date) 
    VALUES (?, ?, ?);
''', [
    (201, 1, '2024-09-02'),  
    (202, 2, '2024-09-15'),  
    (203, 1, '2024-09-22'),  
    (204, 3, '2024-09-04')   
])

cursor.execute("SELECT * FROM orders")
print("\n Orders Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute(''' 
    SELECT * 
    FROM clients
    NATURAL JOIN orders;
''')

print("\n Natural Join \n")
rows = cursor.fetchall()
print("Client Name    | Order ID | Order Date")
print("-------------------------------------")
for row in rows:
    client_name = row[1] 
    order_id = row[2]      
    order_date = row[3]    
    print(f"{client_name:<14} | {order_id:<8} | {order_date}")

conn.commit()
conn.close()
