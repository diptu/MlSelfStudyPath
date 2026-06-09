from pathlib import Path
from linear.knn_classifier import KNNClassifier
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    # ============================================================
    # LOAD CIFAR-10
    # ============================================================

    print("Loading CIFAR-10 dataset...")

    # Gets the directory where test.py lives
    BASE_DIR = Path(__file__).resolve().parent
    data_dir = BASE_DIR / "data" / "cifar10" / "train"

    image_paths = []
    labels = []
    path_list = [
        "airplane",
        "automobile",
        "bird",
        "cat",
        "deer",
        "dog",
        "frog",
        "horse",
        "ship",
        "truck",
    ]

    for i, label in enumerate(path_list):
        img_dir = data_dir / label

        # Ensure the directory exists before attempting to list it
        if not img_dir.exists():
            print(f"Warning: Directory not found {img_dir}")
            continue

        for img in os.listdir(img_dir):
            # Exclude hidden files like .DS_Store (common on macOS)
            if img.startswith("."):
                continue

            img_path = img_dir / img
            image_paths.append(str(img_path))
            labels.append(label)

    class_names = sorted(set(labels))

    class_indices = {name: idx for idx, name in enumerate(class_names)}
    label_indices = [class_indices[label] for label in labels]

    df = pd.DataFrame({"img_path": image_paths, "label": labels})
    print(df.head(2))

    for category, group in df.groupby("label"):
        fig, ax = plt.subplots(1, 3, figsize=(8, 8))
        ax = ax.ravel()
        for i, (_, r) in enumerate(group.sample(3).iterrows()):
            img = plt.imread(r.img_path)
            ax[i].imshow(img)
            ax[i].axis("off")
            ax[i].set_title(r.label)
        plt.show()

    train_ratio = 0.80
    test_ratio = 0.10
    val_ratio = 0.10

    df_train, df_test_val = train_test_split(
        df, train_size=train_ratio, random_state=42
    )
    df_test, df_val = train_test_split(
        df_test_val, train_size=test_ratio / (test_ratio + val_ratio), random_state=42
    )

    # Flatten labels
    y_train = y_train.flatten()
    y_test = y_test.flatten()

    # ============================================================
# PREPROCESSING
# ============================================================

# Normalize pixel values
X_train = X_train.astype(np.float32) / 255.0
X_test = X_test.astype(np.float32) / 255.0

# Flatten images:
# (32, 32, 3) -> (3072,)
X_train = X_train.reshape(X_train.shape[0], -1)
X_test = X_test.reshape(X_test.shape[0], -1)

print(f"Train shape: {X_train.shape}")
print(f"Test shape : {X_test.shape}")

# ============================================================
# SUBSET FOR SPEED
# ============================================================

# KNN is VERY slow on full CIFAR-10.
# Use smaller subsets for demonstration.

train_samples = 5000
test_samples = 1000

X_train_small = X_train[:train_samples]
y_train_small = y_train[:train_samples]

X_test_small = X_test[:test_samples]
y_test_small = y_test[:test_samples]

# ============================================================
# TRAIN
# ============================================================

print("\nTraining KNN...")

knn = KNNClassifier(k=5)

knn.fit(X_train_small, y_train_small)

# ============================================================
# EVALUATE
# ============================================================

print("\nEvaluating...")

accuracy = knn.score(X_test_small, y_test_small)

print(f"\nAccuracy: {accuracy:.4f}")

# ============================================================
# VISUALIZE PREDICTIONS
# ============================================================

class_names = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
]

predictions = knn.predict(X_test_small[:5])

plt.figure(figsize=(12, 4))

for i in range(5):
    plt.subplot(1, 5, i + 1)

    image = X_test_small[i].reshape(32, 32, 3)

    plt.imshow(image)

    true_label = class_names[y_test_small[i]]
    pred_label = class_names[predictions[i]]

    plt.title(f"P: {pred_label}\nT: {true_label}")

    plt.axis("off")

plt.tight_layout()
plt.show()
