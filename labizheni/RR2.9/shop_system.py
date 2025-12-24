class Product:
    """
    Клас, що описує окремий товар.
    Властивості: назва, ціна, кількість.
    """

    def __init__(self, name, category, price, quantity):
        # Ініціалізація властивостей об'єкта (Constructor)
        self.name = name  # Публічна властивість
        self.category = category
        self.price = price
        self.quantity = quantity

    def change_price(self, new_price):
        """Змінює ціну товару з перевіркою."""
        if new_price < 0:
            print(f"[Помилка] Ціна для '{self.name}' не може бути від'ємною!")
        else:
            self.price = new_price
            print(f"[Інфо] Нова ціна для '{self.name}': {self.price} грн")

    def restock(self, amount):
        """Додає кількість товару (Прихід)."""
        if amount > 0:
            self.quantity += amount
            print(f"[Склад] Додано {amount} шт. товару '{self.name}'. Всього: {self.quantity}")
        else:
            print("[Помилка] Кількість для додавання має бути додатною.")

    def sell(self, amount):
        """
        Списує товар при продажу.
        Повертає True, якщо операція успішна, і False, якщо товару не вистачає.
        """
        if amount <= 0:
            print("[Помилка] Кількість для продажу має бути більша 0.")
            return False

        if amount > self.quantity:
            print(f"[Увага] Недостатньо товару '{self.name}'! На складі: {self.quantity}, запит: {amount}")
            return False
        else:
            self.quantity -= amount
            total_cost = amount * self.price
            print(f"[Продаж] Продано {amount} шт. '{self.name}' на суму {total_cost} грн. Залишок: {self.quantity}")
            return True

    def __str__(self):
        """Магічний метод для гарного виводу інформації про об'єкт."""
        return f"Товар: {self.name} | Категорія: {self.category} | Ціна: {self.price} грн | К-сть: {self.quantity} шт."


class Warehouse:
    """
    Клас, що керує списком товарів (Агрегація об'єктів Product).
    """

    def __init__(self):
        self.products = []  # Список для зберігання об'єктів класу Product

    def add_product(self, product_obj):
        """Додає об'єкт товару до складу."""
        self.products.append(product_obj)
        print(f"[Склад] Товар '{product_obj.name}' додано до бази.")

    def show_inventory(self):
        """Виводить список всіх товарів."""
        print("\n--- ПОТОЧНИЙ СТАН СКЛАДУ ---")
        if not self.products:
            print("Склад порожній.")
        for p in self.products:
            print(p)  # Тут автоматично спрацює метод __str__ класу Product
        print("-" * 30)

    def get_total_value(self):
        """Рахує загальну вартість товарів на складі."""
        total = 0
        for p in self.products:
            total += p.price * p.quantity
        return total


# --- БЛОК ПЕРЕВІРКИ (Main) ---
if __name__ == "__main__":
    # 1. Створення складу
    my_warehouse = Warehouse()

    # 2. Створення об'єктів товарів (Інстанціювання)
    laptop = Product("MacBook Air", "Ноутбуки", 45000, 5)
    phone = Product("iPhone 15", "Смартфони", 38000, 10)
    mouse = Product("Logitech MX", "Аксесуари", 3500, 20)

    # 3. Додавання товарів на склад
    my_warehouse.add_product(laptop)
    my_warehouse.add_product(phone)
    my_warehouse.add_product(mouse)

    # 4. Перегляд складу
    my_warehouse.show_inventory()

    # 5. Демонстрація роботи методів
    print("\n--- ОПЕРАЦІЇ ---")

    # Спроба продати більше, ніж є (Перевірка логіки)
    laptop.sell(10)

    # Успішний продаж
    phone.sell(2)

    # Зміна ціни
    mouse.change_price(3200)

    # Поповнення запасів
    laptop.restock(3)

    # 6. Фінальний звіт
    my_warehouse.show_inventory()
    total_assets = my_warehouse.get_total_value()
    print(f"\nЗагальна вартість товарів на складі: {total_assets} грн")