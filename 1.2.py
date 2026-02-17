import numpy as np
import matplotlib.pyplot as plt


h = 6.626e-34       # стала Планка, Дж·с
c = 3e8              # швидкість світла, м/с
k = 1.38e-23         # стала Больцмана, Дж/К
pi = 3.14159         # число пі

def planck(lam, T):
    lam_m = lam * 1e-6

    # Чисельник і знаменник формули Планка
    nume = 2 * pi * c**2 * h
    deno = lam_m**5 * (np.exp((h * c) / (lam_m * k * T)) - 1)
    return nume / deno
# --- Діапазон довжин хвиль: 0.38 – 5.0 мкм (500 точок) ---
lam = np.linspace(0.38, 5.0, 500)

# --- Температури для порівняння ---
T1 = 1000  # К
T2 = 2000  # К

# Розрахунок спектральної густини для кожної температури
spec1 = planck(lam, T1)
spec2 = planck(lam, T2)
# --- Побудова графіка ---
plt.figure(figsize=(10, 6))
plt.plot(lam, spec1, label='T = 1000 K')
plt.plot(lam, spec2, label='T = 2000 K')
# Виділення видимого діапазону (жовтий) та ІЧ-діапазону (червоний)
plt.axvspan(0.38, 0.78, color='yellow', alpha=0.3, label='Видиме (0.38–0.78 $\\mu$m)')
plt.axvspan(0.78, 5.0, color='red', alpha=0.1, label='ІЧ (>0.78 $\\mu$m)')
plt.title("Закон Планка: спектральна густина випромінювання")
plt.xlabel("Довжина хвилі ($\\mu$m)")
plt.ylabel("Спектральна густина ($W/m^3$)")
plt.legend()
plt.grid(True)
plt.show()