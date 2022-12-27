# 1.	Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
def calculate_salary(production_in_hours, rate_per_hour, premium):
    salary = (production_in_hours * rate_per_hour)
    try:
        return salary + salary / 100 * premium
    except TypeError:
        return


print(calculate_salary(10, 10, 60))
