class Auto:
    def __init__(self):
        print("Автомобиль заведен")
        self.auto_name = "Mazda"  # публичная переменная
        self._auto_year = 2019  # защищённая переменна
        self.__auto_model = "CX9"  # приватная переменная


a = Auto()
print(a.auto_name)

print(a.auto_model)