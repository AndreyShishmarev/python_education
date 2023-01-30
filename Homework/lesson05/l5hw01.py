# 1.Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
my_file = open('data.txt', 'w')  # raw
strings = []

while True:
    string = input("Введите строки: ")
    if string == '':
        break
    else:
        new_string = string + '\n'
        strings.append(new_string)
my_file.writelines(strings)
my_file.close()
