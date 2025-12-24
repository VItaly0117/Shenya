class Product:
    def __init__(self, name, category, price, quantity):
        # Конструктор: задаємо початкові дані товару
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def change_price(self, new_price):
        # Зміна ціни
        if new_price < 0:
            print("Помилка: ціна не може бути менше 0")
        else:
            self.price = new_price
            print("Ціна для", self.name, "змінена на", self.price)

    def restock(self, amount):
        # Додавання товару (прихід)
        if amount > 0:
            self.quantity += amount
            print("Додано", amount, "шт. товару", self.name)
        else:
            print("Кількість має бути додатною")

    def sell(self, amount):
        # Продаж товару
        if amount <= 0:
            print("Кількість для продажу має бути більше 0")
            return

        if amount > self.quantity:
            print("Не вистачає товару", self.name, "на складі. Є лише:", self.quantity)
        else:
            self.quantity -= amount
            total_cost = amount * self.price
            print("Продано", amount, "шт.", self.name, "на суму:", total_cost)

    def __str__(self):
        # Метод для виводу інформації про об'єкт
        return "Товар: " + self.name + " | Ціна: " + str(self.price) + " | К-сть: " + str(self.quantity)


class Warehouse:
    def __init__(self):
        self.products = []  # Список товарів

    def add_product(self, product):
        self.products.append(product)
        print("Товар", product.name, "додано на склад")

    def show_inventory(self):
        print("\n--- Стан складу ---")
        if len(self.products) == 0:
            print("Склад порожній")
        else:
            for p in self.products:
                print(p)  # Викликає __str__ у Product
        print("-------------------")

    def get_total_value(self):
        total = 0
        for p in self.products:
            total += p.price * p.quantity
        return total


# --- Основна частина ---
if __name__ == "__main__":
    # Створюємо склад
    my_warehouse = Warehouse()

    # Створюємо товари
    laptop = Product("MacBook Air", "Ноутбуки", 45000, 5)
    phone = Product("iPhone 15", "Смартфони", 38000, 10)
    mouse = Product("Logitech MX", "Аксесуари", 3500, 20)

    # Додаємо на склад
    my_warehouse.add_product(laptop)
    my_warehouse.add_product(phone)
    my_warehouse.add_product(mouse)

    # Показуємо що є
    my_warehouse.show_inventory()

    print("\n--- Перевірка роботи методів ---")

    # 1. Спроба продати забагато
    laptop.sell(10)

    # 2. Нормальний продаж
    phone.sell(2)

    # 3. Зміна ціни
    mouse.change_price(3200)

    # 4. Поповнення складу
    laptop.restock(3)

    # Фінальний звіт
    my_warehouse.show_inventory()

    # Вивід загальної вартості
    total = my_warehouse.get_total_value()
    print("Загальна вартість товарів:", total, "грн")