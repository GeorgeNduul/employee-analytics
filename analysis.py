import pandas as pd
import sqlite3

conn = sqlite3.connect("employees.db")

df = pd.read_sql(
    "SELECT * FROM employees",
    conn
)

print(df.head())

conn.close()
