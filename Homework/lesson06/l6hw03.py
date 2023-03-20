# 3.	Реализовать базовый класс Worker (работник).
#
# ●	определить атрибуты: name, surname, position (должность), income (доход);
# ●	последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# ●	создать класс Position (должность) на базе класса Worker;
# ●	в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# ●	проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    name = str
    surname = str
    position = str
    _income = {"wage": int, "bonus": int}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income["wage"] = wage
        self._income["bonus"] = bonus

    def get_full_name(self):
        print(self.name, self.surname, "-", self.position)

    def get_total_income(self):
        print(self._income["wage"] + self._income["bonus"])


p = Position("Jonny", "Walker", "CEO", 23600, 11000)
p.get_full_name()
p.get_total_income()

p2 = Position("Danny", "Koopa", "Streamer", 10000000, 1)
p2.get_full_name()
p2.get_total_income()
