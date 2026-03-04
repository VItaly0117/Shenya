import numpy as np
import matplotlib.pyplot as plt


# Ітераційна функція F(x), де x = F(x)
def F(x):
    return -np.sin(x) - 0.2


# Метод простих ітерацій
def solve_iter(func, x_0, eps=1e-4, max_iter=1000):
    x_n = x_0
    for i in range(max_iter):
        x_n1 = func(x_n)  # x_{n+1} = F(x_n)
        if abs(x_n1 - x_n) < eps:
            return x_n1, i + 1
        x_n = x_n1
    return None, max_iter


# --- Розрахунок ---
root, iters = solve_iter(F, x_0=0, eps=1e-4)

# --- Вивід та графік ---
print("--- Завдання 2.6: Метод простих ітерацій ---")
if root:
    print(f"Корінь: x ≈ {root:.5f} (знайдено за {iters} ітерацій)")

    x_range = np.linspace(-1, 3, 400)
    y_orig = np.sin(x_range) + x_range + 0.2  # f(x)
    y_iter = F(x_range)  # F(x)

    plt.figure(figsize=(10, 7))
    plt.plot(x_range, y_orig, label='f(x) = sin(x) + x + 0.2')
    plt.plot(x_range, x_range, 'k--', label='y = x')
    plt.plot(x_range, y_iter, label='F(x) = -sin(x) - 0.2')
    plt.axhline(0, color='red', linestyle='--')
    plt.plot(root, 0, 'go', markersize=8, label=f'Корінь x ≈ {root:.3f}')

    plt.title("Пошук кореня методом простих ітерацій")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()
else:
    print("Рішення не знайдено за максимальну кількість ітерацій.")