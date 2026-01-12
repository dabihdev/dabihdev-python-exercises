import numpy as np
import matplotlib.pyplot as plt

class SimpleLinearRegression:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.lr = learning_rate
        self.iterations = iterations
        self.m = 0  # Slope
        self.b = 0  # Intercept
        self.loss_history = [] # To store MSE over time

    def fit(self, x, y):
        n = len(x)
        
        for _ in range(self.iterations):
            # 1. Generate predictions
            y_pred = self.m * x + self.b

            # Calculate Mean Squared Error (Loss)
            mse = np.mean((y - y_pred)**2)
            self.loss_history.append(mse)
            
            # 2. Calculate partial derivatives (Gradients)
            # Derivative of MSE with respect to m
            dm = (-2 / n) * np.sum(x * (y - y_pred))
            # Derivative of MSE with respect to b
            db = (-2 / n) * np.sum(y - y_pred)
            
            # 3. Update parameters
            self.m -= self.lr * dm
            self.b -= self.lr * db

    def predict(self, x):
        return self.m * x + self.b

    def plot_loss_curve(self):
        x = np.arange(0, self.iterations)
        y = np.array(self.loss_history)
        plt.plot(x, y)
        plt.show()

# TEST CASES
# Sample Data (Celsius to Fahrenheit)
X_train = np.array([0, 10, 20, 30, 40], dtype=float)
y_train = np.array([32, 50, 68, 86, 104], dtype=float)

# Initialize and train
model = SimpleLinearRegression(learning_rate=0.001, iterations=10000)
model.fit(X_train, y_train)

# Results
print(f"Calculated Slope (m): {model.m:.2f}")     # Expected: ~1.80
print(f"Calculated Intercept (b): {model.b:.2f}") # Expected: ~32.00

# Prediction Test
test_val = 100
prediction = model.predict(test_val)
print(f"Prediction for {test_val}°C: {prediction:.2f}°F") # Expected: 212.00

# PLOT LOSS CURVE
model.plot_loss_curve()
