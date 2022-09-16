volume_list = []
for element in range(int(input('Введите количество элементов списка:'))):
    print('Элемент списка №', element + 1)
    volume_list.append(input('Введите значение: '))
print(volume_list)

for el in range(0, len(volume_list)-1, 2):
     volume_list[el], volume_list[el+1] = volume_list[el+1], volume_list[el]
print(volume_list)
