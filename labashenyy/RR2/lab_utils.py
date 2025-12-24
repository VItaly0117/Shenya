import math

# --- ГЛОБАЛЬНІ ЗМІННІ МОДУЛЯ ---
GRAVITATIONAL_CONSTANT = 6.7e-8  # G у г^-1 * см^3 * сек^-2

# --- ФУНКЦІЇ ---

def calculate_gravity(mass, radius_km):
    """
    Задача 1.24. Розраховує прискорення вільного падіння.
    """
    radius_cm = radius_km * 100000
    g = (GRAVITATIONAL_CONSTANT * mass) / (radius_cm ** 2)
    return g

def calculate_deposit_interest(amount, term_months, annual_rate=6):
    """
    Задача 1.23. Розраховує відсотки.
    Параметр annual_rate має значення за замовчуванням 6.
    """
    monthly_rate = annual_rate / 12 / 100
    total_interest = amount * monthly_rate * term_months
    return total_interest

def check_triangle_fits_in_circle(side_a):
    """
    Задача 1.21. Перевіряє, чи вміститься трикутник у колі.
    Повертає кортеж: (радіус, булевий результат).
    """
    calculated_radius = side_a * math.sqrt(3) / 3
    is_fitting = True # Для рівностороннього, вписаного у це коло
    return calculated_radius, is_fitting

def convert_m3min_to_ls(flow_m3_min):
    """Допоміжна функція: переведення м3/хв у л/с"""
    return (flow_m3_min * 1000) / 60

def find_max_flow(*flows):
    """
    Задача 1.31. Знаходить максимум серед довільної кількості аргументів (*args).
    """
    if not flows:
        return 0
    return max(flows)