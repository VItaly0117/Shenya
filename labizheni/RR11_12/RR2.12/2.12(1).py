def setup_thermostat():
    # Замикання для збереження стану температури
    current_target = 22

    def adjust(new_value):
        nonlocal current_target
        old_value = current_target
        current_target = new_value
        return "Температуру змінено з ", old_value, " на ", current_target

    return adjust


change_temp = setup_thermostat()


def smart_validator(func):
    def wrapper(device_id, value, is_online):
        min_t, max_t = 16, 28

        # Перевірка зв'язку через виключення
        if not is_online:
            raise Exception("Пристрій " + str(device_id) + " не відповідає (Offline)")

        # Перевірка лімітів з конкретизацією причини
        if value < min_t:
            raise Exception("Занадто ХОЛОДНО: " + str(value) + "°C нижче ліміту")
        if value > max_t:
            raise Exception("Занадто ЖАРКО: " + str(value) + "°C вище ліміту")

        message = func(device_id, value, is_online)
        status = change_temp(value)
        return message + " | " + "".join(map(str, status))

    return wrapper


@smart_validator
def set_temperature(device_id, value, is_online):
    return "Сигнал надіслано на " + str(device_id)


# --- ТЕСТУВАННЯ ЧЕРЕЗ TRY-EXCEPT ---
commands = [
    ("Датчик-1", 25, True),  # Успішно
    ("Датчик-1", 10, True),  # Помилка: Холодно
    ("Датчик-2", 35, True),  # Помилка: Жарко
    ("Датчик-3", 20, False),  # Помилка: Офлайн
    ("Датчик-1", 18, True)  # Успішно (замикання покаже зміну з 25 на 18)
]

for d_id, val, online in commands:
    try:
        result = set_temperature(d_id, val, online)
        print("УСПІХ:", result)
    except Exception as e:
        print("ВІДМОВА СИСТЕМИ:", e)