import matplotlib.pyplot as plt

# --- Налаштування файлів ---
file_from_python = 'coordinates_growing_wave.txt'
file_from_spreadsheet = 'function_data.csv'

try:
    # 1. Завантажуємо дані з TXT
    x_py, y_py = [], []
    with open(file_from_python, 'r', encoding='utf-8') as f:
        header = next(f)  # Пропускаємо заголовок
        for line in f:
            if line.strip():
                # Розбиваємо рядок по табуляції та конвертуємо в числа
                parts = line.strip().split('\t')
                x_py.append(float(parts[0]))
                y_py.append(float(parts[1]))

    print(f"Завантажено {len(x_py)} точок з {file_from_python}")

    # 2. Завантажуємо дані з CSV
    x_xls, y_xls = [], []
    with open(file_from_spreadsheet, 'r', encoding='utf-8') as f:
        header = next(f)  # Пропускаємо заголовок
        for line in f:
            if line.strip():
                # Замінюємо кому на крапку для float(), розбиваємо по ';'
                clean_line = line.strip().replace(',', '.')
                parts = clean_line.split(';')
                x_xls.append(float(parts[0]))
                y_xls.append(float(parts[1]))

    print(f"Завантажено {len(x_xls)} точок з {file_from_spreadsheet}")

    # 3. Створюємо графік
    plt.figure(figsize=(12, 7))

    # 4. Малюємо дані з Python-файлу
    plt.plot(x_py, y_py, 'b-', label='Дані з Python (TXT)')

    # 5. Малюємо дані з CSV-файлу
    plt.plot(x_xls, y_xls, 'r--', linewidth=2, label='Дані з Excel (CSV)')

    # 6. Додаємо елементи оформлення
    plt.title('Візуалізація функції згасаючих коливань\ny = x*0.5*sin(3*x)')
    plt.xlabel('Вісь X (час або відстань)')
    plt.ylabel('Вісь Y (амплітуда)')
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.show()

except FileNotFoundError:
    print(f"Помилка: файл не знайдено. Переконайтеся, що {file_from_python} та {file_from_spreadsheet} існують.")
except ValueError as e:
    print(f"Помилка при читанні даних: {e}. Перевірте формат чисел у файлах.")
except Exception as e:
    print(f"Сталася помилка: {e}")