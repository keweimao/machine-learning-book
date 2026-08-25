"""Train the book's matched MNIST models and regenerate CNN practicum assets.

Run from the repository root with:

    .venv/bin/python scripts/generate_cnn_practicum_assets.py

The script uses the same split, optimizer, batch size, stopping rule, and roughly
matched parameter budget for the MLP and CNN. Published figures are written to
``assets/figures/chapter09a/practicum``; models stay under ignored ``tmp``.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import keras
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from keras import layers


ROOT = Path(__file__).resolve().parents[1]
FIGURE_DIR = ROOT / "assets" / "figures" / "chapter09a" / "practicum"
MODEL_DIR = ROOT / "tmp" / "cnn_practicum"
FIGURE_DIR.mkdir(parents=True, exist_ok=True)
MODEL_DIR.mkdir(parents=True, exist_ok=True)

SEED = 42
BATCH_SIZE = 128
MAX_EPOCHS = 12
keras.utils.set_random_seed(SEED)
try:
    tf.config.experimental.enable_op_determinism()
except Exception:
    pass

plt.rcParams.update(
    {
        "figure.dpi": 140,
        "savefig.dpi": 220,
        "font.size": 10,
        "axes.titlesize": 11,
        "axes.labelsize": 10,
    }
)


def save_figure(fig: plt.Figure, name: str) -> None:
    fig.savefig(FIGURE_DIR / name, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def load_data():
    """Return one fixed fit/validation/test split in vector and image forms."""
    (x_train_raw, y_train_raw), (x_test_raw, y_test) = (
        keras.datasets.mnist.load_data()
    )
    order = np.random.default_rng(SEED).permutation(len(x_train_raw))
    x_train_raw, y_train_raw = x_train_raw[order], y_train_raw[order]
    x_fit_raw, x_val_raw = x_train_raw[:54000], x_train_raw[54000:]
    y_fit, y_val = y_train_raw[:54000], y_train_raw[54000:]

    scale = lambda x: x.astype("float32") / 255.0
    x_fit_image = scale(x_fit_raw)[..., np.newaxis]
    x_val_image = scale(x_val_raw)[..., np.newaxis]
    x_test_image = scale(x_test_raw)[..., np.newaxis]
    x_fit_vector = x_fit_image.reshape(-1, 784)
    x_val_vector = x_val_image.reshape(-1, 784)
    x_test_vector = x_test_image.reshape(-1, 784)
    return {
        "x_fit_raw": x_fit_raw,
        "x_val_raw": x_val_raw,
        "x_test_raw": x_test_raw,
        "y_fit": y_fit,
        "y_val": y_val,
        "y_test": y_test,
        "x_fit_image": x_fit_image,
        "x_val_image": x_val_image,
        "x_test_image": x_test_image,
        "x_fit_vector": x_fit_vector,
        "x_val_vector": x_val_vector,
        "x_test_vector": x_test_vector,
    }


def build_mlp() -> keras.Model:
    keras.utils.set_random_seed(SEED)
    model = keras.Sequential(
        [
            keras.Input(shape=(784,)),
            layers.Dense(128, activation="relu"),
            layers.Dense(64, activation="relu"),
            layers.Dense(10, activation="softmax"),
        ],
        name="mnist_mlp",
    )
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    assert model.count_params() == 109386
    return model


def build_cnn() -> keras.Model:
    keras.utils.set_random_seed(SEED)
    model = keras.Sequential(
        [
            keras.Input(shape=(28, 28, 1)),
            layers.Conv2D(16, 3, padding="same", activation="relu", name="conv_1"),
            layers.MaxPooling2D(2, name="pool_1"),
            layers.Conv2D(32, 3, padding="same", activation="relu", name="conv_2"),
            layers.MaxPooling2D(2, name="pool_2"),
            layers.Flatten(),
            layers.Dense(64, activation="relu"),
            layers.Dense(10, activation="softmax"),
        ],
        name="mnist_cnn",
    )
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    assert model.count_params() == 105866
    return model


def train(model, x_fit, y_fit, x_val, y_val):
    callback = keras.callbacks.EarlyStopping(
        monitor="val_loss", patience=2, restore_best_weights=True
    )
    start = time.perf_counter()
    history = model.fit(
        x_fit,
        y_fit,
        validation_data=(x_val, y_val),
        batch_size=BATCH_SIZE,
        epochs=MAX_EPOCHS,
        callbacks=[callback],
        verbose=2,
    )
    return history.history, time.perf_counter() - start


def cross_correlate2d(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """Valid two-dimensional cross-correlation, written for transparency."""
    kh, kw = kernel.shape
    out = np.empty((image.shape[0] - kh + 1, image.shape[1] - kw + 1))
    for row in range(out.shape[0]):
        for col in range(out.shape[1]):
            patch = image[row : row + kh, col : col + kw]
            out[row, col] = np.sum(patch * kernel)
    return np.maximum(out, 0.0)


def plot_examples(data) -> None:
    fig, axes = plt.subplots(2, 5, figsize=(8.4, 3.5))
    for digit, ax in enumerate(axes.flat):
        index = np.flatnonzero(data["y_fit"] == digit)[0]
        ax.imshow(data["x_fit_raw"][index], cmap="gray")
        ax.set_title(f"label {digit}")
        ax.axis("off")
    fig.suptitle("MNIST examples: same size, different local strokes", y=1.01)
    fig.tight_layout()
    save_figure(fig, "mnist-examples.png")


def plot_flattening(data) -> None:
    index = np.flatnonzero(data["y_test"] == 7)[0]
    image = data["x_test_raw"][index] / 255.0
    vector = image.reshape(-1)
    fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.2), gridspec_kw={"width_ratios": [1, 2.2]})
    axes[0].imshow(image, cmap="gray")
    axes[0].set_title("Grid input: 28 x 28")
    axes[0].axis("off")
    axes[1].plot(vector, color="#355C7D", linewidth=1)
    axes[1].set(title="Same 784 values after flattening", xlabel="vector position", ylabel="pixel intensity")
    axes[1].set_xlim(0, 783)
    fig.suptitle("Flattening preserves values but hides two-dimensional adjacency")
    fig.tight_layout()
    save_figure(fig, "flatten-grid-versus-vector.png")


def plot_hand_designed_kernels(data) -> None:
    kernels = {
        "vertical stroke": np.array([[-1, 2, -1], [-1, 2, -1], [-1, 2, -1]], dtype=float),
        "horizontal stroke": np.array([[-1, -1, -1], [2, 2, 2], [-1, -1, -1]], dtype=float),
        "rising diagonal": np.array([[-1, -1, 2], [-1, 2, -1], [2, -1, -1]], dtype=float),
    }
    indices = [np.flatnonzero(data["y_test"] == digit)[0] for digit in (1, 7)]
    fig, axes = plt.subplots(2, 4, figsize=(10.2, 5.1))
    for row, (digit, index) in enumerate(zip((1, 7), indices)):
        image = data["x_test_image"][index, :, :, 0]
        axes[row, 0].imshow(image, cmap="gray")
        axes[row, 0].set_ylabel(f"digit {digit}", fontweight="bold")
        axes[row, 0].set_title("input" if row == 0 else "")
        axes[row, 0].axis("off")
        for col, (name, kernel) in enumerate(kernels.items(), start=1):
            response = cross_correlate2d(image, kernel)
            axes[row, col].imshow(response, cmap="magma", vmin=0)
            axes[row, col].set_title(name if row == 0 else "")
            axes[row, col].axis("off")
    fig.suptitle("Hand-designed kernels light up matching local strokes", y=1.01)
    fig.tight_layout()
    save_figure(fig, "hand-kernel-activations-1-7.png")


def plot_learning_curves(histories) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(9.2, 6.2), sharex="col")
    colors = {"train": "#355C7D", "validation": "#C44E52"}
    for col, name in enumerate(("MLP", "CNN")):
        history = histories[name]
        epochs = np.arange(1, len(history["loss"]) + 1)
        axes[0, col].plot(epochs, history["loss"], marker="o", color=colors["train"], label="training")
        axes[0, col].plot(epochs, history["val_loss"], marker="o", color=colors["validation"], label="validation")
        best = int(np.argmin(history["val_loss"]))
        axes[0, col].axvline(best + 1, color="0.45", linestyle="--", linewidth=1)
        axes[0, col].annotate(
            "lowest validation loss",
            (best + 1, history["val_loss"][best]),
            xytext=(-5, 10),
            textcoords="offset points",
            ha="right",
            fontsize=8,
        )
        axes[0, col].set(title=f"{name}: cross-entropy loss", ylabel="loss")
        axes[1, col].plot(epochs, history["accuracy"], marker="o", color=colors["train"], label="training")
        axes[1, col].plot(epochs, history["val_accuracy"], marker="o", color=colors["validation"], label="validation")
        axes[1, col].set(title=f"{name}: accuracy", xlabel="epoch", ylabel="accuracy")
        axes[0, col].legend(frameon=False)
        axes[1, col].legend(frameon=False)
    fig.suptitle("Training and validation tell different stories", y=1.01)
    fig.tight_layout()
    save_figure(fig, "mlp-cnn-learning-curves.png")


def plot_result_comparison(results) -> None:
    names = ["MLP", "CNN"]
    accuracy = [100 * results[name]["test_accuracy"] for name in names]
    errors = [results[name]["test_errors"] for name in names]
    params = [results[name]["parameters"] for name in names]
    fig, axes = plt.subplots(1, 3, figsize=(9.3, 3.0))
    palette = ["#6C8EBF", "#70AD47"]
    bars = axes[0].bar(names, accuracy, color=palette)
    axes[0].set(title="Test accuracy", ylabel="percent", ylim=(95, 100))
    axes[0].bar_label(bars, fmt="%.2f%%", padding=3)
    bars = axes[1].bar(names, errors, color=palette)
    axes[1].set(title="Misclassified test images", ylabel="count")
    axes[1].bar_label(bars, padding=3)
    bars = axes[2].bar(names, params, color=palette)
    axes[2].set(title="Trainable parameters", ylabel="count")
    axes[2].bar_label(bars, labels=[f"{p:,}" for p in params], padding=3)
    fig.suptitle("Matched parameter budgets, different spatial assumptions", y=1.04)
    fig.tight_layout()
    save_figure(fig, "mlp-cnn-results.png")


def plot_learned_kernels_and_maps(cnn_model, data) -> dict:
    probe = keras.Model(cnn_model.inputs, cnn_model.get_layer("conv_1").output)
    feature_maps = probe.predict(data["x_test_image"], batch_size=256, verbose=0)
    # Normalize each image's channel means before comparing classes. This keeps a
    # digit with more ink from making every channel look globally stronger.
    channel_means = feature_maps.mean(axis=(1, 2))
    channel_share = channel_means / (channel_means.sum(axis=1, keepdims=True) + 1e-12)
    one_maps = channel_share[data["y_test"] == 1].mean(axis=0)
    seven_maps = channel_share[data["y_test"] == 7].mean(axis=0)
    difference = one_maps - seven_maps
    one_channel = int(np.argmax(difference))
    seven_channel = int(np.argmin(difference))
    channels = [one_channel, seven_channel]

    kernels, _ = cnn_model.get_layer("conv_1").get_weights()
    indices = [np.flatnonzero(data["y_test"] == digit)[0] for digit in (1, 7)]
    fig, axes = plt.subplots(3, 3, figsize=(7.6, 7.0))
    for col, channel in enumerate(channels, start=1):
        limit = np.abs(kernels[:, :, 0, channel]).max()
        axes[0, col].imshow(kernels[:, :, 0, channel], cmap="coolwarm", vmin=-limit, vmax=limit)
        axes[0, col].set_title(f"learned kernel {channel}")
        axes[0, col].axis("off")
    axes[0, 0].text(0.5, 0.5, "weights learned\nfrom labels", ha="center", va="center", fontsize=11)
    axes[0, 0].axis("off")
    for row, (digit, index) in enumerate(zip((1, 7), indices), start=1):
        axes[row, 0].imshow(data["x_test_raw"][index], cmap="gray")
        axes[row, 0].set_ylabel(f"digit {digit}", fontweight="bold")
        axes[row, 0].axis("off")
        for col, channel in enumerate(channels, start=1):
            axes[row, col].imshow(feature_maps[index, :, :, channel], cmap="magma", vmin=0)
            axes[row, col].axis("off")
    fig.suptitle("Learned kernels produce different activation patterns", y=1.01)
    fig.tight_layout()
    save_figure(fig, "learned-kernels-feature-maps-1-7.png")
    return {
        "channel_with_larger_relative_activation_for_1": one_channel,
        "channel_with_larger_relative_activation_for_7": seven_channel,
        "mean_channel_share_difference_1_minus_7": {
            str(one_channel): float(difference[one_channel]),
            str(seven_channel): float(difference[seven_channel]),
        },
    }


def main() -> None:
    data = load_data()
    plot_examples(data)
    plot_flattening(data)
    plot_hand_designed_kernels(data)

    models = {"MLP": build_mlp(), "CNN": build_cnn()}
    inputs = {
        "MLP": (data["x_fit_vector"], data["x_val_vector"], data["x_test_vector"]),
        "CNN": (data["x_fit_image"], data["x_val_image"], data["x_test_image"]),
    }
    histories, results = {}, {}
    for name, model in models.items():
        print(f"\n=== Training {name} ===")
        x_fit, x_val, x_test = inputs[name]
        history, seconds = train(model, x_fit, data["y_fit"], x_val, data["y_val"])
        test_loss, test_accuracy = model.evaluate(x_test, data["y_test"], verbose=0)
        predictions = model.predict(x_test, batch_size=256, verbose=0).argmax(axis=1)
        histories[name] = history
        results[name] = {
            "parameters": model.count_params(),
            "epochs_run": len(history["loss"]),
            "best_epoch": int(np.argmin(history["val_loss"]) + 1),
            "best_validation_loss": float(np.min(history["val_loss"])),
            "test_loss": float(test_loss),
            "test_accuracy": float(test_accuracy),
            "test_errors": int(np.sum(predictions != data["y_test"])),
            "training_seconds": float(seconds),
        }
        model.save(MODEL_DIR / f"{name.lower()}.keras")
        print(results[name])

    plot_learning_curves(histories)
    plot_result_comparison(results)
    activation_summary = plot_learned_kernels_and_maps(models["CNN"], data)

    payload = {
        "protocol": {
            "seed": SEED,
            "fit_examples": 54000,
            "validation_examples": 6000,
            "test_examples": 10000,
            "batch_size": BATCH_SIZE,
            "maximum_epochs": MAX_EPOCHS,
            "optimizer": "Adam(learning_rate=0.001)",
            "early_stopping": "validation loss, patience=2, restore best weights",
            "tensorflow": tf.__version__,
            "keras": keras.__version__,
        },
        "results": results,
        "activation_summary": activation_summary,
        "histories": histories,
    }
    (FIGURE_DIR / "results.json").write_text(json.dumps(payload, indent=2) + "\n")
    print(f"\nWrote practicum assets to {FIGURE_DIR}")


if __name__ == "__main__":
    main()
