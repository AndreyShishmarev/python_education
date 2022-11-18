# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x=int(input("Введите число: ")), y=int(input("Введите степень: "))):
    s = x ** y
    return s


print(my_func())


def my_func2(x=int(input("Введите число: ")), y=int(input("Введите степень: "))):
    if y > 0:
        result = 1
        while y != 0:
            result *= x
            y -= 1
        return result
    elif y < 0:
        result = 1
        while y != 0:
            result /= x
            y += 1
        return result


print(my_func2())
