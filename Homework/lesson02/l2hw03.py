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

month_dict = {"Январь": 1, "Февраль": 2, "Март": 3, "Апрель": 4, "Май": 5, "Июнь": 6, "Июль": 7, "Август": 8,
              "Сентябрь": 9,
              "Октябрь": 10, "Ноябрь": 11, "Декабрь": 12}
month_number = int(input('Введите номер месяца: '))
if month_number == month_dict.get('Январь') or month_number == month_dict.get('Февраль') or month_number == month_dict.get("Декабрь"):
    print('Зима')
elif month_number == month_dict.get('Май') or month_number == month_dict.get("Март") or month_number == month_dict.get("Апрель"):
    print('Весна')
elif month_number == month_dict.get("Июнь") or month_number == month_dict.get("Июль") or month_number == month_dict.get("Август"):
    print('Лето')
elif month_number == month_dict.get("Сентябрь") or month_number == month_dict.get("Октябрь") or month_number == month_dict.get("Ноябрь"):
    print('Осень')
else:
    print('Такого месяца не существует!')
