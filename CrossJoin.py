import sqlite3

conn = sqlite3.connect('Shop_Products_Cross_Join.db')
cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL
    );''')

cursor.execute(''' 
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL
    );''')

cursor.executemany(''' 
    INSERT INTO products (product_id, product_name) 
    VALUES (?, ?);
''', [
    (1, 'Smartphone'),
    (2, 'Fitness Tracker'),
    (3, 'Television'),
    (4, 'Notebook')
])

cursor.execute("SELECT * FROM products")
print("\n Products Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.executemany(''' 
    INSERT INTO customers (customer_id, customer_name) 
    VALUES (?, ?);
''', [
    (1, 'Alice Johnson'),
    (2, 'Bob Smith'),
    (3, 'Charlie Davis'),
    (4, 'David Lee')
])

cursor.execute("SELECT * FROM customers")
print("\n Customers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)  

cursor.execute(''' 
    SELECT products.product_name, customers.customer_name
    FROM products
    CROSS JOIN customers;
''')

print("Cross Join \n")
rows = cursor.fetchall()
print("Product Name  | Customer Name") 
print("-----------------------------")

for row in rows:
    product_name = row[0]  
    customer_name = row[1] 
    print(f"{product_name:<12} | {customer_name}")

conn.commit()
conn.close()
