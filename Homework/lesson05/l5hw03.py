# 3.Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
my_file = open('l5hw03.txt', 'r')

for data in my_file.readlines():
    list_values = int(data.split()[1])
    # average = sum(list_values) / len(data.split()[1])
    print(list_values)
    # lastname, salary = data.split()
    # if int(salary) < 20000:
    #     print(data)
    my_file.close()
