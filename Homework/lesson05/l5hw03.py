# 3.Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
my_file = open('l5hw03.txt', 'r')

my_list = []
my_sum = 0
count = 0

for data in my_file.readlines():
    lastname, salary = data.split()
    if int(salary) < 20000:
        # print(data)
        my_list.append(lastname)
        my_sum += int(data.split()[1])
        count += 1
average = my_sum / count
print(f"Сотрудники: ", my_list)
print(f"Средняя ЗП: ", average)
my_file.close()
