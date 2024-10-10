import sqlite3

conn = sqlite3.connect('Members_Unique_Constraint.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE members (
    member_id INTEGER PRIMARY KEY,
    member_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);''')

cursor.execute('''INSERT INTO members (member_id, member_name, email) VALUES (1, 'John Doe', 'john@example.com');''')
cursor.execute('''INSERT INTO members (member_id, member_name, email) VALUES (2, 'Jane Smith', 'jane@example.com');''')

cursor.execute('''SELECT * FROM members;''')
print(cursor.fetchall())

cursor.execute('''INSERT INTO members (member_id, member_name, email) VALUES (3, 'Sam Wilson', 'john@example.com');''')

conn.commit()
conn.close()