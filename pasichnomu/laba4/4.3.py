import matplotlib.pyplot as plt
import numpy as np

# Константи за умовою
R = 5  # Опір у Омах
start_I = 0
end_I = 10
step = 0.25

# Створення масиву значень сили струму I від 0 до 10 з кроком 0.25
# Додаємо step до end_I, щоб включити кінцеве значення 10 у графік
currents = np.arange(start_I, end_I + step, step)

# Розрахунок напруги U за законом Ома: U = I * R
voltages = currents * R

# Вивід перших кількох значень для перевірки (без f-рядків)
print("Приклади розрахунків (I -> U):")
for i in range(5):
    print("Струм:", currents[i], "А  => Напруга:", voltages[i], "В")

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(currents, voltages, label="U = I * R (R=5 Ом)", color="blue", linewidth=2)

# Оформлення осей та заголовка
plt.title("Вольт-амперна характеристика опору")
plt.xlabel("Сила струму I (А)")
plt.ylabel("Напруга U (В)")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

# Додамо позначення точок кроку (опціонально)
plt.scatter(currents, voltages, color="red", s=10)

plt.show()