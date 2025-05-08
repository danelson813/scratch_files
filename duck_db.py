import duckdb
# create a connection to a file called 'file.db'
con = duckdb.connect('file.db')
# create a table and load data into it
con.sql('CREATE TABLE test(i INTEGER)')
con.sql('INSERT INTO test VALUES (42)')
# query the table
con.table('test').show()
# explicitly close the connection
con.close()

# If connecting again to file.db, your data will still be there

con = duckdb.connect('file.db')
con.sql("show all tables")

# **********************************************************************
# create the table "my_table" from the DataFrame "my_df"
# Note: duckdb.sql connects to the default in-memory database connection
duckdb.sql("CREATE TABLE my_table AS SELECT * FROM my_df")

results =duckdb.sql("select * from my_table")