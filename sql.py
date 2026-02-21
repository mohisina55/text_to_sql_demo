import sqlite3

##connect to sqlite
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor() #responsible for inserting,retrieving and managing data in the database
##create a table
STUDENT_TABLE = """
CREATE TABLE students(
    Name varchar(25),
    class varchar(25),
    section varchar(25),
    marks int
)
"""
cursor.execute(STUDENT_TABLE)
##insert data into the table
cursor.execute("INSERT INTO students VALUES('John Doe','10th','A',85)")
cursor.execute("INSERT INTO students VALUES('Jane Smith','10th','B',90)")
cursor.execute("INSERT INTO students VALUES('Alice Johnson','10th','A',78)")
cursor.execute("INSERT INTO students VALUES('Bob Brown','10th','B',92)")
cursor.execute("INSERT INTO students VALUES('Charlie Davis','10th','A',88)")
cursor.execute("INSERT INTO students VALUES('Emily Wilson','10th','B',95)")
cursor.execute("INSERT INTO students VALUES('David Lee','10th','A',80)")    

print("Data inserted successfully")

data = cursor.execute("SELECT * FROM students")
for row in data:
    print(row)
##commit the changes to the database
connection.commit()
connection.close()