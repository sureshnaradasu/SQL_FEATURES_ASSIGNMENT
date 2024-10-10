import sqlite3

conn = sqlite3.connect('Members_Not_Null.db')
cursor = conn.cursor() 

cursor.execute('''CREATE TABLE members (
    member_id INTEGER PRIMARY KEY, 
    membername TEXT NOT NULL, 
    contact_email TEXT NOT NULL   
);''')

cursor.execute('INSERT INTO members (member_id, membername, contact_email) VALUES (1, "Mehak", "meh@outlook.com");')
cursor.execute('INSERT INTO members (member_id, membername, contact_email) VALUES (2, "Yamini", "yam@outlook.com");')

try:
    cursor.execute('INSERT INTO members (member_id, membername, contact_email) VALUES (3, NULL, "mosa@outlook.com");')
except sqlite3.IntegrityError as e:
    print("Error:", e)

try:
    cursor.execute('INSERT INTO members (member_id, membername, contact_email) VALUES (4, "Moosa", NULL);')
except sqlite3.IntegrityError as e:
    print("Error:", e) 

print("\n Current data in the members table:")
cursor.execute('SELECT * FROM members')
for row in cursor.fetchall():
    print(row) 

conn.commit()
conn.close()
