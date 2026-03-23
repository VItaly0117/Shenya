import matplotlib.pyplot as plt
import numpy as np
import random

# Базові параметри
R0 = 5.0
I = np.arange(0, 10.25, 0.25)
p_values = [0.03, 0.15, 0.3]

plt.figure(figsize=(15, 5))

for idx, p in enumerate(p_values):
    # Генеруємо напругу з шумом: U = I * R_noisy
    # R = R0 + p * (2 * random - 1) * R0
    U_noisy = []
    for current in I:
        r_random = R0 + p * (2 * random.random() - 1) * R0
        U_noisy.append(current * r_random)

    U_noisy = np.array(U_noisy)

    # Метод найменших квадратів для апроксимації (шукаємо нахил R_approx)
    # Оскільки лінія має проходити через (0,0), формула спрощується:
    # R_approx = sum(I * U) / sum(I^2)
    R_approx = np.sum(I * U_noisy) / np.sum(I ** 2)

    # Побудова графіка
    plt.subplot(1, 3, idx + 1)
    plt.scatter(I, U_noisy, color='red', s=10, label='Зашумлені дані')
    plt.plot(I, R_approx * I, color='blue', label='Регресія (МНК)')
    plt.plot(I, R0 * I, color='green', linestyle='--', alpha=0.6, label='Ідеальна ВАХ')

    plt.title("Відхилення p = " + str(p))
    plt.xlabel("I, А")
    plt.ylabel("U, В")
    plt.grid(True)
    plt.legend()

    print("При p =", p, "отримано опір R =", round(R_approx, 4), "Ом")

plt.tight_layout()
plt.show()