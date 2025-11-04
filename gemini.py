import pandas as pd

# Create a sample DataFrame
data = {'event': ['Event A', 'Event B', 'Event C', 'Event D', 'Event E'],
        'date': ['2023-06-15', '2023-07-01', '2024-07-20', '2024-08-10', '2025-07-05']}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Step 1: Ensure the 'date' column is in datetime format
df['date'] = pd.to_datetime(df['date'])

# Step 2: Filter for dates in July
july_dates_df = df[df['date'].dt.month == 7]

print("\nDataFrame with only July dates:")
print(july_dates_df)

# If you only want the 'date' column from the filtered DataFrame:
only_july_dates_series = july_dates_df['date']
print("\nSeries with only July dates (the 'date' column):")
print(only_july_dates_series)




import pandas as pd

# Create a sample DataFrame
data = {'event': ['Event A', 'Event B', 'Event C', 'Event D', 'Event E'],
        'date': ['2023-06-15', '2023-07-01', '2024-07-20', '2024-08-10', '2025-07-05']}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Step 1: Ensure the 'date' column is in datetime format
df['date'] = pd.to_datetime(df['date'])

# Step 2: Filter for dates in July
july_dates_df = df[df['date'].dt.month == 7]

print("\nDataFrame with only July dates:")
print(july_dates_df)

# If you only want the 'date' column from the filtered DataFrame:
only_july_dates_series = july_dates_df['date']
print("\nSeries with only July dates (the 'date' column):")
print(only_july_dates_series)
'''
SELECT
    your_date_column,
    DATE_PART('month', your_date_column) AS month_number
FROM
    your_table;


SELECT
    your_date_column,
    DATE_PART('month', your_date_column) AS month_number
FROM
    your_table;
'''

import duckdb
import pandas as pd

# Create a sample Pandas DataFrame (or load data from a CSV, etc.)
data = {'event': ['Event A', 'Event B', 'Event C', 'Event D', 'Event E'],
        'date': ['2023-06-15', '2023-07-01', '2024-07-20', '2024-08-10', '2025-07-05']}
df = pd.DataFrame(data)

# Connect to DuckDB (in-memory database for this example)
con = duckdb.connect(database=':memory:', read_only=False)

# Register the Pandas DataFrame as a DuckDB table
con.execute("CREATE TABLE my_dates AS SELECT * FROM df")

# Query to extract the month
result = con.execute("""
    SELECT
        date,
        EXTRACT(MONTH FROM date) AS month_number
    FROM
        my_dates
    WHERE
        EXTRACT(MONTH FROM date) = 7; -- Filter for July (month 7)
""").fetchdf()

print(result)

# Close the connection
con.close()

'''
In DuckDB, you can extract the month from a date (or timestamp) column using the EXTRACT function or the DATE_PART function. Both are equivalent for this purpose.

Here's how you can do it:

1. Using EXTRACT:

SQL

SELECT
    your_date_column,
    EXTRACT(MONTH FROM your_date_column) AS month_number
FROM
    your_table;
2. Using DATE_PART:

SQL

SELECT
    your_date_column,
    DATE_PART('month', your_date_column) AS month_number
FROM
    your_table;
Example in a DuckDB Python context:

If you're using DuckDB with Python (e.g., loading data into DuckDB and then querying it), here's how you'd typically do it:

Python

import duckdb
import pandas as pd

# Create a sample Pandas DataFrame (or load data from a CSV, etc.)
data = {'event': ['Event A', 'Event B', 'Event C', 'Event D', 'Event E'],
        'date': ['2023-06-15', '2023-07-01', '2024-07-20', '2024-08-10', '2025-07-05']}
df = pd.DataFrame(data)

# Connect to DuckDB (in-memory database for this example)
con = duckdb.connect(database=':memory:', read_only=False)

# Register the Pandas DataFrame as a DuckDB table
con.execute("CREATE TABLE my_dates AS SELECT * FROM df")

# Query to extract the month
result = con.execute("""
    SELECT
        date,
        EXTRACT(MONTH FROM date) AS month_number
    FROM
        my_dates
    WHERE
        EXTRACT(MONTH FROM date) = 7; -- Filter for July (month 7)
""").fetchdf()

print(result)

# Close the connection
con.close()
Key points:

EXTRACT(MONTH FROM date_column) or DATE_PART('month', date_column): These are the primary functions to get the numerical month (1 for January, 7 for July, etc.) from a date or timestamp column.

WHERE EXTRACT(MONTH FROM date) = 7: This is how you would filter your results to only include dates in July.

DuckDB's date and time functions are quite comprehensive and align well with standard SQL.
'''


'''
game plan:
read the Ledger 26 file into a df
put into a duckdb file
seperate out the activities for the month
seperate into checks and deposits
put them into an excel sheet as a report
Lions
'''