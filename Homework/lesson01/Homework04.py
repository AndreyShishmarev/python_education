n = int(input("Введите число: "))
max = 0
while n != 0:
    count = n % 10
    if count >= max:
        max = count
    n //= 10
print(max)
