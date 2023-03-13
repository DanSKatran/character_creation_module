from math import sqrt

message = (
    'Добро пожаловать в самую лучшую программу для вычисления'
    ' квадратного корня из заданного числа'
)


def calculate_squar_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> float:
    """Sorts document in case of less 0."""
    if your_number <= 0:
        return 0
    else:
        square_root = calculate_squar_root(your_number)
        print(f'Мы вычислили квадратный корень из введённого вами числа. Это будет: {square_root}')


print(message)
calc(25.5)