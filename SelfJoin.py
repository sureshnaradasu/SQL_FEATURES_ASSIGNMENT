import sqlite3

conn = sqlite3.connect('Company_Employees_Self_Join.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY, 
        employee_name TEXT NOT NULL,      
        manager_id INTEGER,           
        FOREIGN KEY (manager_id) REFERENCES employees(employee_id) 
    );
''')

cursor.executemany(''' 
    INSERT INTO employees (employee_id, employee_name, manager_id) 
    VALUES (?, ?, ?);
''', [
    (1, 'Alice Johnson', None),       
    (2, 'Bob Smith', 1),       
    (3, 'Charlie Davis', 1),  
    (4, 'David Lee', 2),       
    (5, 'Eve Stone', 2),  
    (6, 'Frank Wright', 3)      
])

cursor.execute("SELECT * FROM employees")
print("\n Employees Table\n")
rows = cursor.fetchall() 
for row in rows:
    print(row)

cursor.execute('''
    SELECT e.employee_name AS Employee, m.employee_name AS Manager
    FROM employees e
    LEFT JOIN employees m ON e.manager_id = m.employee_id; 
''')

rows = cursor.fetchall()
print("\n Self Join \n")
for row in rows:
    print(row)

conn.commit()
conn.close()
