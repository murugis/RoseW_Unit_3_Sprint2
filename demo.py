import sqlite3

#path to demo_data.sqlite3
db = 'demo_data.sqlite3'

#creating connection
conn = sqlite3.connect(db)

#cursor
cursor = conn.cursor()

#dropping the table if it exists to avoid duplicates
cursor.execute('DROP TABLE IF EXISTS demo;')


#creating the demo table
query = '''
CREATE TABLE IF NOT EXISTS demo(
    s varchar,
    x int,
    y int
); '''  

#query execution to populate demo table
cursor.execute(query)

#data Insertion
query2 ='''
INSERT INTO demo(s,x,y) VALUES
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
'''
cursor.execute(query2)
conn.commit()

# How many rows in demo table?
query3 = '''
SELECT COUNT(*) FROM demo;
'''
total_rows = cursor.execute(query3).fetchall()
print('Total Rows:', total_rows,)

# How many rows are there where both x and y are at least 5?
query4 = '''
SELECT *
FROM demo
WHERE x >= 5 AND y >= 5;
'''
rows_x_y= cursor.execute(query4).fetchall()
print('Rows where x and y are at least 5:', rows_x_y)

# How many unique values of y are there?
query5 = '''
SELECT COUNT(DISTINCT y) FROM demo;
'''
unique_y = cursor.execute(query5).fetchall()
print('Number of unique values of y:', unique_y)

conn.commit()
cursor.close()
conn.close()

