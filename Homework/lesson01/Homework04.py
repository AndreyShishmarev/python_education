n = int(input("Введите число: "))
max = 0
while n > 10:
    count = n % 10
    if count >= max:
        max = count
    n //= 10

print(max)