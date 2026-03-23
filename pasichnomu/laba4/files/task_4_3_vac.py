import numpy as np
import matplotlib.pyplot as plt

R0 = 5
I = np.arange(0.25, 10.25, 0.25)
U_ideal = R0 * I

# 4.3 — ідеальна ВАХ
plt.figure()
plt.plot(I, U_ideal)
plt.title("ВАХ резистора R=5 Ом")
plt.xlabel("I, A")
plt.ylabel("U, В")
plt.grid()
plt.show()

# 4.3.1 — з шумом і МНК
for p in [0.03, 0.15, 0.30]:
    R_noise = R0 + p * (2*np.random.random(len(I)) - 1) * R0
    U_noise = R_noise * I

    # МНК без вільного члена: U = a*I
    a = np.dot(I, U_noise) / np.dot(I, I)
    print(f"p={p}: R_fit = {a:.4f} Ом")

    plt.figure()
    plt.scatter(I, U_noise, s=20, label="З шумом")
    plt.plot(I, a*I, color="red", label=f"МНК: R≈{a:.3f}")
    plt.plot(I, U_ideal, linestyle="--", label="Ідеал")
    plt.title(f"ВАХ з шумом p={p}")
    plt.xlabel("I, A")
    plt.ylabel("U, В")
    plt.legend()
    plt.grid()
    plt.show()