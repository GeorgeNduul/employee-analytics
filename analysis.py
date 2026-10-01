import sqlite3

conn = sqlite3.connect("employees.db")

cursor = conn.cursor()

query = """
SELECT COUNT(*)
FROM employees
"""
query = """
SELECT MAX(id)
FROM employees
"""
query = """
SELECT MIN(id)
FROM employees
"""

cursor.execute(query)

result = cursor.fetchone()

print(result)

conn.close()