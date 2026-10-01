import sqlite3

conn = sqlite3.connect("employees.db")

cursor = conn.cursor()

query = """
SELECT e.name,
       d.department
FROM employees e
INNER JOIN departments d
ON e.id = d.id
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(row)

conn.close()
