import sqlite3

#db
dbpath = 'demo_data.sqlite3'

#connecting the demo_data DB
conn = sqlite3.connect(dbpath)


cursor = conn.cursor()

# How many rows are in the demo table?
query = '''
SELECT
  COUNT(*)
FROM demo
'''

results = cursor.execute(query).fetchall()
print(results)

#How many rows are there whre both 'x' and 'y' are at least 5
query2 = '''
SELECT *
FROM demo
WHERE  x >= 5 and y >= 5
'''

results2 = cursor.execute(query2).fetchall()
result2 = len(results2)
print(results2)

# How many unique values are there for 'y'
query3 = '''
SELECT
  COUNT(DISTINCT y)
FROM demo
'''

results3 = cursor.execute(query).fetchall()
print(results3)