import os
import sqlite3


## Query All the Tables!
### Setup
"""
Before we get started you'll need a few things.
1. Download the [Chinook Database here](https://github.com/bundickm/Study-Guides/blob/master/data/Chinook_Sqlite.sqlite)
2. The schema can be [found here](https://github.com/bundickm/Study-Guides/blob/master/data/Chinook%20Schema.png)
3. Create a file named `study_part2.py` and complete the exercise below. The only library you should need to import is `sqlite3`. Don't forget to be PEP8 compliant!
4. Add a connection to the chinook database so that you can answer the queries below.
"""

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "chinook.db") 

connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()



### Queries
'''**Single Table Queries**'''

query = """
SELECT CustomerId, AVG(Total) FROM invoices
GROUP BY CustomerId LIMIT 5;
"""
print("1. Find the average invoice total for each customer, return the details for the first 5 ID's")
results = cursor.execute(query).fetchall()
for result in results:
    print(result)



print('\n\n2. Return all columns in Customer for the first 5 customers residing in the United States')
query = """
SELECT FirstName, LastName From customers
WHERE Country = "USA"
LIMIT 5;
"""
results = cursor.execute(query).fetchall()
for result in results:
    print(result)



print('\n\n3. Which employee does not report to anyone?')
query = """
SELECT LastName, FirstName FROM employees
WHERE ReportsTo IS NULL;
"""
results = cursor.execute(query).fetchall()
print(results)




print('\n\n4. Find the number of unique composers')
query = "SELECT COUNT(distinct ArtistId) FROM albums;"
results = cursor.execute(query).fetchone()
print(results)



print('\n\n5. How many rows are in the Track table?')
query = "SELECT COUNT(*) FROM tracks;"
results = cursor.execute(query).fetchone()
print(results)




"""
**Joins**
"""



print('\n\n6. Get the name of all Black Sabbath tracks and the albums they came off of')
query = """
SELECT 
	--artists.Name, 
	Albums.title as Album,
	tracks.name as TrackName
FROM artists
LEFT JOIN albums ON artists.ArtistId = albums.ArtistId
LEFT JOIN tracks ON albums.AlbumId = tracks.AlbumId
WHERE artists.Name = "Black Sabbath";

"""
results = cursor.execute(query).fetchall()
for result in results:
    print(result)



print('\n\n7. What is the most popular genre by number of tracks?')
query = """
SELECT
	genres.Name as Genre
	,COUNT(tracks.Name) as NumberOfTracks
FROM genres
Left JOIN tracks on tracks.GenreId = genres.GenreId
GROUP BY genres.Name
Order BY NumberOfTracks DESC
LIMIT 1;
"""
results = cursor.execute(query).fetchone()
print(results)



print('\n\n8. Find all customers that have spent over $45')
query = """
SELECT * FROM
(
	SELECT 
		customers.LastName
		,customers.FirstName
		,SUM(invoices.Total) as Total_Spending
	FROM customers
	LEFT JOIN invoices on customers.CustomerId = invoices.CustomerId
	GROUP BY customers.CustomerId
) 
WHERE Total_Spending >= 45
"""
results = cursor.execute(query).fetchall()
for result in results:
    print(result)





print('''\n\n9. Find the first and last name, title, and the number of customers each employee has helped.
 If the customer count is 0 for an employee, it doesn't need to be displayed. 
 Order the employees from most to least customers.''')
query = """
 SELECT * FROM
(
	SELECT 
		employees.FirstName
		,employees.LastName
		,employees.Title
		,sum(customers.CustomerId) as NumberOfCustomer
	FROM employees
	LEFT JOIN customers ON employees.EmployeeId = customers.SupportRepId
	LEFT JOIN invoices ON customers.CustomerId = invoices.CustomerId
	GROUP BY employees.EmployeeId
)
WHERE NumberOfCustomer IS NOT NULL;
"""
results = cursor.execute(query).fetchall()
for result in results:
    print(result)









print("""\n\n10. Return the first and last name of each employee and who they report to
""")
query = """
SELECT 
	employees2.LastName 
	,employees2.FirstName 
	,employees1.LastName AS ReportTo_LastName
	,employees1.FirstName AS ReportTo_FirstName
FROM employees as employees1
JOIN employees as employees2 ON employees1.EmployeeId = employees2.ReportsTo
ORDER BY ReportTo_LastName;
"""
results = cursor.execute(query).fetchall()
for result in results:
    print(result)