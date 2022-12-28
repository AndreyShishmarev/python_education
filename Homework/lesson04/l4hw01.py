# 1.	Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

file_name, production_in_hours, rate_per_hour, premium = argv
salary = int(production_in_hours) * int(rate_per_hour)
calculate_salary = salary + salary / 100 * int(premium)
print(calculate_salary)

# def calculate_salary(production_in_hours, rate_per_hour, premium):
#     salary = (production_in_hours * rate_per_hour)
#     try:
#         return salary + salary / 100 * premium
#     except TypeError:
#         return
#
#
# print(calculate_salary(10, 10, 60))
