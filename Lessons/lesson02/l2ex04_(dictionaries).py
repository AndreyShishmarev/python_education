old_dict = dict(name="John", age=10)
new_dict = {"name": "Jonh", "age": 10}

print(old_dict.keys())
print(old_dict.values())

print(new_dict["age"])
print(new_dict.get("age"))

# print(new_dict["surname"])
if new_dict.get("surname") is None:
    print("No surname")
