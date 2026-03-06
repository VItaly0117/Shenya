import matplotlib.pyplot as plt
import numpy as np

# Вихідні дані
v0 = 5      # початкова швидкість, м/с
a = 3       # прискорення, м/с^2
t_max = 10  # загальний час руху, с
t = np.linspace(0, t_max, 100)

# Формули залежностей
v = v0 + a * t          # Швидкість: v(t) = v0 + at
s = v0 * t + (a * t**2) / 2  # Шлях: s(t) = v0t + at^2/2

# Розрахунок кінцевих значень
v_final = v0 + a * t_max
s_final = v0 * t_max + (a * t_max**2) / 2

print("Результати для t = ",t_max," с:")
print("Кінцева швидкість: ",v_final," м/с")
print("Пройдений шлях: ",s_final," м")

# Побудова графіків
plt.figure(figsize=(12, 5))

# Графік швидкості v(t)
plt.subplot(1, 2, 1)
plt.plot(t, v, 'r-', linewidth=2)
plt.title('Залежність швидкості від часу v(t)')
plt.xlabel('Час (t), с')
plt.ylabel('Швидкість (v), м/с')
plt.grid(True)

# Графік шляху s(t)
plt.subplot(1, 2, 2)
plt.plot(t, s, 'b-', linewidth=2)
plt.title('Залежність шляху від часу s(t)')
plt.xlabel('Час (t), с')
plt.ylabel('Шлях (s), м')
plt.grid(True)

plt.tight_layout()
plt.show()