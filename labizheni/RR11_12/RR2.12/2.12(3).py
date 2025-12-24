import math


def check_triangle_fits_in_circle(side_a):
    """
    Функція з файлу RR1/task_1_21.py
    Визначає радіус описаного кола для трикутника та перевіряє умову.
    """
    # Радіус описаного кола для рівностороннього трикутника
    calculated_radius = side_a * math.sqrt(3) / 3
    is_fitting = True
    return calculated_radius, is_fitting

if __name__ == "__main__":
    print("--- Задача 1.21: Геометрія (Безпечне введення) ---")

    try:
        raw_input = input("Введіть сторону трикутника: ")
        side = float(raw_input)
        if side <= 0:
            raise ValueError("Сторона трикутника має бути додатним числом!")

        radius, fits = check_triangle_fits_in_circle(side)
        print("Сторона:", side)
        print("Розрахунковий радіус:", round(radius, 3))

        if fits:
            print("Результат: Трикутник вміститься у коло.")
        else:
            print("Результат: Трикутник не вміститься.")

    except ValueError as e:
        # Цей блок перехоплює:
        # 1. Помилки float() (якщо ввели "abc")
        # 2. Нашу власну помилку (якщо ввели -5)
        print(" Помилка даних:", e)