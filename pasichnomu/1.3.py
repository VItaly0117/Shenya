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
    R = np.linspace(0.93*Z, 2.5*Z, 500)
    U1=(Z/R)**12 #сили відштовхування
    U2=(Z/R)**6 #сили притягання
    U=4*A*(U1-U2)
    return R, U


HeR,HeU=calculations(elements["He"][0],elements["He"][1])
plt.plot(HeR,HeU)
NeR,NeU=calculations(elements["Ne"][0],elements["Ne"][1])
plt.plot(NeR,NeU)
ArR,ArU=calculations(elements["Ar"][0],elements["Ar"][1])
plt.plot(ArR,ArU)
KrR,KrU=calculations(elements["Kr"][0],elements["Kr"][1])
plt.plot(KrR,KrU)
XeR,XeU=calculations(elements["Xe"][0],elements["Xe"][1])
plt.plot(XeR,XeU)
plt.grid(True)
plt.show()
