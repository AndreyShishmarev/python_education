# 2.Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
my_file = open('data.txt', 'r')
strings = 0
for string in my_file:
    strings += string.count("\n")
    words = len(string.split())
    print(f"{words} слово в {strings} строке")
print(f"{strings} строки в файле {my_file.name}")
my_file.close()