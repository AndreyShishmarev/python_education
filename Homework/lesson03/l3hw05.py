# 5. Программа запрашивает у пользователя строку чисел,разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_my_string(x=map(int, input("Введите числа через пробел ").split())):
    return sum(x)


s = sum_my_string()

print(s)

string = input("Введите числа через пробел ")

while string != "`":
    i = map(int, string.split())
    s = s + sum_my_string(i)
    print(s)
    string = input("Введите числа через пробел ")
    if string == "'":
        break
