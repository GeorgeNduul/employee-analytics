# api_extract.py

import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data)
df.to_csv(
    "users.csv",
    index=False
)

print(df.head())