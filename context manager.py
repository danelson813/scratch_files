'''
with open("example.txt", "r") as file:
    contents = file.read()
    print(contents)


Timing Context Manager
A timing context manager can be used to measure the execution time of a block of code. Here's an example:

import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        print(f"Execution time: {end_time - self.start_time}")

with Timer():
    # some block of code to measure execution time
    time.sleep(2)
In this example, the "Timer" class is defined as a context manager. The "enter" method records the start time of the block of code, and the "exit" method calculates the execution time and prints it to the console.



Context managers can be used to manage transactions in a database. Here's an example using the SQLite library:

import sqlite3

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        
    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

with Database("example.db") as cursor:
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
In this example, the "Database" class is defined as a context manager. The "enter" method creates a connection to the database and returns a cursor object for executing queries. The "exit" method commits the transaction if no exceptions were raised, or rolls back the transaction if an exception occurred.


'''