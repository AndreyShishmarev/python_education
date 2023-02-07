my_dict = {}
average_profit = {}
my_list = []
with open('l5hw07.txt', encoding='utf-8') as file:
    for line in file:
        # print(line)
        data = line.split()
        # print(data[2],data[3])
        profit = int(data[2]) - int(data[3])
        # print(profit)
        if profit > 0:
            my_dict[data[0]] = profit
    my_list.append(my_dict)
# avr_profit = sum(int(my_dict[0]))/len(my_dict)
# print(avr_profit)
print(my_list.__len__())
print(my_dict.__len__())
print(my_dict)
