"""ELEC/COMP 576 - Assignment 0, Tasks 3 and 4 (Matplotlib figures)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# ---- Task 3: the exact script given in the assignment ----
plt.figure()
plt.plot([1, 2, 3, 4], [1, 2, 7, 14])
plt.axis([0, 6, 0, 20])
plt.savefig("task3.png", dpi=150, bbox_inches="tight")
plt.close()

# ---- Task 4: a figure of my choice (ReLU activation) ----
x = np.linspace(-5, 5, 200)
relu = np.maximum(0, x)
plt.figure(figsize=(6, 4))
plt.plot(x, relu, lw=2.5, color="#1b4f8a")
plt.axhline(0, color="gray", lw=0.8)
plt.axvline(0, color="gray", lw=0.8)
plt.title("ReLU activation function")
plt.xlabel("x")
plt.ylabel("ReLU(x) = max(0, x)")
plt.grid(True, alpha=0.3)
plt.savefig("task4.png", dpi=150, bbox_inches="tight")
plt.close()
print("saved task3.png, task4.png")
