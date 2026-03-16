# ============================================================
# Лабораторна робота №3 — Завдання 3.3
# Обчислення інтегралів трьома методами:
#   • Метод трапецій
#   • Метод Сімпсона
#   • Метод Монте-Карло
# Всі варіанти 1–19 + додатковий (√x·sin(x))
# ============================================================

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.integrate import quad   # для точного значення (еталон)

np.random.seed(2024)

# Зберігаємо графіки у ту саму папку, де лежить цей файл
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
#  Методи чисельного інтегрування
# ============================================================

def trapezoid(func, a, b, n=2000):
    """
    Метод трапецій:
        I ≈ dx · (y₁/2 + y₂ + ... + y_{n-1} + yₙ/2)
    """
    x  = np.linspace(a, b, n + 1)
    y  = func(x)
    dx = (b - a) / n
    return (y[0] / 2 + np.sum(y[1:-1]) + y[-1] / 2) * dx


def simpson(func, a, b, n=2000):
    """
    Метод Сімпсона (n — парне):
        I ≈ (dx/3) · [y₀ + 4y₁ + 2y₂ + 4y₃ + ... + 4y_{n-1} + yₙ]
    """
    if n % 2 != 0:
        n += 1
    x      = np.linspace(a, b, n + 1)
    y      = func(x)
    dx     = (b - a) / n
    result = y[0] + y[-1]
    result += 4.0 * np.sum(y[1:-1:2])
    result += 2.0 * np.sum(y[2:-2:2])
    return result * dx / 3.0


def monte_carlo(func, a, b, n=500_000):
    """
    Метод Монте-Карло (статистична оцінка):
        I ≈ (b − a) · E[f(x)] = (b − a) · (1/N) · Σ f(xᵢ)
    де xᵢ — рівномірно розподілені в [a, b]
    """
    x_rand = np.random.uniform(a, b, n)
    return (b - a) * np.mean(func(x_rand))


# ============================================================
#  Список всіх варіантів інтегралів
# ============================================================
# Формат: (номер, опис_LaTeX, функція, a, b)

