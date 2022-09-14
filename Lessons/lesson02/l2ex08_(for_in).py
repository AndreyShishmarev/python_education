users = ["John", "Artur", "Kate"]

# index = 0
# while index < len(users):
#     print(f"Hello, {users[index]}")
#     index += 1

for user in users:
    print(f"Hello, {user}")

# Пример конструкции цикла for in для работы со справочниками, коллекциями и кортежами!
person = {"name": "John", "age": 10}

for key, value in person.items():
    print(f"key {key} = {value}")
