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

# ---- Task 4: a figure of my choice ----
x = np.linspace(0, 4 * np.pi, 500)
plt.figure(figsize=(7, 4))
plt.plot(x, np.sin(x) * np.exp(-0.2 * x), label=r"$\sin(x)\,e^{-0.2x}$", lw=2, color="#1b4f8a")
plt.plot(x, np.cos(x) * np.exp(-0.2 * x), label=r"$\cos(x)\,e^{-0.2x}$", lw=2, color="#e8722a", ls="--")
plt.fill_between(x, np.sin(x) * np.exp(-0.2 * x), alpha=0.15, color="#1b4f8a")
plt.title("Damped sinusoids")
plt.xlabel("x")
plt.ylabel("amplitude")
plt.grid(True, alpha=0.3)
plt.legend()
plt.savefig("task4.png", dpi=150, bbox_inches="tight")
plt.close()
print("saved task3.png, task4.png")
