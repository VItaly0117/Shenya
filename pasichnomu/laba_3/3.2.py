import numpy as np
import matplotlib.pyplot as plt

# --- Початок фізичних розрахунків (аналогічно попередньому) ---
h = 6.626e-34
c = 3e8
k = 1.38e-23
sigma = 5.67e-8

def planck_law(lam, T):
    exponent = (h * c) / (lam * k * T)
    if exponent > 700: return 0
    return (2 * h * c**2) / (lam**5 * (np.exp(exponent) - 1))

def simpson_integration(f, a, b, n, T):
    if n % 2 != 0: n += 1
    dx = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = np.array([f(val, T) for val in x])
    integral = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2])
    return (dx / 3) * integral

def calculate_efficiency(T):
    visible_power = simpson_integration(planck_law, 400e-9, 700e-9, 1000, T)
    total_power = sigma * T**4
    return (visible_power / total_power) * 100

# --- БЛОК ВИВОДУ БЕЗ f-strings ---

print("{:<18} | {:<10}".format("Температура (К)", "ККД (%)"))
print("-" * 32)

key_temperatures = [1000, 2000, 2500, 3000, 4000, 5778, 6500]

for T in key_temperatures:
    eff = calculate_efficiency(T)
    # Використання .format() замість f-рядка
    print("{:<18} | {:<10.4f}".format(T, eff))

# --- Побудова графіка ---
temps = np.linspace(500, 7000, 200)
effs = [calculate_efficiency(T) for T in temps]

plt.figure(figsize=(10, 6))
plt.plot(temps, effs, color='blue')
plt.title('Залежність ККД від температури')
plt.xlabel('T, K')
plt.ylabel('Efficiency, %')
plt.grid(True)
plt.show()