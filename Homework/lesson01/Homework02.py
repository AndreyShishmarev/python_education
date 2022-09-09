time = int(input("Введите время в секундах: "))
# print('{}'.format(time / 60))
# print('{}'.format(time / 3600))
print(f'{time // 3600}:{time // 60}:{time % 60}')
