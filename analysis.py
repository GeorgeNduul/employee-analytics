import pandas as pd
import sqlite3

conn = sqlite3.connect("employees.db")

df = pd.read_sql("""
SELECT e.name,
       d.department
FROM employees e
INNER JOIN departments d
ON e.id = d.id
""", conn)

print(df.head())
print(df.isnull().sum())
df.fillna("Unknown", inplace=True)
print(
    df.groupby("department").size()
)

conn.close()