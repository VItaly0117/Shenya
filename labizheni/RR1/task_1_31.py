# --- ДЕМОНСТРАЦІЯ ДОВІЛЬНОЇ КІЛЬКОСТІ АРГУМЕНТІВ (*ARGS) ---
"""
Знаходить найбільшу швидкість серед усіх переданих значень.
Demonstrates: *args дозволяє передати будь-яку кількість значень
(2, 3, 10 і т.д.) і працювати з ними як з кортежем.
"""
def find_max_flow(*flows):
    if not flows:
        return None

    # ЗАМІНА: Прибрали f-string, просто перелічуємо через кому
    print("DEBUG (Трасування): Отримано аргументів:", len(flows), ". Значення:", flows)

    max_flow = max(flows)
    return max_flow

def convert_m3min_to_ls(flow_m3_min):
    # 1 м3 = 1000 л, 1 хв = 60 с
    return (flow_m3_min * 1000) / 60

if __name__ == "__main__":
    print("--- Задача 1.31: Потоки (*args) ---")

    # Вхідні дані
    flow1_ls = 15.0  # вже в л/с
    flow2_m3min = 1.2  # м3/хв

    # Конвертація
    flow2_ls = convert_m3min_to_ls(flow2_m3min)

    # ЗАМІНА: Прості прінти
    print("Потік 1:", flow1_ls, "л/с")
    print("Потік 2:", flow2_ls, "л/с")

    # Виклик функції з *args.
    # Ми передаємо 4 значення, хоча в умові було 2 потоки.
    # Функція спрацює, бо приймає *args.
    best_flow = find_max_flow(flow1_ls, flow2_ls, 5.5, 25.0)

    # ЗАМІНА
    print("Найбільша швидкість:", best_flow, "л/с")