import numpy as np
import matplotlib.pyplot as plt

X = np.array([2, 4, 6, 8, 10], dtype=float)
Y = np.array([5.5, 6.3, 7.2, 8.0, 8.6], dtype=float)
N = len(X)

# МНК
a1 = (N * np.sum(X*Y) - np.sum(X)*np.sum(Y)) / (N * np.sum(X**2) - np.sum(X)**2)
a0 = (np.sum(Y) - a1 * np.sum(X)) / N

print(f"y = {a0:.4f} + {a1:.4f}*x")
print(f"Еталон: y = 4.75 + 0.395*x")

x_line = np.linspace(0, 12, 100)

plt.scatter(X, Y, color="red", label="Експериментальні точки")
plt.plot(x_line, a0 + a1*x_line, label=f"МНК: y={a0:.3f}+{a1:.3f}x")
plt.plot(x_line, 4.75 + 0.395*x_line, linestyle="--", label="Еталон: y=4.75+0.395x")
plt.legend()
plt.grid()
plt.title("Лінійна регресія (МНК)")
plt.show()