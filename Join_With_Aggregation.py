import sqlite3

conn = sqlite3.connect('Clients_Join_With_Aggregation.db')
cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS clients (
        client_id INTEGER PRIMARY KEY,
        client_name TEXT NOT NULL
    );
''')

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        client_id INTEGER,
        product_id INTEGER NOT NULL,
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
    INSERT INTO orders (order_id, client_id, product_id) 
    VALUES (?, ?, ?);
''', [
    (201, 1, 1),  
    (202, 1, 2),  
    (203, 2, 1), 
    (204, 2, 3),  
    (205, 3, 2),  
    (206, 3, 4)  
])

cursor.execute("SELECT * FROM orders")
print("\n Orders Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute(''' 
    SELECT clients.client_name, COUNT(orders.product_id) AS total_products_ordered
    FROM clients
    JOIN orders ON clients.client_id = orders.client_id
    GROUP BY clients.client_name;
''')

rows = cursor.fetchall()

print("\n Client Name    | Total Products Ordered")
print("--------------------------------------")
for row in rows:
    client_name = row[0] 
    total_products_ordered = row[1]  
    print(f"{client_name:<16} | {total_products_ordered}")

conn.commit()
conn.close()
