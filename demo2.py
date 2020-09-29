import sqlite3

conn = sqlite3.connect('demo_data2.db')

cursor = conn.cursor()

#create table
demT = ''' 
CREATE TABLE IF NOT EXISTS demo2(
    s varchar,
    x int,
    y int
); ''' 

cursor.execute(demT)

query = '''
INSERT INTO demo2 VALUES
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
'''
cursor.execute('SELECT * FROM demo2')
results = cursor.fetchall()

print(results)

conn.commit()
conn.close