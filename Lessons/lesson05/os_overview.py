import os

if os.path.exists('data.txt'):
    os.remove('data.txt')

current_dir = '..'
files = os.listdir()

for x in files:
    print(os.path.split(x))
    # print(os.path.isdir(f"./{x}"))

print(os.path.split('\ASUS\SDC\Download'))

print(os.path.join('\ASUS\SDC\Download', 'file', 'hop', '1.txt'))