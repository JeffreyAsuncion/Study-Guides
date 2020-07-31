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




'4. Find the number of unique composers'




'5. How many rows are in the Track table?'


"""
**Joins**

6. Get the name of all Black Sabbath tracks and the albums they came off of
7. What is the most popular genre by number of tracks?
8. Find all customers that have spent over $45
9. Find the first and last name, title, and the number of customers each employee has helped. If the customer count is 0 for an employee, it doesn't need to be displayed. Order the employees from most to least customers.
10. Return the first and last name of each employee and who they report to
"""