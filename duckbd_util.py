import duckdb
from pathlib import Path


def send2db(filename):
    conn = duckdb.connect('Books.db')
    c = conn.cursor()
    pathname = Path(filename)
    
    c.execute(
        "CREATE OR REPLACE TABLE books 
        AS SELECT * FROM read_csv_auto(pathname);"
    )

    books = c.execute("SELECT * FROM books").fetchall()
    for book in books:
        print(book)
    conn.close()

if __name__ == "__main__":
    send2db(False)
