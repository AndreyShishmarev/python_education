month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month = int(input('Введите номер месяца:'))
if month == month_list[0] or month == month_list[1] or month == month_list[11]:
    print('Зима')
elif month == month_list[2] or month == month_list[3] or month == month_list[4]:
    print('Весна')
elif month == month_list[5] or month == month_list[6] or month == month_list[7]:
    print('Лето')
elif month == month_list[8] or month == month_list[9] or month == month_list[10]:
    print('Осень')
else:
    print('Не существует такого месяца')