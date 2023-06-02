class Person:
   def __init__(self, attrs: dict):
       self.attributes = attrs

john = Person({"first_name": "John", "last_name": "Doe", "age": 30})
print(john.attributes['first_name'])
