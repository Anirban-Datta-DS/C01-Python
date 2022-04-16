import sqlite3
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect(r"C:\Data\SQLite3\pythonsqlite.db")
 
# cursor object
cursor_obj = connection_obj.cursor()
 
# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS GEEK")
 
# Creating table
table = """ CREATE TABLE TEAM (
            First_Name CHAR(25) NOT NULL,
            Last_Name CHAR(25),
            Experience FLOAT,
            Python INT,
            Statistics INT
        ); """
 
cursor_obj.execute(table)
 
print("Table is Ready")
 
# Close the connection
connection_obj.close()