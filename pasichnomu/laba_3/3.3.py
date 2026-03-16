import numpy as np
import matplotlib.pyplot as plt
import random


# 1. Визначення функції та меж
def f(x):
    return 1 / (1 + np.cos(x) ** 2)


a = 0
b = np.pi / 2
N = 1000  # Кількість розбиттів або точок


# 2. Метод трапецій
def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return integral


# 3. Метод Сімпсона
def simpson_rule(f, a, b, n):
    if n % 2 != 0: n += 1
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    integral = (h / 3) * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]))
    return integral


# 4. Метод Монте-Карло
def monte_carlo_integration(f, a, b, n):
    # Знаходимо максимум функції на відрізку для побудови прямокутника R
    x_vals = np.linspace(a, b, 1000)
    y_max = np.max(f(x_vals))

    hits = 0
    for _ in range(n):
        x_rand = random.uniform(a, b)
        y_rand = random.uniform(0, y_max)
        if y_rand <= f(x_rand):
            hits += 1

    # Інтеграл = площа прямокутника * відношення попадань
    area_rect = (b - a) * y_max
    integral = area_rect * (hits / n)
    return integral


# Обчислення
res_trap = trapezoidal_rule(f, a, b, N)
res_simp = simpson_rule(f, a, b, N)
res_monte = monte_carlo_integration(f, a, b, 100000)  # Більше точок для точності


# 5. Вивід результатів
print("Метод", "Результат")
print("-" * 38)
print("Метод трапецій", res_trap)
print("Метод Сімпсона", res_simp)
print("Метод Монте-Карло", res_monte)

# 6. Побудова графіка
x_plt = np.linspace(a, b, 200)
y_plt = f(x_plt)

plt.figure(figsize=(10, 5))
plt.plot(x_plt, y_plt, 'r-', linewidth=2, label='f(x) = 1 / (1 + cos²x)')
plt.fill_between(x_plt, y_plt, color='skyblue', alpha=0.4, label='Площа (інтеграл)')
plt.title('Графік підінтегральної функції')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle='--')
plt.legend()
plt.show()