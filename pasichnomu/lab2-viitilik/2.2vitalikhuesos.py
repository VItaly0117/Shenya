import numpy as np
import matplotlib.pyplot as plt


def f_22(x):
    return ((0.03 * x - 3) * x + 3) * x

def dichotomy_max(f, a, b, E):
    while abs(b - a) >= 2 * E:
        x1 = (a + b - E) / 2
        x2 = (a + b + E) / 2
        if f(x1) > f(x2):
            b = x2
        else:
            a = x1
    x_max = (a + b) / 2
    return x_max, f(x_max)

x_max, f_max = dichotomy_max(f_22, -10, 10, 0.001)

x_vals_22 = np.linspace(-10, 10, 400)
y_vals_22 = f_22(x_vals_22)

plt.figure(figsize=(8, 5))
plt.plot(x_vals_22, y_vals_22, label='f(x) = ((0.03*x - 3)*x + 3)*x', color='black')
plt.scatter([x_max], [f_max], color='red', zorder=5, label=f'Max: x={x_max:.3f}, y={f_max:.3f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()