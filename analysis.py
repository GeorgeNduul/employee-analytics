import sqlite3

conn = sqlite3.connect("employees.db")

cursor = conn.cursor()

query = """
SELECT *
FROM employees
"""

cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()