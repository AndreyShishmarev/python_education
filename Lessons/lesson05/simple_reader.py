my_file = open(r'data.txt', 'w')  # raw

# for line in my_file.readlines():
# print(line.replace('\n', ''))

for data in my_file.read(1024):
    print(data)

my_file.close()
