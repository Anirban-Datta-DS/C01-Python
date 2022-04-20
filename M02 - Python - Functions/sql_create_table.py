import sqlite3

#Connecting to sqlite
database = r"C:\Data\SQLite3\pythonsqlite.db"
conn = sqlite3.connect(database)
print(f'Type of conn: {type(conn)}')
print()

#Creating a cursor object using the cursor() method
cursor = conn.cursor()
print(f'Type of cursor: {type(cursor)}')
print()

cursor.execute("DROP TABLE TEAM")
print('Table dropped.')


#Creating table as per requirement
sql_query ='''CREATE TABLE IF NOT EXISTS TEAM(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   EXPERIENCE FLOAT,
   STATISTICS INT,
   PYTHON INT,
   R INT
)'''
cursor.execute(sql_query)
print("Table created successfully.")

# Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()