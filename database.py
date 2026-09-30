from pathlib import Path
import pandas as pd
import sqlite3

BASE_DIR = Path(__file__).parent

csv_file = BASE_DIR / "users.csv"
db_file = BASE_DIR / "employees.db"

df = pd.read_csv(csv_file)

conn = sqlite3.connect(db_file)

df.to_sql(
    "employees",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Data loaded successfully")