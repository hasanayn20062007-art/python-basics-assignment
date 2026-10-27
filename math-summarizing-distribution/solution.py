
import numpy as np

def skewness(x):
    x = np.array(x, dtype=float)

    mean = np.mean(x)
    std = np.std(x)

    if std == 0:
        return 0.0

    z_scores = (x - mean) / std
    return float(np.mean(z_scores ** 3))


def summarize_distribution(x):
    return {
        "mean": float(np.mean(x)),
        "median": float(np.median(x)),
        "std": float(np.std(x)),
        "skew": skewness(x)
    }
