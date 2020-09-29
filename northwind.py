import sqlite3

#DB path
dbpath = 'northwind_small.sqlite3'

#connecting to the database
conn = sqlite3.connect(dbpath)

cursor = conn.cursor()

# QUESTIONS
#Whar are the most expensive items(per unit price)
# in the database

query = '''
SELECT
  ProductName,
  UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
'''
results = cursor.execute(query).fetchall()
print('Most expensive products',results, '\n')

# What is the average age of an employee at the time of hiring
query2 = '''
SELECT
  AVG(HireDate-BirthDate)
FROM Employee;
'''
results2 = cursor.execute(query2).fetchall()
print('Average age of employee at the time of hiring', results2, '\n')

# How does the average age of the employee at hire vary by city
query3 = '''
SELECT AVG(HireDate-BirthDate), City
FROM Employee
GROUP BY City;
'''
results3 = cursor.execute(query3).fetchall()
print('Average age by city', results3,'\n')

### Part 3 - Sailing the Northwind Seas

# What are the ten most expensive items(per unit)
# in the database *and* their suppliers?

query4 = '''
SELECT
  p.ProductName,
  s.Companyname,
  p.UnitPrice
FROM Product as p
JOIN Supplier s ON p.SupplierId = s.Id
ORDER BY p.UnitPrice DESC
LIMIT 10
'''
results4 = cursor.execute(query4).fetchall()
print('Most expensive by company:',results4,'\n')

# What is the largest category(by number of unique products in it)?
query5 = '''
SELECT
  c.CategoryName,
  COUNT(c.Id) as cat_count
FROM category as c
JOIN Product p ON c.Id = p.CategoryId
GROUP BY c.CategoryName
ORDER BY cat_count DESC
'''
results5 = cursor.execute(query5).fetchall()
print('Largest category',results5, '\n')

# Who is the employee with the most Territories?
query6 = '''
SELECT 
  et.EmployeeId,
  e.FirstName,
  e.Lastname,
  COUNT(et.TerritoryId) as TotalTerritory
FROM Employee as e
JOIN EmployeeTerritory et on e.Id = et.EmployeeId
GROUP BY et.EmployeeId
ORDER BY TotalTerritory DESC
LIMIT 1
'''

results6 = cursor.execute(query6).fetchone()
print('Employee with the most territories :',results6)


