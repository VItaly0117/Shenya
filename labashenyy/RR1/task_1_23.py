# task_1_23.py

# --- ДЕМОНСТРАЦІЯ ТИПОВИХ ЗНАЧЕНЬ ТА КЛЮЧОВИХ АРГУМЕНТІВ ---

def calculate_deposit_interest(amount, term_months, annual_rate=6):
    """
    Розраховує суму відсотків.
    Demonstrates: Параметр за замовчуванням (annual_rate=6).
    Якщо rate не передати, функція візьме 6%.
    """
    monthly_rate = annual_rate / 12 / 100
    total_interest = amount * monthly_rate * term_months
    return total_interest


if __name__ == "__main__":
    print("--- Задача 1.23: Депозит (Типові значення) ---")

    user_amount = float(input("Введіть суму вкладу: "))

    # 1. Виклик без вказання відсотка (використовується типове значення 6%)
    # Це позиційні аргументи
    interest_standard = calculate_deposit_interest(user_amount, 6)
    print(f"Варіант 1 (Стандарт 6%, 6 міс): {interest_standard:.2f} грн")

    # 2. Виклик із зміною відсотка через КЛЮЧОВИЙ аргумент
    # Ми явно вказуємо annual_rate=8
    interest_high = calculate_deposit_interest(amount=user_amount, term_months=12, annual_rate=8)
    print(f"Варіант 2 (Підвищений 8%, 12 міс): {interest_high:.2f} грн")