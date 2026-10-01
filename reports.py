import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Department": [
        "IT",
        "Finance",
        "HR",
        "Operations",
        "Sales"
    ],
    "Count": [
        2,
        2,
        2,
        2,
        2
    ]
}

df = pd.DataFrame(data)

df.plot(
    x="Department",
    y="Count",
    kind="bar"
)

plt.title("Employees by Department")

plt.show()
