import numpy as np
from collections import Counter
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class Node:
    """A helper class to store tree nodes."""
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature      # Which column we split on
        self.threshold = threshold  # The value we split at
        self.left = left            # The "Yes" subtree
        self.right = right          # The "No" subtree
        self.value = value          # If it's a leaf node, what's the class?

    def is_leaf(self):
        return self.value is not None

class DecisionTree:
    def __init__(self, max_depth=10, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None

    def fit(self, X, y):
        # Start the recursion!
        self.root = self._grow_tree(X, y)

    def _grow_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))

        # --- 1. BASE CASES ---
        # Stop if: only one label left, max depth reached, or not enough samples
        if (depth >= self.max_depth or n_labels == 1 or n_samples < self.min_samples_split):
            leaf_value = self._most_common_label(y)
            return Node(value=leaf_value)

        # --- 2. THE RECURSIVE STEP ---
        # Find the best feature and threshold to split on
        best_feat, best_thresh = self._best_criteria(X, y, n_features)

        # Split the data into two halves
        left_idxs, right_idxs = self._split(X[:, best_feat], best_thresh)
        
        # Recurse! Call _grow_tree for the left and right branches
        left = self._grow_tree(X[left_idxs, :], y[left_idxs], depth + 1)
        right = self._grow_tree(X[right_idxs, :], y[right_idxs], depth + 1)
        
        return Node(best_feat, best_thresh, left, right)

    def _best_criteria(self, X, y, n_features):
        best_gain = -1
        split_idx, split_thresh = None, None

        for feat_idx in range(n_features):
            X_column = X[:, feat_idx]
            thresholds = np.unique(X_column)
            for threshold in thresholds:
                gain = self._information_gain(y, X_column, threshold)
                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat_idx
                    split_thresh = threshold
        return split_idx, split_thresh

    def _entropy(self, y):
        # Formula: -sum(p(x) * log2(p(x)))
        hist = np.bincount(y)
        ps = hist / len(y)
        return -np.sum([p * np.log2(p) for p in ps if p > 0])

    def _information_gain(self, y, X_column, split_thresh):
        # 1. Parent entropy
        parent_entropy = self._entropy(y)

        # 2. Generate split
        left_idxs, right_idxs = self._split(X_column, split_thresh)
        if len(left_idxs) == 0 or len(right_idxs) == 0:
            return 0

        # 3. Weighted avg entropy of children
        n = len(y)
        n_l, n_r = len(left_idxs), len(right_idxs)
        e_l, e_r = self._entropy(y[left_idxs]), self._entropy(y[right_idxs])
        child_entropy = (n_l / n) * e_l + (n_r / n) * e_r

        # 4. IG = Information Gain
        return parent_entropy - child_entropy

    def _split(self, X_column, split_thresh):
        left_idxs = np.argwhere(X_column <= split_thresh).flatten()
        right_idxs = np.argwhere(X_column > split_thresh).flatten()
        return left_idxs, right_idxs

    def _most_common_label(self, y):
        counter = Counter(y)
        return counter.most_common(1)[0][0]

    def predict(self, X):
        return np.array([self._traverse_tree(x, self.root) for x in X])

    def _traverse_tree(self, x, node):
        # Recursive function to navigate down the tree for prediction
        if node.is_leaf():
            return node.value

        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)

# 1. Load the data
data = load_iris()
X = data.data
y = data.target

# 2. Split into Training and Testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Initialize our custom Decision Tree
# We'll set a max_depth of 5 to prevent overfitting
clf = DecisionTree(max_depth=5)

# 4. Train the model (This triggers the recursive _grow_tree calls)
clf.fit(X_train, y_train)

# 5. Make predictions (This triggers the recursive _traverse_tree calls)
predictions = clf.predict(X_test)

# 6. Evaluate the performance
acc = accuracy_score(y_test, predictions)

print(f"Custom Decision Tree Accuracy: {acc * 100:.2f}%")
print("Predictions:", predictions)
print("Actual Labels:", y_test)