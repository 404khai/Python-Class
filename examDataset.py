import pandas as pd

examData={
    "Name": ["Mike", "David", "Daniel", "Korede", "Stephanie", "Frank"],
    "Study Hours": [5, 3, 8, 2, 7, 4],
    "Sleep Hours": [7,6,6,5,8,7],
    "Scores": [80, 60, 92, 55, 88, 72]
}

df = pd.DataFrame(examData)

print(df)