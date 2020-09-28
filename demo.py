import sqlite3

#path to demo_data.sqlite3
filepath = 'demo_data.sqlite3'

#creating connection
conn = sqlite3.connect(filepath)

#cursor
cursor = conn.cursor()

#creating the demo table
query = '''
CREATE TABLE IF NOT EXIST demo(
    s varchar,
    x int,
    y int
); '''  

#query execution to populate demo table
cursor.execute(query)

#data Insertion
query2 ='''
INSERT INTO demo VALUES
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
'''
cursor.execute(query2)
conn.commit()
conn.close
