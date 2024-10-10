import sqlite3

conn = sqlite3.connect('Product_Suppliers_Right_Join.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS suppliers (
        supplier_id INTEGER PRIMARY KEY,
        supplier_name TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS product_suppliers (
        product_id INTEGER,
        supplier_id INTEGER,
        FOREIGN KEY (product_id) REFERENCES products(product_id),
        FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
    );
''')

cursor.executemany('''
    INSERT INTO products (product_id, product_name) 
    VALUES (?, ?);
''', [
    (1, 'Gaming Console'),
    (2, 'Fitness Tracker'),
    (3, 'Smart Speaker'),
    (4, 'Drone'),
    (5, 'VR Headset')
])

cursor.execute("SELECT * FROM products")
print("\nProducts Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.executemany('''
    INSERT INTO suppliers (supplier_id, supplier_name) 
    VALUES (?, ?);
''', [
    (1, 'Innovative Tech Solutions'),
    (2, 'Digital Devices Hub'),
    (3, 'NextGen Electronics')
])

cursor.execute("SELECT * FROM suppliers")
print("\nSuppliers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.executemany('''
    INSERT INTO product_suppliers (product_id, supplier_id) 
    VALUES (?, ?);
''', [
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3)
])

cursor.execute("SELECT * FROM product_suppliers")
print("\nProduct Suppliers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Simulating a RIGHT JOIN by swapping the order of the tables in a LEFT JOIN
cursor.execute('''
    SELECT products.product_name, suppliers.supplier_name  
    FROM suppliers
    LEFT JOIN product_suppliers ON suppliers.supplier_id = product_suppliers.supplier_id
    LEFT JOIN products ON product_suppliers.product_id = products.product_id;
''')

rows = cursor.fetchall()

print("\nSimulated Right Join\n")
for row in rows:
    print(row)

conn.commit()
conn.close()