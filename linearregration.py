import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
Y = np.array([2, 4, 5, 4, 5, 7])

# Create and train model
model = LinearRegression()
model.fit(X, Y)

# Predict values
Y_pred = model.predict(X)

# Print equation
print("Slope (m):", model.coef_[0])
print("Intercept (b):", model.intercept_)

# Plot data points
plt.scatter(X, Y, color='blue', label='Actual Data')

# Plot regression line
plt.plot(X, Y_pred, color='red', linewidth=2, label='Regression Line')

plt.title("Linear Regression")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.grid(True)

plt.show()