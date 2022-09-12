revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
profit = revenue - costs
profitability = profit / revenue * 100
if revenue > costs:
    print('Прибыль! ', 'Рентабельность выручки: ', profitability, '%')
    number_of_employees = int(input('Введите количество сотрудников: '))
    profit_per_employee = profit / number_of_employees
    print('Прибыль на одного сотрудника ', profit_per_employee)
elif costs > revenue:
    print('Убыток! ')
