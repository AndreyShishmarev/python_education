string = input("Введите слова: ")
word = string.split()
str_number = 0

for i in range(len(string)):
    str_number += 1
    new_word = word.index(i)
    print(str_number, new_word[:10])
