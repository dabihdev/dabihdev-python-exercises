import numpy as np
import matplotlib.pyplot as plt

class LogisticRegression:
    def __init__(self, learning_rate = 0.01, iterations = 1000):
        self.lr = learning_rate
        self.iterations = iterations
        self.weight = 0.0  # Simplified to a single float for one feature
        self.bias = 0.0

    def _sigmoid(self, z: np.ndarray) -> np.ndarray:
        # z would be the result of the linear model
        # the sigmoid formula would be:
        # 1 / (1 + np.exp(-(w*x + b))
        return 1 / (1 + np.exp(-z))

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Fits the model to a single feature.
        X: 1D array of shape (n_samples,)
        y: 1D array of shape (n_samples,)
        """
        n_samples = X.shape[0] # gets the samples length
        
        # Initialize parameters
        self.weight = 0.0
        self.bias = 0.0

        for _ in range(self.iterations):
            # Forward pass: y = wx + b
            linear_model = (X * self.weight) + self.bias
            y_predicted = self._sigmoid(linear_model)

            # Gradient calculation (partial derivatives)
            # (used to know which direction I'm moving
            # on the Loss curve)
            # The Loss function is Binary Cross Entropy
            # (Log Loss function)
            dw = (1 / n_samples) * np.sum(X * (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            # Update parameters
            self.weight -= self.lr * dw
            self.bias -= self.lr * db

    def predict_prob(self, X: np.ndarray) -> np.ndarray:
        """Returns the raw probability scores."""
        linear_model = (X * self.weight) + self.bias
        return self._sigmoid(linear_model)

    def predict(self, X: np.ndarray) -> list[int]:
        """Returns class labels 0 or 1."""
        y_predicted = self.predict_prob(X)
        return [1 if i > 0.5 else 0 for i in y_predicted]



# 1. Train the model (using the same data from before)
X_train = np.array([1, 2, 3, 7, 8, 9])
y_train = np.array([0, 0, 0, 1, 1, 1])
model = LogisticRegression(learning_rate=0.1, iterations=1000)
model.fit(X_train, y_train)

# New test points
X_new = np.array([0.5, 4.0, 6.0, 9.5])
y_new_preds = model.predict(X_new)

# 2. Generate points for a smooth S-curve
# We create 100 points between 0 and 10 to draw the line
X_curve = np.linspace(0, 10, 100)
y_curve = model.predict_prob(X_curve)

# 3. Plotting
plt.figure(figsize=(8, 5))

# Plot the actual data points
plt.scatter(X_train, y_train, color='red', label='Training Data')

# Plot the learned Sigmoid Curve
plt.plot(X_curve, y_curve, color='blue', label='Logistic Regression Curve')

# New points added in blue
plt.scatter(X_new, y_new_preds, color='blue', marker='x', s=100, label='Predicted New Points')

# Add a line at 0.5 to show the decision threshold
plt.axhline(y=0.5, color='gray', linestyle='--', label='0.5 Threshold')

plt.xlabel('X (Feature)')
plt.ylabel('Probability / Class')
plt.title('Logistic Regression Fit')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
