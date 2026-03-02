import numpy as np
import matplotlib.pyplot as plt

# Початкові дані
e=1e-13
elements={  #first columnt represents A*10**-23 Дж,second - Z*10**-10 m
    "He": [14e-23, 2.56e-10],
    "Ne": [50e-23, 2.74e-10],
    "Ar": [167e-23, 3.40e-10],
    "Kr": [225e-23, 3.65e-10],
    "Xe": [320e-23, 3.98e-10]
}


def calculations(A,Z,R):

    U1=(Z/R)**12 #сили відштовхування
    U2=(Z/R)**6 #сили притягання
    U=4*A*(U1-U2)
    min_lim=0.93*Z
    max_lim=2.5*Z

    return U, min_lim, max_lim,

for name, data in elements.items():
    a = 0.93*data[1]
    b = 2.2*data[1]

    while abs(a - b) > 2*e:  # знаходимо максимум методом дихотомії
        if  calculations(data[0],data[1],((a + b) / 2 + e / 2)) > calculations(data[0],data[1],((a + b) / 2 - e / 2)):
            b = (a + b) / 2 + e / 2
        else:
            a = (a + b) / 2 - e / 2

    x_max = (a + b) / 2


    plt.scatter(x_max,calculations(data[0],data[1],x_max)[0],color="red",marker="o",label="minimum")#виводимо точку мінімуму
    R = np.linspace(0.93 * data[1], 2.2 * data[1], 500)
    U,min_lim,max_lim = calculations(data[0], data[1],R)
    plt.plot(R, U, label=name)#виводимо графік для кращого розуміння



    plt.ylim(min(U) * 1.5, max(U) * 0.3)
    plt.xlim(min_lim, max_lim)
    plt.xlabel("Відстань між частинками (м)")
    plt.ylabel("Потенціал Ленарда-Джонса (Дж)")
    plt.legend()
    plt.grid(True)
    plt.show()


