from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from LogisticRegression import LogisticRegression

if __name__ == "__main__":
    # Create synthetic dataset
    X, y = make_classification(
        n_samples=500,
        n_features=2,
        n_redundant=0,
        n_informative=2,
        n_clusters_per_class=1,
        random_state=42,
    )

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    # Train model
    model = LogisticRegression(
        learning_rate=0.1,
        epochs=2000,
    )

    model.fit(
        X_train,
        y_train,
    )

    # Accuracy
    accuracy = model.accuracy(
        X_test,
        y_test,
    )

    print(f"Accuracy: {accuracy:.4f}")

    # Confusion Matrix
    cm = model.confusion_matrix(
        X_test,
        y_test,
    )

    print("\nConfusion Matrix:")
    print(cm)

    # Classification Metrics
    report = model.classification_report(
        X_test,
        y_test,
    )

    print("\nClassification Report:")

    for metric, value in report.items():
        print(f"{metric:<10}: {value:.4f}")

    # Plot Loss Curve
    model.plot_loss()

    # Plot Decision Boundary
    model.plot_decision_boundary(
        X_test,
        y_test,
    )
