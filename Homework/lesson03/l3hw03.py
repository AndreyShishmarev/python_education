# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def first_func(var_1, var_2, var_3):
    return max(var_1 + var_2, var_1 + var_3, var_2 + var_3)


print("Max =", first_func(10, 20, 30))
