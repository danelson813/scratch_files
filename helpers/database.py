# sqlite3_snippet.py
import sqlite3 as sq
import pandas as pd
import pathlib


def put_into_sqlite3(df: pd.DataFrame, table_name: pathlib, db_name: str) -> None:
    conn = sq.connect(f'data/{db_name}.sqlite')  # creates file
    cur = conn.cursor()  # cursor
    cur.execute(f"""DROP TABLE IF EXISTS {table_name}""")
    df.to_sql(table_name, conn, if_exists='replace', index=False)  # writes to file
    conn.close()  # good practice: close connection


def get_sqlite3_to_df(table_name, db_name) -> pd.DataFrame:
    conn = sq.connect(f'data/{db_name}.sqlite')
    df_ = pd.read_sql(f'select * from {table_name}', conn, index_col='rank')
    conn.close()
    return df_