INTEGRALS = [

    # ── Варіанти 1–10 (перший інтеграл кожного студента) ────

    # №1  — Андрієвський Кіріл Юрійович
    (1,
     r"$\int_0^1 (\sin x + 1)\,dx$",
     lambda x: np.sin(x) + 1,
     0, 1),

    # №2  — Бунь Даніїл Вячеславович
    (2,
     r"$\int_1^3 |x^2 + 2|\,dx$",
     lambda x: np.abs(x**2 + 2),    # x²+2 > 0 завжди
     1, 3),

    # №3  — Гридньов Костянтин Романович
    (3,
     r"$\int_2^6 (x^3 + 1)\,dx$",
     lambda x: x**3 + 1,
     2, 6),

    # №4  — Калініченко Віталій Миколайович
    (4,
     r"$\int_0^1 (x^3 + x^2)\,dx$",
     lambda x: x**3 + x**2,
     0, 1),

    # №5  — Колєснік Євгенія Миколаївна
    (5,
     r"$\int_{0.1}^{0.5} (x^2 - 4x + 3)\,dx$",
     lambda x: x**2 - 4*x + 3,
     0.1, 0.5),

    # №6  — Колот Артем Михайлович
    (6,
     r"$\int_{-\pi/2}^{\pi/2} (\cos x + x)\,dx$",
     lambda x: np.cos(x) + x,
     -np.pi/2, np.pi/2),

    # №7  — Кононенко Тимофій Анатолійович  ★
    (7,
     r"$\int_1^2 x\ln x\,dx$",
     lambda x: x * np.log(x),
     1, 2),

    # №8  — Литвин Нікіта Сергійович
    (8,
     r"$\int_0^1 \frac{1}{1+x^3}\,dx$",
     lambda x: 1.0 / (1 + x**3),
     0, 1),

    # №9  — Наумейко Артьом Володимирович
    (9,
     r"$\int_1^2 \frac{\ln x}{x}\,dx$",
     lambda x: np.log(x) / x,
     1, 2),

    # №10 — Науменко Богдан Олександрович
    (10,
     r"$\int_1^2 \frac{\cos x}{x}\,dx$",
     lambda x: np.cos(x) / x,
     1, 2),

    # ── Варіанти +10 (другий інтеграл кожного студента) ─────

    # №10б — Науменко Богдан Олександрович  (10+10=20 → варіант "10б" зі списку)
    ("10б",
     r"$\int_0^1 \sqrt{x}\sin x\,dx$",
     lambda x: np.sqrt(x) * np.sin(x),
     0, 1),

    # №11 — Савісько Владислав Васильович  /  також 2й варіант Андрієвського (1+10=11)
    (11,
     r"$\int_0^1 \sqrt{x}\cos x\,dx$",
     lambda x: np.sqrt(x) * np.cos(x),
     0, 1),

    # №12 — Савчук Ярослав Русланович  /  2й варіант Бунь Даніїла (2+10=12)
    (12,
     r"$\int_0^{\pi} \frac{1}{1+x+\sqrt{|\sin x|}}\,dx$",
     lambda x: 1.0 / (1 + x + np.sqrt(np.abs(np.sin(x)))),
     0, np.pi),

    # №13 — Тагіров Дмитро Денисович  /  2й варіант Гридньова (3+10=13)
    (13,
     r"$\int_2^3 \frac{1}{1+\ln\sqrt{x}}\,dx$",
     lambda x: 1.0 / (1 + 0.5 * np.log(x)),
     2, 3),

    # №14 — Тертичний Максим Вадимович  /  2й варіант Калініченка (4+10=14)
    (14,
     r"$\int_0^{\pi/2} \frac{1}{1+\cos^2 x}\,dx$",
     lambda x: 1.0 / (1 + np.cos(x)**2),
     0, np.pi / 2),

    # №15 — Харченко Андрій Юрійович  /  2й варіант Колєснік (5+10=15)
    (15,
     r"$\int_0^{0.5} \sqrt{\frac{1-0.25x^2}{1+x^2}}\,dx$",
     lambda x: np.sqrt((1 - 0.25 * x**2) / (1 + x**2)),
     0, 0.5),

    # №16 — 2й варіант Колота Артема (6+10=16)
    (16,
     r"$\int_0^1 \frac{\sin x}{1+x^2}\,dx$",
     lambda x: np.sin(x) / (1 + x**2),
     0, 1),

    # №17 — 2й варіант Кононенка Тимофія (7+10=17)  ★
    (17,
     r"$\int_0^1 e^{-4x^3+2x+1}\,dx$",
     lambda x: np.exp(-4 * x**3 + 2 * x + 1),
     0, 1),

    # №18 — 2й варіант Литвина Нікіти (8+10=18)
    (18,
     r"$\int_0^{\pi/2} \sqrt{1-0.5\sin^2 x}\,dx$",
     lambda x: np.sqrt(1 - 0.5 * np.sin(x)**2),
     0, np.pi / 2),

    # №19 — 2й варіант Наумейка Артьома (9+10=19)
    (19,
     r"$\int_0^1 \frac{1}{1+\sin^3 x}\,dx$",
     lambda x: 1.0 / (1 + np.sin(x)**3),
     0, 1),
]


# ============================================================
#  Обчислення та таблиця результатів
# ============================================================

print("=" * 82)
print(f"  {'№':<5} {'Метод трапецій':>16}  {'Метод Сімпсона':>16}  "
      f"{'Монте-Карло':>14}  {'Еталон (scipy)':>15}")
print("=" * 82)

results = []
for num, label, func, a, b in INTEGRALS:
    i_trap  = trapezoid(func, a, b)
    i_simp  = simpson(func, a, b)
    i_mc    = monte_carlo(func, a, b)
    i_exact, _ = quad(func, a, b)

    results.append((num, label, func, a, b, i_trap, i_simp, i_mc, i_exact))

    # Відносні похибки відносно scipy
    err_trap = abs(i_trap - i_exact) / (abs(i_exact) + 1e-30) * 100
    err_simp = abs(i_simp - i_exact) / (abs(i_exact) + 1e-30) * 100
    err_mc   = abs(i_mc   - i_exact) / (abs(i_exact) + 1e-30) * 100

    print(f"  {str(num):<5} {i_trap:>16.8f}  {i_simp:>16.8f}  "
          f"{i_mc:>14.8f}  {i_exact:>15.8f}")

