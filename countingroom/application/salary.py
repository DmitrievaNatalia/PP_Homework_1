def calculate_salary():
    try:
        time = float(input('Выработка в часах: '))
        salary = float(input('Ставка в час в рублях: '))
        bonus = float(input('Премия в рублях: '))
        result = time * salary + bonus
        print(f'заработная плата сотрудника  {result}')
    except ValueError:
        return print('введите числовое значение')