# 5.	Реализовать класс Stationery (канцелярская принадлежность).
#
# ●	определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# ●	создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ●	в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# ●	создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:
    title = "Канцелярская принадлежность"

    def draw(self):
        print("Запуск отрисовки!")


class Pen(Stationary):
    title = "Ручкой"

    def draw(self):
        print(f"Отрисовка {self.title}!")


class Pencil(Stationary):
    title = "Карандашом"

    def draw(self):
        print(f"Отрисовка {self.title}!")


class Handle(Stationary):
    title = "Маркером"

    def draw(self):
        print(f"Отрисовка {self.title}!")


stationary = Stationary()
pen = Pen()
pencil = Pencil()
handle = Handle()

stationary.draw()

pen.draw()

pencil.draw()

handle.draw()
