"""
Logistic Regression using Batch Gradient Descent
------------------------------------------------

Binary Logistic Regression implemented from scratch using NumPy.

Features
--------
✓ Binary Cross Entropy Loss
✓ Batch Gradient Descent
✓ Accuracy Score
✓ Confusion Matrix
✓ Precision
✓ Recall
✓ F1 Score
✓ Decision Boundary Plot
✓ Loss Curve Plot

Author: Nazmul Alam Diptu
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt


class LogisticRegression:
    """
    Binary Logistic Regression using Batch Gradient Descent.
    """

    def __init__(
        self,
        learning_rate: float = 0.01,
        epochs: int = 1000,
    ) -> None:
        self.learning_rate = learning_rate
        self.epochs = epochs

        self.weight: np.ndarray | None = None
        self.bias: float = 0.0

        self.loss_history: list[float] = []

    @staticmethod
    def _sigmoid(z: np.ndarray) -> np.ndarray:
        z = np.clip(z, -500, 500)
        return 1.0 / (1.0 + np.exp(-z))

    @staticmethod
    def _binary_cross_entropy(
        y_true: np.ndarray,
        y_pred: np.ndarray,
    ) -> float:
        epsilon = 1e-15

        y_pred = np.clip(
            y_pred,
            epsilon,
            1 - epsilon,
        )

        loss = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

        return float(loss)

    def fit(
        self,
        x: np.ndarray,
        y: np.ndarray,
    ) -> "LogisticRegression":
        x = np.asarray(x, dtype=np.float64)
        y = np.asarray(y, dtype=np.float64)

        if x.ndim == 1:
            x = x.reshape(-1, 1)

        n_samples, n_features = x.shape

        self.weight = np.zeros(n_features)
        self.bias = 0.0

        self.loss_history.clear()

        for _ in range(self.epochs):
            z = np.dot(x, self.weight) + self.bias

            y_pred = self._sigmoid(z)

            loss = self._binary_cross_entropy(
                y_true=y,
                y_pred=y_pred,
            )

            self.loss_history.append(loss)

            dw = (1 / n_samples) * np.dot(
                x.T,
                (y_pred - y),
            )

            db = (1 / n_samples) * np.sum(
                y_pred - y,
            )

            self.weight -= self.learning_rate * dw

            self.bias -= self.learning_rate * db

        return self

    def predict_proba(
        self,
        x: np.ndarray,
    ) -> np.ndarray:
        if self.weight is None:
            raise ValueError("Model must be fitted before prediction.")

        x = np.asarray(
            x,
            dtype=np.float64,
        )

        if x.ndim == 1:
            x = x.reshape(-1, 1)

        z = (
            np.dot(
                x,
                self.weight,
            )
            + self.bias
        )

        return self._sigmoid(z)

    def predict(
        self,
        x: np.ndarray,
        threshold: float = 0.5,
    ) -> np.ndarray:
        probabilities = self.predict_proba(x)

        return (probabilities >= threshold).astype(int)

    def accuracy(
        self,
        x: np.ndarray,
        y: np.ndarray,
    ) -> float:
        predictions = self.predict(x)

        return float(np.mean(predictions == y))

    def score(
        self,
        x: np.ndarray,
        y: np.ndarray,
    ) -> float:
        return self.accuracy(x, y)

    def confusion_matrix(
        self,
        x: np.ndarray,
        y: np.ndarray,
    ) -> np.ndarray:
        y_pred = self.predict(x)

        tp = np.sum((y == 1) & (y_pred == 1))

        tn = np.sum((y == 0) & (y_pred == 0))

        fp = np.sum((y == 0) & (y_pred == 1))

        fn = np.sum((y == 1) & (y_pred == 0))

        return np.array(
            [
                [tn, fp],
                [fn, tp],
            ]
        )

    def classification_report(
        self,
        x: np.ndarray,
        y: np.ndarray,
    ) -> dict:
        cm = self.confusion_matrix(x, y)

        tn, fp = cm[0]
        fn, tp = cm[1]

        precision = tp / (tp + fp + 1e-15)

        recall = tp / (tp + fn + 1e-15)

        f1 = 2 * precision * recall / (precision + recall + 1e-15)

        accuracy = (tp + tn) / np.sum(cm)

        return {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1,
        }

    def plot_loss(self) -> None:
        plt.figure(figsize=(8, 5))

        plt.plot(
            self.loss_history,
            linewidth=2,
        )

        plt.title("Training Loss")

        plt.xlabel("Epoch")

        plt.ylabel(
            """Binary Cross Entropy
            The Binary Cross-Entropy formula calculates `log(y_pred)` and `log(1 - y_pred)`. 
            If your model predicts an exact `0.0` or `1.0`, NumPy evaluates `log(0)`, which equals `-inf`. 
            Multiplying `-inf` by `0` yields `nan`, which corrupts your gradients and breaks training.
            
            ### The Fix
            Applying `np.clip(y_pred, {epsilon_val}, {1 - epsilon_val})` bounds your predictions 
            to a safe interval:
            * `0.0` becomes `{epsilon_val}` -> `log({epsilon_val})` evaluates safely to ~-34.54
            * `1.0` becomes `{1 - epsilon_val}`
            
            This keeps the math stable, the loss scalar clean, and the gradients valid.
            """
        )

        plt.grid(True)

        plt.show()

    def plot_decision_boundary(
        self,
        x: np.ndarray,
        y: np.ndarray,
    ) -> None:
        if x.shape[1] != 2:
            raise ValueError(
                "Decision boundary visualization requires exactly 2 features."
            )

        x_min, x_max = (
            x[:, 0].min() - 1,
            x[:, 0].max() + 1,
        )

        y_min, y_max = (
            x[:, 1].min() - 1,
            x[:, 1].max() + 1,
        )

        xx, yy = np.meshgrid(
            np.arange(
                x_min,
                x_max,
                0.05,
            ),
            np.arange(
                y_min,
                y_max,
                0.05,
            ),
        )

        grid = np.c_[
            xx.ravel(),
            yy.ravel(),
        ]

        predictions = self.predict(grid).reshape(xx.shape)

        plt.figure(figsize=(8, 6))

        plt.contourf(
            xx,
            yy,
            predictions,
            alpha=0.3,
        )

        plt.scatter(
            x[:, 0],
            x[:, 1],
            c=y,
            edgecolors="k",
        )

        plt.title("Decision Boundary")

        plt.xlabel("Feature 1")

        plt.ylabel("Feature 2")

        plt.show()
