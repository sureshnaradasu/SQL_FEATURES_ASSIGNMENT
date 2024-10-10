import sqlite3

conn = sqlite3.connect('Employees_Department_Full_Outer_Join.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE employees (
        employee_id INTEGER PRIMARY KEY,
        employee_name TEXT NOT NULL,
        department_id INTEGER,
        FOREIGN KEY (department_id) REFERENCES departments(department_id)
    );
''')

cursor.execute('''
    CREATE TABLE departments (
        department_id INTEGER PRIMARY KEY,
        department_name TEXT NOT NULL
    );
''')

cursor.executemany('''
    INSERT INTO departments (department_id, department_name) 
    VALUES (?, ?);
''', [
    (1, 'HR'),
    (2, 'Engineering'),
    (3, 'Marketing'),
    (4, 'Sales')
])

cursor.execute("SELECT * FROM departments")
print("\nDepartments Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.executemany('''
    INSERT INTO employees (employee_id, employee_name, department_id) 
    VALUES (?, ?, ?);
''', [
    (1, 'Alice Johnson', 1),      
    (2, 'Bob Smith', 2),     
    (3, 'Charlie Davis', None),  
    (4, 'Diana Miller', 3)      
])

cursor.execute("SELECT * FROM employees")
print("\nEmployees Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''
    SELECT employees.employee_name, departments.department_name
    FROM employees
    LEFT JOIN departments ON employees.department_id = departments.department_id

    UNION

    SELECT employees.employee_name, departments.department_name
    FROM departments
    LEFT JOIN employees ON employees.department_id = departments.department_id;
''')

print("\nFull Outer Join\n")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
