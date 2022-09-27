string = input("Введите слова: ")
word = string.split()
str_number = 0

for i in range(len(string)):
    str_number += 1
    next_word = word[i]
    print(str_number, next_word[:10])

# while len(string) != n:
#     str_number += 1
#     new_word = word[n]
#     print("Cтрока №", str_number, new_word[:10])
#     n += 1

# print("Длинна строки", len(word_list))
# print("Строка №", str_number + 1, word)
# for i in word_list:
#     print("Слово", word[i])
