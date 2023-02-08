result_dict = {}
average_profit = {}
firm_list = []
with open('l5hw07.txt', encoding='utf-8') as file:
    for line in file:
        data = line.split()
        profit = int(data[2]) - int(data[3])
        loss = int(data[2]) - int(data[3])
        result_dict[data[0]] = profit
    firm_list.append(result_dict)
    average_profit['Средняя прибыль'] = sum(result_dict.values()) / len(result_dict)
    firm_list.append(average_profit)
print(firm_list)