import numpy as np
import matplotlib.pyplot as plt

def potential(r, epsilon=1.0, sigma=3.4):
    if r == 0:
        return float('inf')
    ratio = sigma / r
    return 4 * epsilon * (ratio**12 - ratio**6)

def find_root(func, a, b, steps=1000):
    h = (b - a) / steps
    x = a
    while x < b:
        if func(x) * func(x + h) <= 0:
            return x + h / 2
        x += h
    return None

# --- Розрахунок ---
root = find_root(potential, 2.0, 5.0)

print("--- Завдання 2.4: Рівномірний пошук ---")
if root:
    print(f"Точка перетину (U(R)=0): R ≈ {root:.4f}")
    print(f"Аналітичне значення: R = sigma = 3.4000")

# --- Графік ---
r_vals = np.linspace(2.5, 6, 400)
u_vals = potential(r_vals)

plt.figure(figsize=(10, 6))
plt.plot(r_vals, u_vals, label='Потенціал U(R)')
plt.axhline(0, color='red', linestyle='--')

if root:
    plt.plot(root, 0, 'go', markersize=10, label=f'Корінь R ≈ {root:.2f}')

plt.title('Пошук кореня U(R) = 0 методом рівномірного пошуку')
plt.xlabel("Відстань R")
plt.ylabel("Потенціал U")
plt.grid(True)
plt.legend()
plt.ylim(-1.5, 1.5)
plt.show()
