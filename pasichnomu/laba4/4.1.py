def lagrange_interpolation(x_values, y_values, x):
    """
    Обчислює значення багаточлена Лагранжа у точці x.
    """

    result = 0.0

    for i in x_values:
        # Обчислення базисного полінома l_i(x)
        basis = 1.0
        for j in x_values:
            if i != j:
                basis *= (x - x_values[j]) / (x_values[i] - x_values[j])

        # Додавання до загальної суми: L(x) = sum(y_i * l_i(x))
        result += y_values[i] * basis

    return result



X = [0, 1, 2, 3, 4]
Y = [1, 2, 3, 4, 5]
target_x = 2.5

# Обчислення
answer = lagrange_interpolation(X, Y, target_x)

print("Значення функції при x =", target_x, "дорівнює", answer)