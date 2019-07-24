import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

query = """
CREATE TABLE students (
userid VARCHAR(12), 
password VARCHAR(12), 
name TEXT, 
address TEXT, 
country VARCHAR(20),
zipcode VARCHAR(10),
email TEXT,
sex VARCHAR(10),
language TEXT,
about TEXT)
"""

conn.execute(query)
print("Table created successfully")
conn.close()