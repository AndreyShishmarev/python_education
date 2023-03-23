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
    title = "Ручка"

    def draw(self):
        print("Отрисовка ручкой!")


class Pencil(Stationary):
    title = "Карандаш"

    def draw(self):
        print("Отрисовка карандашом!")


class Handle(Stationary):
    title = "Маркер"

    def draw(self):
        print("Отрисовка маркером!")


stationary = Stationary()
pen = Pen()
pencil = Pencil()
handle = Handle()

print(stationary.title)
stationary.draw()

print(pen.title)
pen.draw()

print(pencil.title)
pencil.draw()

print(handle.title)
handle.draw()
