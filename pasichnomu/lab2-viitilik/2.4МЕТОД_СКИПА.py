import numpy as np
import matplotlib.pyplot as plt

def f_25(x):
    E0, R, I0, D = 2, 10, 10**(-8), 20
    return E0 - x - R * I0 * np.exp(D * x) - 1

def dichotomy_root(f, a, b, e):
    while abs(b - a) > e:
        x = (a + b) / 2
        if f(x) == 0.0:
            return x
        if f(a) * f(x) > 0:
            a = x
        else:
            b = x
    return (a + b) / 2

def F_iter(x):
    return -np.sin(x) - 0.2

def simple_iteration_root(F, x0, E, max_iter=1000):
    xn = x0
    for _ in range(max_iter):
        xn_plus_1 = F(xn)
        if abs(xn_plus_1 - xn) < E:
            return xn_plus_1
        xn = xn_plus_1
    return xn

root_25 = dichotomy_root(f_25, 0, 2, 0.0001)
root_26 = simple_iteration_root(F_iter, 0, 0.0001)

# Графики 2.5 и 2.6
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# 2.5
x_vals_25 = np.linspace(0, 2, 400)
y_vals_25 = f_25(x_vals_25)
ax1.plot(x_vals_25, y_vals_25, label='f(x) (Задание 2.5)', color='green')
ax1.axhline(0, color='black', linewidth=1)
ax1.scatter([root_25], [0], color='red', zorder=5, label=f'Корень: {root_25:.4f}')
ax1.set_title('Задание 2.5: Корень (Дихотомия)')
ax1.grid(True)
ax1.legend()

# 2.6
x_vals_26 = np.linspace(-1, 3, 400)
# Для графика строим f(x) = sin(x) + x + 0.2
y_vals_26 = np.sin(x_vals_26) + x_vals_26 + 0.2
ax2.plot(x_vals_26, y_vals_26, label='f(x) = sin(x) + x + 0.2', color='purple')
ax2.axhline(0, color='black', linewidth=1)
ax2.scatter([root_26], [0], color='red', zorder=5, label=f'Корень: {root_26:.4f}')
ax2.set_title('Задание 2.6: Корень (Простые итерации)')
ax2.grid(True)
ax2.legend()
plt.show()