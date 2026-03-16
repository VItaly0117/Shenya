# ============================================================
# Лабораторна робота №3 — Завдання 3.2
# ККД лампи розжарювання в залежності від температури спіралі
# Метод: СІМПСОНА
# ============================================================

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Фізичні константи ────────────────────────────────────────
h     = 6.626e-34   # стала Планка, Дж·с
c     = 3.0e8       # швидкість світла, м/с
k     = 1.381e-23   # стала Больцмана, Дж/К
sigma = 5.67e-8     # стала Стефана–Больцмана, Вт/(м²·К⁴)

# ── Видимий діапазон ──────────────────────────────────────────
lam_min = 400e-9    # м
lam_max = 700e-9    # м
N       = 1000      # кількість підінтервалів (парне!)


# ── Функція Планка ────────────────────────────────────────────
def planck(lam, T):
    """f(λ,T) = 2πhc² / [λ⁵·(exp(hc/kTλ) − 1)]"""
    exp_arg = np.clip(h * c / (k * T * lam), 0, 700)   # обмежуємо переповнення
    return (2 * np.pi * h * c**2) / (lam**5 * (np.exp(exp_arg) - 1))


# ── Метод Сімпсона ────────────────────────────────────────────
def simpson(f_vals, dx):
    """
    Формула Сімпсона (складена):
        I ≈ (dx/3) · [y₀ + 4y₁ + 2y₂ + 4y₃ + ... + 4y_{n-1} + yₙ]
    N — парне
    """
    n = len(f_vals) - 1
    assert n % 2 == 0, "N має бути парним для методу Сімпсона"
    result = f_vals[0] + f_vals[-1]
    result += 4.0 * np.sum(f_vals[1:-1:2])   # непарні індекси
    result += 2.0 * np.sum(f_vals[2:-2:2])   # парні індекси
    return result * dx / 3.0


# ── Розрахунок ККД для масиву температур ─────────────────────
lambdas = np.linspace(lam_min, lam_max, N + 1)
dx      = (lam_max - lam_min) / N

T_range = np.linspace(800, 10000, 500)
eta     = np.zeros_like(T_range)

for i, T in enumerate(T_range):
    y        = planck(lambdas, T)
    I_vis    = simpson(y, dx)
    I_total  = sigma * T**4           # закон Стефана–Больцмана
    eta[i]   = I_vis / I_total

eta_pct = eta * 100.0   # у відсотках


# ── Характерні точки ──────────────────────────────────────────
T_lamps = {
    "Звичайна лампа\n(2400–2700 К)":  2600,
    "Галогенна лампа\n(≈3000 К)":     3000,
    "Вольфрам, Tmax\n(≈3400 К)":      3400,
    "Сонце\n(5778 К)":                5778,
}

print("=" * 55)
print("  ККД лампи розжарювання  —  метод Сімпсона")
print("=" * 55)
print(f"  {'Джерело':<28} {'T, К':>7}  {'η, %':>7}")
print("-" * 55)
for label, T in T_lamps.items():
    eta_val = np.interp(T, T_range, eta_pct)
    print(f"  {label.replace(chr(10),' '):<28} {T:>7}  {eta_val:>7.2f}")
print("=" * 55)


# ── Графік ────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle("ККД лампи розжарювання у видимому діапазоні 400–700 нм\n"
             "(метод Сімпсона)", fontsize=14, fontweight='bold')

colors_pts = ['#1f77b4', '#ff7f0e', '#d62728', '#2ca02c']

# ── Графік 1: η(T) ────────────────────────────────────────────
ax1 = axes[0]
ax1.plot(T_range, eta_pct, color='crimson', linewidth=2.5, label='η(T)')
ax1.fill_between(T_range, eta_pct, alpha=0.15, color='crimson')

for (label, T), col in zip(T_lamps.items(), colors_pts):
    eta_pt = np.interp(T, T_range, eta_pct)
    ax1.axvline(T, color=col, linestyle='--', alpha=0.6, linewidth=1.4)
    ax1.scatter(T, eta_pt, color=col, zorder=5, s=80)
    ax1.annotate(f'{label}\nη={eta_pt:.1f}%',
                 xy=(T, eta_pt),
                 xytext=(T + 150, eta_pt + 0.8),
                 fontsize=8.5, color=col,
                 arrowprops=dict(arrowstyle='->', color=col, lw=1.2))

ax1.set_xlabel('Температура спіралі T, К', fontsize=12)
ax1.set_ylabel('ККД η, %', fontsize=12)
ax1.set_title('Залежність ККД від температури', fontsize=12)
ax1.set_xlim(800, 10000)
ax1.set_ylim(0, max(eta_pct) * 1.2)
ax1.grid(True, alpha=0.3)


# ── Графік 2: спектри Планка для різних T ────────────────────
ax2 = axes[1]
lam_full_nm = np.linspace(100, 3000, 3000)
lam_full    = lam_full_nm * 1e-9
vis_mask    = (lam_full_nm >= 400) & (lam_full_nm <= 700)

T_plot_list = [2600, 3000, 3400, 5778]
for T_p, col in zip(T_plot_list, colors_pts):
    y_spec = planck(lam_full, T_p)
    # нормуємо до максимуму для порівняння форми
    y_norm = y_spec / np.max(y_spec)
    eta_pt = np.interp(T_p, T_range, eta_pct)
    ax2.plot(lam_full_nm, y_norm, color=col, linewidth=2,
             label=f'T={T_p} К  (η={eta_pt:.1f}%)')
    ax2.fill_between(lam_full_nm, y_norm,
                     where=vis_mask, alpha=0.18, color=col)

ax2.axvspan(400, 700, alpha=0.06, color='yellow', label='Видимий діапазон')
ax2.axvline(400, color='purple', linestyle=':', linewidth=1)
ax2.axvline(700, color='red',    linestyle=':', linewidth=1)

ax2.set_xlabel('Довжина хвилі λ, нм', fontsize=12)
ax2.set_ylabel('Нормована спектральна щільність', fontsize=12)
ax2.set_title('Спектри АЧТ для різних температур', fontsize=12)
ax2.set_xlim(100, 3000)
ax2.set_ylim(0, 1.15)
ax2.legend(fontsize=10, loc='upper right')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 'task_3_2.png'), dpi=150, bbox_inches='tight')
plt.show()
print("Графік збережено: task_3_2.png")