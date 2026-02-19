import numpy as np
import matplotlib.pyplot as plt

# Початкові дані
elements={  #first columnt represents A*10**-23 Дж,second - Z*10**-10 m
    "He": [14e-23, 2.56e-10],
    "Ne": [50e-23, 2.74e-10],
    "Ar": [167e-23, 3.40e-10],
    "Kr": [225e-23, 3.65e-10],
    "Xe": [320e-23, 3.98e-10]
}

R = np.linspace(2.05e-10, 1e-9, 500)
def calculations(A,Z):

    U1=(Z/R)**12 #сили відштовхування
    U2=(Z/R)**6 #сили притягання
    U=4*A*(U1-U2)
    return U

for name, data in elements.items():
    U = calculations(data[0], data[1])
    plt.plot(R, U, label=name)

plt.ylim(-0.32e-20, 0.32e-20)
plt.xlim(2.1e-10,6e-10)
plt.xlabel("Відстань між частинками (м)")
plt.ylabel("Потенціал Ленарда-Джонса (Дж)")
plt.legend()
plt.grid(True)
plt.show()
