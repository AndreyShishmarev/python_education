# 7.Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

result_dict = {}
average_profit = {}
firm_list = []
with open('l5hw07.txt', encoding='utf-8') as file:
    for line in file:
        data = line.split()
        profit = int(data[2]) - int(data[3])
        if profit >= 0:
            result_dict[data[0]] = profit
            average_profit['Средняя прибыль'] = sum(result_dict.values()) / len(result_dict)
        elif profit < 0:
            result_dict[data[0]] = profit
firm_list.append(result_dict)
firm_list.append(average_profit)
print(firm_list)

with open('l5hw07.json', 'w') as json_file:
    json.dump(firm_list, json_file)
