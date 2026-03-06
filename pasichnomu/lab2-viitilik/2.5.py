import numpy as np
import matplotlib.pyplot as plt

def func(x, e0=2, r=10, i0=1e-8, d=20):
    return e0 - x - r * i0 * np.exp(d * x) - 1

def find_root_dichotomy(f, a, b, eps=1e-4):
    # Перевірка, чи знаки на кінцях відрізка різні
    if f(a) * f(b) >= 0:
        print("Метод дихотомії не може гарантувати результат (знаки однакові).")
        # Інвертуємо функцію, якщо f(a) < 0, як у вашому прикладі
        f_adjusted = lambda x: -f(x)
        if f_adjusted(a) * f_adjusted(b) < 0:
            f = f_adjusted
        else:
            return None, 0

    iters = 0
    while (b - a) > eps:
        iters += 1
        mid = (a + b) / 2
        if f(mid) * f(a) < 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2, iters

# --- Розрахунок ---
root, iterations = find_root_dichotomy(func, 0, 2, eps=0.0001)

print("--- Завдання 2.5: Метод дихотомії ---")
if root:
    print(f"Корінь рівняння: x ≈ {root:.5f}")
    print(f"Кількість ітерацій: {iterations}")

# --- Графік ---
x_vals = np.linspace(0, 2, 400)
y_vals = func(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x) = E0 - x - R*I0*e^(Dx) - 1')
plt.axhline(0, color='red', linestyle='--')

if root:
    plt.plot(root, func(root), 'go', markersize=10, label=f'Корінь x ≈ {root:.3f}')

plt.title('Пошук кореня методом дихотомії')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
