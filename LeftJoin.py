import sqlite3

connection = sqlite3.connect('Customer_Orders_Left_Join.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS customers ( customer_id INTEGER PRIMARY KEY, customer_name TEXT NOT NULL);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS orders ( order_id INTEGER PRIMARY KEY, customer_id INTEGER, product_name TEXT NOT NULL, FOREIGN KEY (customer_id) REFERENCES customers(customer_id));''')

cursor.executemany('''INSERT INTO customers (customer_id, customer_name) VALUES (?, ?);''', [
    (1, 'Alice Johnson'),
    (2, 'Bob Smith'),
    (3, 'Charlie Davis'),
    (4, 'David Brown'),
    (5, 'Eva Green')
])

cursor.execute("SELECT * FROM customers")
print("\nCustomers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.executemany('''INSERT INTO orders (order_id, customer_id, product_name) VALUES (?, ?, ?);''', [
    (101, 1, 'Refrigerator'),
    (102, 2, 'Microwave Oven'),
    (103, 1, 'Air Conditioner'),
    (104, 3, 'Washing Machine'),
    (105, 4, 'Dishwasher'),
    (106, 5, 'Vacuum Cleaner'),
    (107, 3, 'Water Purifier'),
    (108, 2, 'Blender')
])

cursor.execute("SELECT * FROM orders")
print("\nOrders Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''SELECT customers.customer_name, orders.product_name FROM customers LEFT JOIN orders ON customers.customer_id = orders.customer_id;''')
print("\nLeft Join\n")
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.commit()
connection.close()
