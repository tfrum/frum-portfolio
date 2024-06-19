import numpy as np

class DataGenerator:
    def __init__(self, num_samples, num_features, seed=None):
        self.num_samples = num_samples
        self.num_features = num_features
        if seed is not None:
            np.random.seed(seed)

    def generate(self):
        X = np.random.rand(self.num_samples, self.num_features)
        coef = np.random.rand(self.num_features)
        y = np.dot(X, coef) + np.random.rand(self.num_samples)
        return X, y

class RidgeRegression:
    def __init__(self, alpha):
        self.alpha = alpha

    def fit(self, X, y):
        gram = np.dot(X.T, X)
        gram += self.alpha * np.eye(X.shape[1])
        self.coef_ = np.dot(np.linalg.inv(gram), np.dot(X.T, y))
        return self

    def predict(self, X):
        return np.dot(X, self.coef_)

class Evaluator:
    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred

    def mean_squared_error(self):
        return np.mean((self.y_true - self.y_pred) ** 2)

def run_test(seed):
    data_generator = DataGenerator(100, 5, seed)
    X, y = data_generator.generate()

    ridge_regression = RidgeRegression(0.1)
    ridge_regression.fit(X, y)
    y_pred = ridge_regression.predict(X)

    evaluator = Evaluator(y, y_pred)
    mse = evaluator.mean_squared_error()
    
    return mse

mse_seed_0 = run_test(0)
mse_seed_123 = run_test(123)
mse_seed_42 = run_test(42)

expected_mse_seed_0 = 0.08561243381783225
expected_mse_seed_123 = 0.08084365004470064
expected_mse_seed_42 = 0.1028727681797894

assert np.isclose(mse_seed_0, expected_mse_seed_0, rtol=1e-6), f"Test with seed 0 failed, expected {expected_mse_seed_0} but got {mse_seed_0}"
assert np.isclose(mse_seed_123, expected_mse_seed_123, rtol=1e-6), f"Test with seed 123 failed, expected {expected_mse_seed_123} but got {mse_seed_123}"
assert np.isclose(mse_seed_42, expected_mse_seed_42, rtol=1e-6), f"Test with seed 42 failed, expected {expected_mse_seed_42} but got {mse_seed_42}"