print("=" * 82)
print()
print("Похибки відносно scipy (quad):")
print("-" * 82)
print(f"  {'№':<5} {'Трапеції, %':>14}  {'Сімпсон, %':>14}  {'Монте-Карло, %':>16}")
print("-" * 82)
for num, label, func, a, b, i_trap, i_simp, i_mc, i_exact in results:
    err_trap = abs(i_trap - i_exact) / (abs(i_exact) + 1e-30) * 100
    err_simp = abs(i_simp - i_exact) / (abs(i_exact) + 1e-30) * 100
    err_mc   = abs(i_mc   - i_exact) / (abs(i_exact) + 1e-30) * 100
    print(f"  {str(num):<5} {err_trap:>14.6f}  {err_simp:>14.6f}  {err_mc:>16.4f}")
print("=" * 82)


# ============================================================
#  Графіки функцій (сітка 4×5)
# ============================================================

n_total = len(INTEGRALS)
ncols   = 4
nrows   = (n_total + ncols - 1) // ncols    # = 5

fig, axes = plt.subplots(nrows, ncols, figsize=(20, 22))
fig.suptitle("Лабораторна робота №3 — Завдання 3.3\n"
             "Функції для інтегрування (всі варіанти)",
             fontsize=15, fontweight='bold', y=0.995)

axes_flat = axes.flatten()

for idx, (num, label, func, a, b, i_trap, i_simp, i_mc, i_exact) in enumerate(results):
    ax = axes_flat[idx]

    x_plot = np.linspace(a, b, 600)
    y_plot = func(x_plot)

    # Основна крива
    ax.plot(x_plot, y_plot, 'royalblue', linewidth=2.0)

    # Зафарбована область
    ax.fill_between(x_plot, y_plot,
                    alpha=0.20, color='cornflowerblue')
    ax.axhline(0, color='black', linewidth=0.6, alpha=0.5)

    # Межі інтегрування
    ax.axvline(a, color='gray', linestyle=':', linewidth=1.0)
    ax.axvline(b, color='gray', linestyle=':', linewidth=1.0)

    ax.set_title(label, fontsize=9.5, pad=4)
    ax.set_xlabel('x', fontsize=8)
    ax.set_ylabel('f(x)', fontsize=8)
    ax.tick_params(labelsize=7.5)
    ax.grid(True, alpha=0.25)

    # Результат на графіку
    txt = (f"Трап: {i_trap:.5f}\n"
           f"Симп: {i_simp:.5f}\n"
           f"МК:   {i_mc:.5f}")
    ax.text(0.97, 0.97, txt,
            transform=ax.transAxes,
            fontsize=7.0,
            verticalalignment='top',
            horizontalalignment='right',
            bbox=dict(boxstyle='round,pad=0.3',
                      facecolor='lightyellow',
                      edgecolor='gray',
                      alpha=0.85))

# Прибираємо зайві порожні підграфіки
for j in range(idx + 1, len(axes_flat)):
    axes_flat[j].set_visible(False)

plt.tight_layout(rect=[0, 0, 1, 0.985])
plt.savefig(os.path.join(SCRIPT_DIR, 'task_3_3_graphs.png'),
            dpi=140, bbox_inches='tight')
plt.show()
print("Графіки збережено: task_3_3_graphs.png")


# ============================================================
#  Графік порівняння методів (похибки)
# ============================================================

nums_str  = [str(r[0]) for r in results]
errs_trap = [abs(r[5] - r[8]) / (abs(r[8]) + 1e-30) * 100 for r in results]
errs_simp = [abs(r[6] - r[8]) / (abs(r[8]) + 1e-30) * 100 for r in results]
errs_mc   = [abs(r[7] - r[8]) / (abs(r[8]) + 1e-30) * 100 for r in results]

x_pos = np.arange(len(results))
width = 0.28

fig2, ax = plt.subplots(figsize=(18, 6))
ax.bar(x_pos - width, errs_trap, width, label='Трапецій',   color='steelblue',  alpha=0.85)
ax.bar(x_pos,         errs_simp, width, label='Сімпсона',   color='darkorange', alpha=0.85)
ax.bar(x_pos + width, errs_mc,   width, label='Монте-Карло', color='seagreen',   alpha=0.85)

ax.set_yscale('log')
ax.set_xlabel('Номер варіанту', fontsize=12)
ax.set_ylabel('Відносна похибка, %  (лог. шкала)', fontsize=12)
ax.set_title('Порівняння точності методів (N=2000 вузлів, МК=500k точок)',
             fontsize=13, fontweight='bold')
ax.set_xticks(x_pos)
ax.set_xticklabels(nums_str, fontsize=9)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 'task_3_3_errors.png'),
            dpi=140, bbox_inches='tight')
plt.show()
print("Графік похибок збережено: task_3_3_errors.png")