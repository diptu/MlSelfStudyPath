# ! pip3 install scikit-learn
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class LinearRegression:
    """
    Linear Regression using Batch Gradient Descent.
    """

    def __init__(
        self,
        learning_rate: float = 0.01,
        epochs: int = 1000,
    ) -> None:
        self.learning_rate = learning_rate
        self.epochs = epochs

        # Parameters
        self.weight: np.ndarray | None = None
        self.bias: float = 0.0

        # Store training loss
        self.loss_history: list[float] = []

    def fit(
        self,
        x: np.ndarray,
        y: np.ndarray,
    ) -> None:
        """
        Train model using Batch Gradient Descent.
        """

        # Number of samples and features
        n_samples, n_features = x.shape

        # Initialize parameters
        self.weight = np.zeros(n_features)
        self.bias = 0.0

        # Gradient Descent Loop
        for epoch in range(self.epochs):
            # Forward Pass
            predictions = self.predict(x)

            # Compute Loss
            loss = np.mean((predictions - y) ** 2)

            self.loss_history.append(loss)

            # Compute Gradients
            dw = (2 / n_samples) * np.dot(
                x.T,
                (predictions - y),
            )

            db = (2 / n_samples) * np.sum(predictions - y)

            # Update Parameters
            self.weight -= self.learning_rate * dw

            self.bias -= self.learning_rate * db

            # Print Training Progress
            if epoch % 100 == 0:
                print(f"Epoch {epoch:4d} | Loss: {loss:.6f}")

    def predict(
        self,
        x: np.ndarray,
    ) -> np.ndarray:
        """
        Predict target values.
        """

        if self.weight is None:
            raise ValueError("Model not trained yet.")

        return (
            np.dot(
                x,
                self.weight,
            )
            + self.bias
        )

    def score(
        self,
        x: np.ndarray,
        y: np.ndarray,
    ) -> float:
        """
        Compute R² score.
        """

        predictions = self.predict(x)

        ss_total = np.sum((y - np.mean(y)) ** 2)

        ss_residual = np.sum((y - predictions) ** 2)

        return 1 - (ss_residual / ss_total)


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
    model = LinearRegression(
        learning_rate=0.01,
        epochs=1000,
    )

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
