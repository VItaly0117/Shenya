import matplotlib.pyplot as plt
import sys
# Збільшимо ліміт рекурсії трохи, але залишимо захист
sys.setrecursionlimit(2000)
def draw_sierpinski(x1, y1, x2, y2, x3, y3, level):
    if level == 0:
        plt.fill([x1, x2, x3], [y1, y2, y3], 'blue')
        return

    # Розрахунок середин сторін
    x12 = (x1 + x2) / 2
    y12 = (y1 + y2) / 2
    x23 = (x2 + x3) / 2
    y23 = (y2 + y3) / 2
    x31 = (x3 + x1) / 2
    y31 = (y3 + y1) / 2

    # Рекурсивні виклики
    draw_sierpinski(x1, y1, x12, y12, x31, y31, level - 1)
    draw_sierpinski(x12, y12, x2, y2, x23, y23, level - 1)
    draw_sierpinski(x31, y31, x23, y23, x3, y3, level - 1)
if __name__ == "__main__":
    try:
        n = int(input("Введіть глибину фракталу (0-8): "))
        if n < 0:
            raise ValueError("Глибина не може бути від'ємною.")
        plt.figure(figsize=(8, 8))
        draw_sierpinski(0, 1, -1, -0.5, 1, -0.5, n)
        plt.axis('equal')
        plt.axis('off')
        plt.show()

    except ValueError as ve:
        print("Помилка вводу:", ve)
    except RecursionError:
        print("Критична помилка: Перевищено ліміт глибини рекурсії! Введіть менше число.")
    except KeyboardInterrupt:
        print("\nПрограму зупинено користувачем.")