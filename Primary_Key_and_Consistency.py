import sqlite3  

conn = sqlite3.connect('Subjects_Primary_Key_and_Consistency.db')
cursor = conn.cursor() 

cursor.execute(''' 
    CREATE TABLE subjects (
        subject_id INTEGER,
        subject_name TEXT NOT NULL,
        division_id INTEGER,
        PRIMARY KEY (subject_id, division_id)
    );
''')

cursor.execute('''INSERT INTO subjects (subject_id, subject_name, division_id) VALUES (101, 'Machine Learning', 1);''')
cursor.execute('''INSERT INTO subjects (subject_id, subject_name, division_id) VALUES (101, 'Machine Learning', 2);''')

try:
    cursor.execute('''INSERT INTO subjects (subject_id, subject_name, division_id) VALUES (101, 'Data Science', 1);''')
except sqlite3.IntegrityError as e:
    print("Error:", e)

print("\nSubjects table:")
cursor.execute('SELECT * FROM subjects')
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()
