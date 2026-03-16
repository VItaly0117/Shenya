import numpy as np


def planck_law(lam, T):
    """
    Функція Планка для спектральної випромінювальної здатності.
    lam: довжина хвилі в метрах
    T: абсолютна температура в Кельвінах
    """
    h = 6.626e-34  # Стала Планка
    c = 2.998e8  # Швидкість світла
    k = 1.381e-23  # Стала Больцмана

    # Обчислення показника експоненти
    exponent = (h * c) / (lam * k * T)

    # Захист від переповнення (якщо значення занадто велике)
    if exponent > 700:
        return 0.0

    numerator = 2 * np.pi * h * c ** 2
    denominator = (lam ** 5) * (np.exp(exponent) - 1)

    return numerator / denominator


def calculate_integral(T, start_nm, end_nm, n_steps=10000):
    """
    Обчислення інтеграла методом трапецій
    """
    # Перетворення нм у метри
    a = start_nm * 1e-9
    b = end_nm * 1e-9

    # Крок інтегрування
    dx = (b - a) / n_steps

    # Створення масиву значень довжин хвиль
    x = np.linspace(a, b, n_steps + 1)

    # Обчислення значень функції в кожній точці
    y = []
    for val in x:
        y.append(planck_law(val, T))

    # Метод трапецій: (y0 + yn)/2 + сума проміжних значень, все помножити на dx
    total_sum = (y[0] + y[-1]) / 2.0
    for i in range(1, n_steps):
        total_sum += y[i]

    result = total_sum * dx
    return result


# Вхідні дані
temperature = 5778  # Температура (наприклад, поверхні Сонця)
l_min = 400  # Початок видимого спектру (нм)
l_max = 700  # Кінець видимого спектру (нм)

# Виконання розрахунку
power_density = calculate_integral(temperature, l_min, l_max)

# Вивід результатів без використання f-strings
print("Температура тіла:", temperature, "K")
print("Діапазон хвиль: з", l_min, "нм до", l_max, "нм")
print("Потужність теплового випромінювання одиниці площі:")
print("{:.4f} Вт/м^2".format(power_density))