import lab_utils

def print_menu():
    print("\n--- ГОЛОВНЕ МЕНЮ ---")
    print("1. Порівняти гравітацію (Венера vs Сатурн) [Глобальні змінні]")
    print("2. Розрахувати депозит [Аргументи за замовчуванням]")
    print("3. Трикутник і коло [Повернення кількох значень]")
    print("4. Порівняння потоків [Довільна кількість аргументів *args]")
    print("0. Вихід")

def main():
    while True:
        print_menu()
        choice = input("Оберіть пункт: ")

        if choice == '1':
            # Виклик функцій з модуля через крапку: lab_utils.назва_функції
            g_venus = lab_utils.calculate_gravity(4.86e27, 6175)
            g_saturn = lab_utils.calculate_gravity(5.68e29, 57750)

            print(f"\nВенера g: {g_venus:.2f}, Сатурн g: {g_saturn:.2f}")
            if g_saturn > g_venus:
                print("Сатурн перемагає.")
            else:
                print("Венера перемагає.")

        elif choice == '2':
            amount = float(input("Введіть суму вкладу: "))
            res1 = lab_utils.calculate_deposit_interest(amount, 6)
            res2 = lab_utils.calculate_deposit_interest(amount, 12, annual_rate=8)

            print(f"\nПри 6% на півроку: {res1:.2f} грн")
            print(f"При 8% на рік: {res2:.2f} грн")

        elif choice == '3':
            side = float(input("Введіть сторону трикутника: "))
            radius, is_ok = lab_utils.check_triangle_fits_in_circle(side)

            print(f"\nНеобхідний радіус: {radius:.3f}")
            print(f"Чи поміститься: {is_ok}")

        elif choice == '4':
            f1 = 15.0
            f2_raw = 1.2
            # Виклик допоміжної функції з модуля
            f2 = lab_utils.convert_m3min_to_ls(f2_raw)

            print(f"\nПотік 1: {f1}, Потік 2 (конвертований): {f2}")
            # Виклик функції з *args
            best = lab_utils.find_max_flow(f1, f2, 100.0, 0.5)
            print(f"Максимум серед (15.0, 20.0, 100.0, 0.5): {best}")

        elif choice == '0':
            print("Роботу завершено.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")
if __name__ == "__main__":
    main()