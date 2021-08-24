from countingroom.application.salary import calculate_salary
from countingroom.application.db.people import get_employees
from datetime import date

if __name__ == '__main__':
    print(date.today())
    get_employees()
    calculate_salary()
