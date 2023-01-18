# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Решите задание в одну строку.
# Подсказка: используйте функцию range() и генератор.
# def my_generator():
#     for i in range(20, 240):
#         if i % 20 == 0 or i % 21 == 0:
#             print(i)

my_generator = (i % 20 == 0 or i % 21 == 0 for i in range(20, 240))

for el in my_generator:
    print(el)
