# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def my_func(firstname, lastname, year_of_birth, city, email, phone_number):
    print(
        f"Имя - {firstname}; Фамилия - {lastname}; Год рождения - {year_of_birth}; Город проживания - {city};"
        f" эл.ящик - {email}; номер телефона - {phone_number}")


my_func(firstname="Andrey", lastname="Shishmarev", year_of_birth="1989", city="chita",
        email="ashishmarev89@gmail.com", phone_number="+73254646546")
