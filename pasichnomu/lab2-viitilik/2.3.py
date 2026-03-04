import numpy as np
import matplotlib.pyplot as plt

def potential(R, A, Z):
    return 4 * A * 1e-23 * ((Z / R)**12 - (Z / R)**6)
def find_min(func, a, b, eps=1e-7):
    while (b - a) > eps:
        m1, m2 = a + (b - a) / 3, b - (b - a) / 3 #максим иди нахуй это тернарий способ который подразумевает
        if func(m1) < func(m2): # котрый откидывает третину вместо простого деления на 2
            b = m2 # целую котик связь
        else:
            a = m1
    return (a + b) / 2
params = {
    'He': (14, 2.56), 'Ne': (50, 2.74), 'Ar': (167, 3.40),'Kr': (225, 3.65),'Xe': (320, 3.98)
}
r_vals = np.linspace(2.5, 8, 500)
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

fig, axes = plt.subplots(2, 3, figsize=(15, 9))
all_axes = axes.flatten()
ax_combined = all_axes[5]
ar_min_u = 0

print(" Minimum Potential Values:")
for i, (name, p) in enumerate(params.items()):
    pot_func = lambda R: potential(R, p[0], p[1])
    r_min = find_min(pot_func, 2.5, 6.0)
    u_min = pot_func(r_min)
    print(f"{name}: R_min = {r_min:.4f} Å, U_min = {u_min:.4e} J")
    if name == 'Ar':
        ar_min_u = u_min
    ax = all_axes[i]
    color = colors[i]
    curve = pot_func(r_vals)
    ax.plot(r_vals, curve, color=color)
    ax.plot(r_min, u_min, 'ro', label=f'Min ({r_min:.2f} Å)')
    ax.set(title=name, ylim=(u_min * 1.2, abs(u_min) * 0.8))
    ax.legend()
    ax_combined.plot(r_vals, curve, label=name, color=color)
for ax in all_axes:
    ax.grid(True)
ax_combined.set(title="Combined Potentials", ylim=(ar_min_u * 1.5, abs(ar_min_u)))
ax_combined.legend()
plt.tight_layout()
plt.show()
