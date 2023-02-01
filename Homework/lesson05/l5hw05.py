# 5.Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('l5hw05.txt') as f_obj:
    if f_obj.writable():
        f_obj.write("15 57 66 22")
    for line in f_obj:
        print(line)
        numbers = line.split()
        result_list = list(map(int, numbers))
        print(sum(result_list))