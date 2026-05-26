"""
Multiple Linear Regression using the Normal Equation
---------------------------------------------------

This implementation trains a Linear Regression model
using the closed-form Normal Equation instead of
Batch Gradient Descent.

Formula
-------
θ = (XᵀX)⁻¹Xᵀy

Author: Nazmul Alam Diptu
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class LinearRegressionNormalEquation:
    """
    Multiple Linear Regression using the Normal Equation.
    """

    def __init__(self) -> None:
        """
        Initialize model parameters.
        """

        self.weight: np.ndarray | None = None
        self.bias: float = 0.0

    def fit(
        self,
        x: np.ndarray,
        y: np.ndarray,
    ) -> None:
        """
        Train model using the Normal Equation.

        Parameters
        ----------
        x : np.ndarray
            Feature matrix of shape (n_samples, n_features)

        y : np.ndarray
            Target vector of shape (n_samples,)
        """

        # Add bias column (intercept term)
        x_bias = np.c_[
            np.ones(x.shape[0]),
            x,
        ]

        # Compute parameters using Normal Equation
        theta = np.linalg.pinv(x_bias.T @ x_bias) @ (x_bias.T @ y)

        # Separate bias and weights
        self.bias = float(theta[0])
        self.weight = theta[1:]

    def predict(
        self,
        x: np.ndarray,
    ) -> np.ndarray:
        """
        Predict target values.

        Parameters
        ----------
        x : np.ndarray
            Feature matrix

        Returns
        -------
        np.ndarray
            Predicted values
        """

        if self.weight is None:
            raise ValueError("Model not trained yet.")

        return (x @ self.weight) + self.bias

    def score(
        self,
        x: np.ndarray,
        y: np.ndarray,
    ) -> float:
        """
        Compute R² score.

        Parameters
        ----------
        x : np.ndarray
            Feature matrix

        y : np.ndarray
            Actual target values

        Returns
        -------
        float
            R² score
        """

        predictions = self.predict(x)

        ss_total = np.sum((y - np.mean(y)) ** 2)

        ss_residual = np.sum((y - predictions) ** 2)

        return 1 - (ss_residual / ss_total)


# Example Usage

if __name__ == "__main__":
    # -----------------------------------
    # Load Dataset
    # -----------------------------------
    df = pd.read_csv("./data/housing.csv")

    print("\nDataset Preview")
    print("----------------")
    print(df.head())

    # -----------------------------------
    # Features and Target
    # -----------------------------------
    X = df.drop(columns=["price"]).values.astype(np.float64)

    y = df["price"].values.astype(np.float64)

    # -----------------------------------
    # Train/Test Split
    # -----------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.33,
        random_state=42,
    )

    print("\nDataset Shapes")
    print("----------------")
    print(f"X_train: {X_train.shape}")
    print(f"X_test : {X_test.shape}")
    print(f"y_train: {y_train.shape}")
    print(f"y_test : {y_test.shape}")

    # -----------------------------------
    # Feature Scaling
    # -----------------------------------
    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)

    X_test = scaler.transform(X_test)

    # -----------------------------------
    # Initialize Model
    # -----------------------------------
    model = LinearRegressionNormalEquation()

    # -----------------------------------
    # Train Model
    # -----------------------------------
    model.fit(
        X_train,
        y_train,
    )

    # -----------------------------------
    # Predictions
    # -----------------------------------
    predictions = model.predict(X_test)

    # -----------------------------------
    # Final Parameters
    # -----------------------------------
    print("\nFinal Parameters")
    print("----------------")
    print(f"Weights: {model.weight}")
    print(f"Bias: {model.bias:.4f}")

    # -----------------------------------
    # Sample Predictions
    # -----------------------------------
    print("\nSample Predictions")
    print("------------------")

    for actual, predicted in zip(
        y_test[:5],
        predictions[:5],
    ):
        print(f"Actual: {actual:.2f} | Predicted: {predicted:.2f}")

    # -----------------------------------
    # Model Evaluation
    # -----------------------------------
    print("\nTrain R² Score")
    print("----------------")
    print(
        f"There is {100 * model.score(X_train, y_train):.4f}  % less variation around the line then the mean"
    )

    print("\nTest R² Score")
    print("----------------")
    print(
        f"There is {100 * model.score(X_test, y_test):.4f}  % less variation around the line then the mean"
    )
