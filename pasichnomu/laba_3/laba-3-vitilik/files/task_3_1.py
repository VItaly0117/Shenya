# ============================================================
# Лабораторна робота №3 — Завдання 3.1
# Потужність теплового випромінювання АЧТ у видимому діапазоні
# Метод: ТРАПЕЦІЙ
# ============================================================

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
from matplotlib.colors import LinearSegmentedColormap

# ── Фізичні константи ────────────────────────────────────────
h     = 6.626e-34   # стала Планка, Дж·с
c     = 3.0e8       # швидкість світла, м/с
k     = 1.381e-23   # стала Больцмана, Дж/К

# ── Параметри ─────────────────────────────────────────────────
T          = 5778        # температура (поверхня Сонця), К
lam_min_vis = 400e-9    # мінімум видимого діапазону, м
lam_max_vis = 700e-9    # максимум видимого діапазону, м
N          = 1000        # кількість підінтервалів


# ── Функція Планка ──────────────────────────────────────────
def planck(lam, T):
    """
    Спектральна щільність потужності випромінювання АЧТ [Вт/(м²·м)]
        f(λ, T) = 2π h c² / [λ⁵ (exp(hc / kTλ) − 1)]
    """
    exponent = h * c / (k * T * lam)
    return (2 * np.pi * h * c**2) / (lam**5 * (np.exp(exponent) - 1))


# ── Метод трапецій ─────────────────────────────────────────
def trapezoid(f_vals, dx):
    """
    Формула методу трапецій:
        I ≈ (y₁/2 + y₂ + y₃ + ... + y_{n-1} + yₙ/2) · dx
    """
    return (f_vals[0] / 2 + np.sum(f_vals[1:-1]) + f_vals[-1] / 2) * dx


# ── Обчислення інтегралу ───────────────────────────────────
lambdas_vis = np.linspace(lam_min_vis, lam_max_vis, N + 1)
y_vis       = planck(lambdas_vis, T)
dx          = (lam_max_vis - lam_min_vis) / N

I_visible   = trapezoid(y_vis, dx)

# Повний інтеграл (для порівняння)
lam_full = np.linspace(10e-9, 3000e-9, 10001)
y_full   = planck(lam_full, T)
dx_full  = lam_full[1] - lam_full[0]
I_total  = trapezoid(y_full, dx_full)

# Теоретичний результат за законом Стефана–Больцмана: I = σT⁴ (де σ = 5.67e-8)
sigma        = 5.67e-8
I_stefan     = sigma * T**4

print("=" * 55)
print("  Потужність теплового випромінювання АЧТ")
print("  Метод трапецій")
print("=" * 55)
print(f"  Температура тіла:          T = {T} К")
print(f"  Видимий діапазон:      400–700 нм")
print(f"  Кількість підінтервалів:   N = {N}")
print(f"  Крок інтегрування:        dx = {dx*1e9:.4f} нм")
print("-" * 55)
print(f"  I_видимий  (трапеції) = {I_visible:.4e}  Вт/м²")
print(f"  I_повний   (трапеції) = {I_total:.4e}  Вт/м²")
print(f"  I_повний   (Стефан–Больцман) = {I_stefan:.4e}  Вт/м²")
print(f"  Відносна похибка:   {abs(I_total - I_stefan)/I_stefan * 100:.4f} %")
print(f"  Частка видимого випромінювання: {I_visible/I_stefan*100:.2f} %")
print("=" * 55)


# ── Графік ─────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle(f"Випромінювання абсолютно чорного тіла   (T = {T} K)",
             fontsize=14, fontweight='bold')

# ── Графік 1: повний спектр із виділенням видимого діапазону ──
ax1 = axes[0]
lam_plot_nm = lam_full * 1e9
ax1.plot(lam_plot_nm, y_full, 'b-', linewidth=2, label='Спектр АЧТ')

# Кольорове зафарбування видимого діапазону
vis_mask = (lam_plot_nm >= 400) & (lam_plot_nm <= 700)
ax1.fill_between(lam_plot_nm, y_full,
                 where=vis_mask,
                 alpha=0.55, color='gold',
                 label=f'Видимий діапазон\nI = {I_visible:.3e} Вт/м²')

# Вертикальні границі
ax1.axvline(400, color='purple', linestyle='--', linewidth=1.2, alpha=0.7)
ax1.axvline(700, color='red',    linestyle='--', linewidth=1.2, alpha=0.7)
ax1.annotate('400 нм', xy=(400, 0), xytext=(430, max(y_full)*0.05),
             fontsize=9, color='purple')
ax1.annotate('700 нм', xy=(700, 0), xytext=(720, max(y_full)*0.05),
             fontsize=9, color='red')

ax1.set_xlabel('Довжина хвилі λ, нм', fontsize=12)
ax1.set_ylabel('Спектральна щільність, Вт/(м²·м)', fontsize=12)
ax1.set_title('Повний спектр та видимий діапазон', fontsize=12)
ax1.set_xlim(0, 2500)
ax1.set_ylim(bottom=0)
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)


# ── Графік 2: видимий діапазон з трапеціями ──────────────────
ax2 = axes[1]
n_trap = 20   # показуємо лише 20 трапецій для наочності
lam_trap_nm = np.linspace(400, 700, n_trap + 1)
y_trap      = planck(lam_trap_nm * 1e-9, T)

# Малюємо трапеції
for i in range(n_trap):
    x_seg = [lam_trap_nm[i], lam_trap_nm[i], lam_trap_nm[i+1], lam_trap_nm[i+1]]
    y_seg = [0, y_trap[i], y_trap[i+1], 0]
    ax2.fill(x_seg, y_seg, alpha=0.25, color='steelblue')
    ax2.plot([lam_trap_nm[i], lam_trap_nm[i+1]],
             [y_trap[i], y_trap[i+1]], 'steelblue', linewidth=0.8)

# Точна крива
lam_vis_nm = np.linspace(400, 700, 1000)
y_vis_plot = planck(lam_vis_nm * 1e-9, T)
ax2.plot(lam_vis_nm, y_vis_plot, 'r-', linewidth=2.5, label='f(λ,T) — точна крива')

ax2.set_xlabel('Довжина хвилі λ, нм', fontsize=12)
ax2.set_ylabel('Спектральна щільність, Вт/(м²·м)', fontsize=12)
ax2.set_title(f'Метод трапецій (N={n_trap} трапецій показано)', fontsize=12)
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.3)

# Текстовий блок з результатом
textstr = (f'N = {N} підінтервалів\n'
           f'I = {I_visible:.4e} Вт/м²')
ax2.text(0.97, 0.97, textstr, transform=ax2.transAxes,
         fontsize=10, verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 'task_3_1.png'), dpi=150, bbox_inches='tight')
plt.show()
print("Графік збережено: task_3_1.png")