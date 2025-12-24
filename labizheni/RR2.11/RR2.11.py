def setup_thermostat():
    # Замикання: зберігаємо стан цільової температури всередині
    current_target = 20

    def adjust(new_value):
        nonlocal current_target
        old_value = current_target
        current_target = new_value
        return "Температуру змінено з ", old_value, " на ", current_target

    return adjust


# Створюємо екземпляр замикання
change_temp = setup_thermostat()


def connection_required(func):
    # Декоратор: імітуємо перевірку зв'язку з девайсом
    def wrapper(device_id, value, is_online):
        if not is_online:
            return "Помилка: Пристрій", device_id, "поза мережею!"

        # Викликаємо основну логіку
        message = func(device_id, value, is_online)
        # Додаємо дані із замикання
        status = change_temp(value)
        return message, "|", "".join(map(str, status))

    return wrapper


@connection_required
def set_smart_home_temp(device_id, value, is_online):
    return "Команда прийнята для " + str(device_id)


# ПЕРЕВІРКА:
# 1. Спроба змінити температуру на офлайн девайсі
print(*set_smart_home_temp("LivingRoom-01", 22, False))

# 2. Успішна зміна (з 20 на 24)
print(*set_smart_home_temp("LivingRoom-01", 24, True))

# 3. Наступна зміна (вже з 24 на 18) - замикання "пам'ятає" попереднє значення
print(*set_smart_home_temp("LivingRoom-01", 18, True))