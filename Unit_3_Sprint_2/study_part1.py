import os
import sqlite3


"""
## Starting From Scratch
Create a file named `study_part1.py` and complete the exercise below. The only library you should need to import is `sqlite3`. Don't forget to be PEP8 compliant!
1. Create a new database file call `study_part1.sqlite3`
"""

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "study_part1.sqlite3")


"""
2. Create a table with the following columns
```
 student - string
 studied - string
 grade - int
 age - int
 sex - string
 ```
"""

connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()

#Drop Table
cursor.execute('DROP TABLE IF EXISTS students;')


create_table_query = """
CREATE TABLE  IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    ,student VARCHAR(30)
    ,studied TEXT
    ,grade INTEGER
    ,age INTEGER
    ,sex INTEGER
);
"""

cursor.execute(create_table_query)



"""
3. Fill the table with the following data
"""

thundercats = [
    ('Lion-O', 'True', 85, 24, 'Male'),
    ('Cheetara', 'True', 95, 22, 'Female'),
    ('Mumm-Ra', 'False', 65, 153, 'Male'),
    ('Snarf', 'False', 70, 15, 'Male'),
    ('Panthro', 'True', 80, 30, 'Male')
]


for thundercat in thundercats:

    insert_query = f'''
        INSERT INTO students
        (student, studied, grade, age, sex)
        VALUES {thundercat}
    '''
    cursor.execute(insert_query)
    

connection.commit()

"""
4. Save your data. You can check that everything is working so far if you can view the table and data in DBBrowser
"""


"""
5. Write the following queries to check your work. 
Querie outputs should be formatted for readability, 
don't simply print a number to the screen 
with no explanation, add context.
"""
query = 'SELECT AVG(age) FROM students;'
results = cursor.execute(query).fetchone()
print("What is the average age? Expected Result - 48.8", results)



query = "SELECT student FROM students WHERE sex = 'Female';"
results = cursor.execute(query).fetchall()
print("What are the name of the female students? Expected Result - 'Cheetara'", results)




query = """
    SELECT count(student) FROM students
    WHERE studied = 'True';
    """
results = cursor.execute(query).fetchone()
print("How many students studied? Expected Results - 3", results)




query =     """
    SELECT student FROM students
    ORDER BY student;
    """
results = cursor.execute(query).fetchall()
print("Return all students and all columns, sorted by student names in alphabetical order.", results)

