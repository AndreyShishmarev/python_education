# 1.	Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
def calculate_salary(production_in_hours, rate_per_hour, premium):
    try:
        return (production_in_hours * rate_per_hour) + premium
    except TypeError:
        return
print(calculate_salary(10, 3, 6))
