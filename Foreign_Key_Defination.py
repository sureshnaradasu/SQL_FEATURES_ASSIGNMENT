import sqlite3

conn = sqlite3.connect('Writers_Publications_Foreign_Key_Definition.db')
cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS writers (
        writer_id INTEGER PRIMARY KEY,
        writer_name TEXT NOT NULL
    );
''')

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS publications (
        publication_id INTEGER PRIMARY KEY,
        publication_title TEXT NOT NULL,
        writer_id INTEGER,
        FOREIGN KEY (writer_id) REFERENCES writers(writer_id)
    );
''')

cursor.executemany(''' 
    INSERT INTO writers (writer_id, writer_name) 
    VALUES (?, ?);
''', [
    (1, 'Jane Austen'),
    (2, 'Arthur C. Clarke'),
    (3, 'George Orwell')
])

cursor.execute("SELECT * FROM writers")
print("\n Writer Table \n")
writers_rows = cursor.fetchall()
for row in writers_rows:
    print(row)

cursor.executemany(''' 
    INSERT INTO publications (publication_id, publication_title, writer_id) 
    VALUES (?, ?, ?);
''', [
    (1, 'Pride and Prejudice', 1),
    (2, '2001: A Space Odyssey', 2),
    (3, '1984', 3)
])

cursor.execute("SELECT * FROM publications")
print("\n Publications Table \n")
publications_rows = cursor.fetchall()
for row in publications_rows:
    print(row)

conn.commit()
conn.close()
