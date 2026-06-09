"""
K-Nearest Neighbors (KNN) Classifier From Scratch
-------------------------------------------------

This implementation trains a KNN classifier on the CIFAR-10 dataset
without using scikit-learn's KNeighborsClassifier.

Features
--------
- Pure NumPy implementation
- Supports:
    * Euclidean distance
    * Batch prediction
    * Accuracy evaluation
- Uses raw CIFAR-10 image pixels

Dataset
-------
CIFAR-10:
- 60,000 color images
- 10 classes
- Image size: 32x32x3

Author: Nazmul Alam Diptu
"""

from __future__ import annotations

from collections import Counter
from typing import Literal

import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.datasets import cifar10


# ============================================================
# KNN CLASSIFIER
# ============================================================


class KNNClassifier:
    """
    K-Nearest Neighbors classifier from scratch.
    """

    def __init__(
        self,
        k: int = 3,
        distance_metric: Literal["euclidean"] = "euclidean",
    ) -> None:
        """
        Initialize KNN classifier.

        Parameters
        ----------
        k : int
            Number of nearest neighbors.

        distance_metric : str
            Distance metric to use.
        """

        self.k = k
        self.distance_metric = distance_metric

        self.X_train: np.ndarray | None = None
        self.y_train: np.ndarray | None = None

    # ========================================================
    # FIT
    # ========================================================

    def fit(
        self,
        X: np.ndarray,
        y: np.ndarray,
    ) -> None:
        """
        Store training data.

        Parameters
        ----------
        X : np.ndarray
            Training features.

        y : np.ndarray
            Training labels.
        """

        self.X_train = X
        self.y_train = y

    # ========================================================
    # DISTANCE
    # ========================================================

    def _euclidean_distance(
        self,
        x1: np.ndarray,
        x2: np.ndarray,
    ) -> float:
        """
        Compute Euclidean distance.
        """

        return np.sqrt(np.sum((x1 - x2) ** 2))

    # ========================================================
    # SINGLE PREDICTION
    # ========================================================

    def _predict_single(
        self,
        x: np.ndarray,
    ) -> int:
        """
        Predict a single sample.
        """

        assert self.X_train is not None
        assert self.y_train is not None

        distances: list[float] = []

        # Compute distance from all training samples
        for train_sample in self.X_train:
            distance = self._euclidean_distance(x, train_sample)
            distances.append(distance)

        distances_array = np.array(distances)

        # Get indices of k nearest neighbors
        k_indices = np.argsort(distances_array)[: self.k]

        # Get labels
        k_nearest_labels = self.y_train[k_indices]

        # Majority voting
        most_common = Counter(k_nearest_labels).most_common(1)

        return int(most_common[0][0])

    # ========================================================
    # PREDICT
    # ========================================================

    def predict(
        self,
        X: np.ndarray,
    ) -> np.ndarray:
        """
        Predict multiple samples.
        """

        predictions = [self._predict_single(x) for x in X]

        return np.array(predictions)

    # ========================================================
    # SCORE
    # ========================================================

    def score(
        self,
        X: np.ndarray,
        y: np.ndarray,
    ) -> float:
        """
        Compute accuracy.
        """

        predictions = self.predict(X)

        accuracy = np.mean(predictions == y)

        return float(accuracy)
