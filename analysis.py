import sqlite3

conn = sqlite3.connect("employees.db")

cursor = conn.cursor()

query = """
SELECT department,
       COUNT(*) AS employee_count
FROM departments
GROUP BY department
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(row)

conn.close()
