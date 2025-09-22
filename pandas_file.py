import pandas as pd

data={
    "Name": ["John", "Korede", "Daniel"],
    "Age": [25, 30, 28],
    "City": ["Rivers", "Imo", "Lagos"]
}

df = pd.DataFrame(data)

print(df)