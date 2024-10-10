import sqlite3  

conn = sqlite3.connect('Learners_Foreign_Key.db')
cursor = conn.cursor()

cursor.execute('PRAGMA foreign_keys = ON;')

cursor.execute('''CREATE TABLE learners (
    learner_id INTEGER PRIMARY KEY, 
    learner_name TEXT NOT NULL);''')

cursor.execute('''CREATE TABLE subjects (
    subject_id INTEGER, 
    subject_name TEXT NOT NULL, 
    department_id INTEGER, 
    PRIMARY KEY (subject_id, department_id));''')

cursor.execute('''CREATE TABLE learner_subjects (
    learner_id INTEGER,
    subject_id INTEGER,
    department_id INTEGER,
    FOREIGN KEY (learner_id) REFERENCES learners(learner_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id, department_id) REFERENCES subjects(subject_id, department_id) ON DELETE CASCADE,
    PRIMARY KEY (learner_id, subject_id, department_id));''')

cursor.execute('INSERT INTO learners (learner_id, learner_name) VALUES (1, "Lalith Kumar");')
cursor.execute('INSERT INTO learners (learner_id, learner_name) VALUES (2, "Yashnwanth Kuntla");')
cursor.execute('INSERT INTO subjects (subject_id, subject_name, department_id) VALUES (101, "Artificial Intelligence", 1);')
cursor.execute('INSERT INTO subjects (subject_id, subject_name, department_id) VALUES (102, "Big Data Analytics", 1);')

cursor.execute('INSERT INTO learner_subjects (learner_id, subject_id, department_id) VALUES (1, 101, 1);')
cursor.execute('INSERT INTO learner_subjects (learner_id, subject_id, department_id) VALUES (2, 102, 1);')

print("\nCurrent data in the learner_subjects table:")
cursor.execute('SELECT * FROM learner_subjects')
for row in cursor.fetchall():
    print(row)

cursor.execute('INSERT INTO learner_subjects (learner_id, subject_id, department_id) VALUES (3, 101, 1);')
cursor.execute('INSERT INTO learner_subjects (learner_id, subject_id, department_id) VALUES (1, 103, 1);')

conn.commit()
conn.close()