import sqlite3

conn = sqlite3.connect('Customers_Multiple_Join.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,  
        customer_name TEXT NOT NULL       
    );
''')

cursor.execute('''
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,  
        product_name TEXT NOT NULL     
    );
''')

cursor.execute('''
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,      
        customer_id INTEGER,                
        product_id INTEGER,                
        order_date TEXT NOT NULL,          
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),  
        FOREIGN KEY (product_id) REFERENCES products(product_id)      
    );
''')

cursor.executemany(''' 
    INSERT INTO customers (customer_id, customer_name) 
    VALUES (?, ?); 
''', [
    (1, 'Alice Johnson'),
    (2, 'Bob Smith'),
    (3, 'Charlie Davis')
])

cursor.execute("SELECT * FROM customers")
print("\nCustomers Table\n")
rows = cursor.fetchall()  
for row in rows:
    print(row) 

cursor.executemany(''' 
    INSERT INTO products (product_id, product_name) 
    VALUES (?, ?); 
''', [
    (1, 'Mobile'),
    (2, 'Smart TV'),
    (3, 'Watch'),
    (4, 'Camera')
])

cursor.execute("SELECT * FROM products")
print("\nProducts Table\n")
rows = cursor.fetchall()  
for row in rows:
    print(row)  

cursor.executemany(''' 
    INSERT INTO orders (order_id, customer_id, product_id, order_date) 
    VALUES (?, ?, ?, ?); 
''', [
    (101, 1, 1, '2024-08-09'), 
    (102, 1, 2, '2024-08-22'),  
    (103, 2, 3, '2024-08-19'), 
    (104, 3, 4, '2024-08-02'),  
])

cursor.execute("SELECT * FROM orders")
print("\nOrders Table\n")
rows = cursor.fetchall() 
for row in rows:
    print(row)  

cursor.execute('''
    SELECT customers.customer_name, products.product_name, orders.order_date
    FROM orders
    JOIN customers ON orders.customer_id = customers.customer_id  
    JOIN products ON orders.product_id = products.product_id; 
''')

rows = cursor.fetchall()  

print("Customer Name  | Product Name  | Order Date")
print("-------------------------------------------")
for row in rows:
    customer_name = row[0] 
    product_name = row[1] 
    order_date = row[2]     
    print(f"{customer_name:<14} | {product_name:<12} | {order_date}")  

conn.commit()  
conn.close()  
