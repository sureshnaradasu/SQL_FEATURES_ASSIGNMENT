import sqlite3

conn = sqlite3.connect('Pupils_Composite_Key_Constraint.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE pupils (
    pupil_id INTEGER PRIMARY KEY,
    pupil_name TEXT NOT NULL);''')

cursor.execute('''CREATE TABLE subjects (
    subject_id INTEGER PRIMARY KEY,
    subject_name TEXT NOT NULL);''')

cursor.execute('''CREATE TABLE pupil_subjects (
    pupil_id INTEGER,
    subject_id INTEGER,
    PRIMARY KEY (pupil_id, subject_id),
    FOREIGN KEY (pupil_id) REFERENCES pupils(pupil_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id));''')

cursor.execute('INSERT INTO pupils (pupil_id, pupil_name) VALUES (1, "Ben");')
cursor.execute('INSERT INTO pupils (pupil_id, pupil_name) VALUES (2, "Harsh");')

cursor.execute('INSERT INTO subjects (subject_id, subject_name) VALUES (101, "Artificial Intelligence");')
cursor.execute('INSERT INTO subjects (subject_id, subject_name) VALUES (102, "Big Data Analytics");')

cursor.execute('INSERT INTO pupil_subjects (pupil_id, subject_id) VALUES (1, 1023);')
cursor.execute('INSERT INTO pupil_subjects (pupil_id, subject_id) VALUES (2, 1011);')

print("\nCurrent data in the pupil_subjects table:")
cursor.execute('SELECT * FROM pupil_subjects')
for row in cursor.fetchall():
    print(row)

try:
    cursor.execute('INSERT INTO pupil_subjects (pupil_id, subject_id) VALUES (1, 1023);') 
except sqlite3.IntegrityError as e:
    print("Error:", e)  

cursor.execute('INSERT INTO pupil_subjects (pupil_id, subject_id) VALUES (1, 1011);')

conn.commit()
conn.close()
