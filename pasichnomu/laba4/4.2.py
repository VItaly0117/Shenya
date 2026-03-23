import matplotlib.pyplot as plt
import numpy as np

# Вхідні дані з таблиці
x = np.array([2, 4, 6, 8, 10], dtype=float)
y = np.array([5.5, 6.3, 7.2, 8, 8.6], dtype=float)
n = len(x)

# Обчислення коефіцієнтів методом найменших квадратів (y = ax + b)
# Формули:
# a = (n*sum(xy) - sum(x)*sum(y)) / (n*sum(x^2) - (sum(x))^2)
# b = (sum(y) - a*sum(x)) / n

sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_xx = np.sum(x * x)

a = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x**2)
b = (sum_y - a * sum_x) / n

# Вивід результатів без f-рядків
print("Отримане рівняння: y =", round(a, 3), "* x +", round(b, 3))
print("Очікуване рівняння з умови: y = 0.395 * x + 4.75")

# Побудова графіка
plt.scatter(x, y, color='red', label='Експериментальні точки') # Точки
y_pred = a * x + b
plt.plot(x, y_pred, label='Лінія регресії') # Лінія

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Лінійна регресія МНК')
plt.legend()
plt.grid(True)
plt.show()