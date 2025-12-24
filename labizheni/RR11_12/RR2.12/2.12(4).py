class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def sell(self, amount):
        if amount <= 0:
            raise ValueError("Кількість для продажу має бути більшою за 0!")
        if amount > self.quantity:
            error_msg = "Недостатньо товару '" + self.name + "'. На складі: " + str(self.quantity) + ", Запит: " + str(
                amount)
            raise ValueError(error_msg)

        self.quantity -= amount
        return amount * self.price
if __name__ == "__main__":
    laptop = Product("MacBook", 45000, 5)

    orders = [2, 10, -1, 1]  # Список замовлень (10 - забагато, -1 - помилка)

    print("--- Задача RR2.9: Магазин (Custom Exceptions) ---")

    for order_qty in orders:
        try:
            print("Спроба купити", order_qty, "шт...", end=" ")

            cost = laptop.sell(order_qty)

            print(" Успіх! До сплати:", cost, "грн.")
        except ValueError as e:
            print("\n Відмова:", e)

    print("\nЗалишок на складі:", laptop.quantity)