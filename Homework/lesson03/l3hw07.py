# 7.	Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def int_func(string):
    result_string = []
    for word in string:
        result_string.append(word.capitalize())
    return " ".join(result_string)


input_string = input("Введите слова через пробел ").split()
print(int_func(input_string))
