# 4.Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
source_file = open('l5hw04_source.txt', 'r')
result_file = open('l5hw04_result.txt', 'w')
translate_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
for data in source_file.readlines():
    string = data.split(' - ')
    en_word = string[0]
    ru_word = translate_dict.get(string[0])
    print(f"{ru_word} - {string[1]}")
    print(f"{ru_word} - {string[1]}", file=result_file)
source_file.close()
result_file.close()
