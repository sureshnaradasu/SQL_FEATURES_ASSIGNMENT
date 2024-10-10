import sqlite3

conn = sqlite3.connect('Employee_Exisiting_Table_Check_Constrain.db')
cursor = conn.cursor() 

cursor.execute('select * from employees')
print(cursor.fetchall())

try:
    cursor.execute('INSERT INTO employees (employee_id, employee_name, salary) VALUES (3, "Lucky", -80000);')
except sqlite3.IntegrityError as e:
    print("Error:", e)

conn.commit()
conn.close()