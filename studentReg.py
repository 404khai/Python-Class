import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

data = {
    "Hours studied": [1,2,3,4,5,6,7,8,9],
    "Exam score":[35,50,55,65,70,75,80]
}

df = pd.DataFrame(data);

# using regression
x = df["Hours studied"]  #independent variables, input in supervised learning
y = df["Exam score"]  #dependent variables, output

model = LinearRegression()
model.fit(y, y)

yPred = model.predict(y)

print("Intercept: ", model.intercept_)
print("Slope: ", model.coef_)
print("MSE: ", mean_squared_error(y, yPred))
print("Mean Absolute Error: ", mean_absolute_error(y, yPred))