import numpy as np
from collections import Counter

def euclidean_distance(x1: np.ndarray, x2: np.ndarray) -> float:
    return np.sqrt(np.sum((x1 - x2)**2))

def predict_knn(X_train: np.ndarray, y_train: list, x_new: np.ndarray, k: int = 3):
    # 1. Calculate distances between the new point and all training points
    distances = [euclidean_distance(x_new, x_point) for x_point in X_train]
    
    # 2. Get the indices of the k smallest distances
    # argsort returns indices [3, 0, 1...] instead of the distances themselves
    k_indices = np.argsort(distances)[:k]
    
    # 3. Get the labels associated with those indices
    k_nearest_labels = [y_train[i] for i in k_indices]
    
    # 4. Return the most common label (the winner of the vote)
    most_common = Counter(k_nearest_labels).most_common(1)
    return most_common[0][0]

# Test Case 1: Simple 2D Binary Classification
X_train = np.array([[1, 1], [1, 2], [5, 5], [6, 5]])
y_train = [0, 0, 1, 1]  # Classes: 0 (bottom-left) and 1 (top-right)

# This point (1.5, 1.5) is very close to the [1,1] and [1,2] group
x_new = np.array([1.5, 1.5])

result = predict_knn(X_train, y_train, x_new, k=3)
print(f"Test 1 Prediction: {result}") # Expected: 0


# Test Case 2: Multi-class (3 classes)
X_train = np.array([[1, 0], [1, 1], [10, 10], [10, 11], [5, 5], [5, 6]])
y_train = ['A', 'A', 'B', 'B', 'C', 'C']

# This point is right next to the 'C' cluster
x_new = np.array([5.1, 5.1])

result = predict_knn(X_train, y_train, x_new, k=3)
print(f"Test 2 Prediction: {result}") # Expected: 'C'

# Test Case 3: High K value influence
X_train = np.array([
    [1, 1],   # Class 0 (The closest neighbor)
    [5, 5],   # Class 1
    [5, 6],   # Class 1
    [6, 5]    # Class 1
])
y_train = [0, 1, 1, 1]
x_new = np.array([1.1, 1.1])

# With k=1, it should be 0. With k=3, it should be 1.
print(f"K=1 Prediction: {predict_knn(X_train, y_train, x_new, k=1)}") # Expected: 0
print(f"K=3 Prediction: {predict_knn(X_train, y_train, x_new, k=3)}") # Expected: 1

