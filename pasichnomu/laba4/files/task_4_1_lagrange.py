import numpy as np
import matplotlib.pyplot as plt

X = np.array([0, 1, 2, 3, 4], dtype=float)
Y = np.array([1, 2, 3, 4, 5], dtype=float)

def lagrange(X, Y, x):
    n = len(X)
    result = 0
    for i in range(n):
        term = Y[i]
        for j in range(n):
            if j != i:
                term *= (x - X[j]) / (X[i] - X[j])
        result += term
    return result

x_target = 2.5
y_target = lagrange(X, Y, x_target)
print(f"L({x_target}) = {y_target}")

x_plot = np.linspace(0, 4, 100)
y_plot = [lagrange(X, Y, xi) for xi in x_plot]

plt.plot(x_plot, y_plot, label="Поліном Лагранжа")
plt.scatter(X, Y, color="red", label="Вузли")
plt.scatter(x_target, y_target, color="green", marker="*", s=150, label=f"L(2.5)={y_target:.2f}")
plt.legend()
plt.grid()
plt.title("Інтерполяція Лагранжа")
plt.show()