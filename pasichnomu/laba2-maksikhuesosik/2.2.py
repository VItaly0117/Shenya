import matplotlib.pyplot as plt
import numpy as np
#задаємо початкові параметри
a = -10
b = 10
e = 0.001
def func(x):#задаємо функцію
    return ((0.03*x-3)*x+3)*x



while abs(a - b) > e:#знаходимо максимум методом дихотомії
    if func((a+b)/2+e/2)<func((a+b)/2-e/2):
        b = (a+b)/2+e/2
    elif func((a+b)/2+e/2)>func((a+b)/2-e/2):
        a = (a+b)/2-e/2
    elif func((a + b) / 2 + e/2) == func((a + b) / 2 - e/2):
        b = (a+b)/2-e/2
x_max=(a+b)/2

print("Максимальне значення функції у=",func(x_max)," в точці х=",x_max)

plt.scatter(x_max,func(x_max),color="red",label="maximum")#позначаємо точку максимуму


r= np.linspace(-10,10,2000)
plt.plot(r,func(r),label="y=((0.03*x-3)*x+3)*x")#створюємо графік для зручності

#добавляєм штучкі в графік
plt.grid(True)
plt.legend()
plt.show()