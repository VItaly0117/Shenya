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


def calculations(A,Z):
    R = np.linspace(0.93 * Z, 2.2 * Z, 500)
    U1=(Z/R)**12 #сили відштовхування
    U2=(Z/R)**6 #сили притягання
    U=4*A*(U1-U2)
    min_lim=0.93*Z
    max_lim=2.5*Z


    return U, min_lim, max_lim,R



for name, data in elements.items():

    U,min_lim,max_lim,R = calculations(data[0], data[1])
    U_min=U[0]
    R_min=R[0]
    for i in range(1,len(U)):#перебираємо кожну точку щоб визначити мінімум
        if U[i]>U[i+1]:
            U_min=U[i+1]
            R_min=R[i+1]
        else:#виходимо х циклу при виконанні умови
            break
    print("Мінімальний потенціал",name," U=",U_min," Дж, на відстані ",R_min,"м")
    # Задаємо параметри графіків
    plt.ylim(min(U) * 1.5, max(U) * 0.3)
    plt.xlim(min_lim, max_lim)
    plt.xlabel("Відстань між частинками (м)")
    plt.ylabel("Потенціал Ленарда-Джонса (Дж)")

    plt.grid(True)

    # Виводимо графіки та легенду
    plt.scatter(R_min, U_min, color="red", marker="o", label="minimum")
    plt.plot(R, U, label=name)
    plt.legend()

    plt.show()


