# 6.	*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.

goods = []
while input("Хотите добавить товар? д\н ") == "д":
    product_number = int(input("Введите номер продукта "))
    product_options = {}
    while input("Хотите добавить параметры товара? д\н ") == "д":
        product_options_key = input("Введите характеристику товара ")
        product_options_value = input("Введите значение характеристики товара ")
        product_options[product_options_key] = product_options_value
    goods.append(tuple([product_number, product_options]))
print(goods)

analitics = {}
for good in goods:
    for product_options_key, product_options_value in good[1].items():
        if product_options_key in analitics:
            analitics[product_options_key].append(product_options_value)
        else:
            analitics[product_options_key] = [product_options_value]
print(analitics, "\n")
