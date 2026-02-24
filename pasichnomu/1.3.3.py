import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = np.array([14, 50, 167, 225, 320])
Z = np.array([2.56, 2.74, 3.4, 3.65, 3.98])
names = ['He', 'Ne', 'Ar', 'Kr', 'Xe']
R = np.linspace(1, 10, 500)

# Calculate potentials
# Formula simplified: 10^-10 cancels out in Z/R ratio. A is scaled by 10^-23.
potentials = [4 * a * 1e-23 * ((z/R)**12 - (z/R)**6) for a, z in zip(A, Z)]

# Plotting
fig, axes = plt.subplots(2, 3, figsize=(14, 8))
ax_combined = axes[1, 2]

# Iterate over the first 5 axes (individual plots) and potentials
for i, (ax, pot, name) in enumerate(zip(axes.flat, potentials, names)):
    # Individual plot
    ax.plot(R, pot, color='red' if i == 0 else None)
    ax.set_ylim(pot.min() * 1.2, abs(pot.min()) * 0.5)
    ax.set_title(name)
    
    # Add to combined plot
    ax_combined.plot(R, pot, label=name)

# Common settings for all plots
for ax in axes.flat:
    ax.grid(True)
    ax.set(xlabel="R", ylabel="U")

# Specific settings for combined plot
ar_min = potentials[2].min() # Argon is index 2
ax_combined.set_ylim(ar_min * 2, abs(ar_min))
ax_combined.legend()

plt.tight_layout()
plt.show()