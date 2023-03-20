# Реализуйте базовый класс Car.
#
# ●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# ●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# ●	для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.
from turtle import left


class Car:
    speed = int
    color = str
    name = str
    is_police = bool

    def go(self):
        print("Машина поехала!")

    def stop(self):
        print("Машина остановилась!")

    # def turn(left):
    #     print("Машина повернула на лево")
    #
    # def turn(right):
    #     print("Машина повернула на право")

    def turn(self, direction):
        print("Машина повернула на " + direction)

    def show_speed(self):
        print(self.speed, "км\ч")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(self.speed, "км\ч")
        if self.speed > 60:
            print("Превышение скорости!!!")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(self.speed, "км\ч")
        if self.speed > 40:
            print("Превышение скорости!!!")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


town_car = TownCar(65, "Green", "Mazda", False)
town_car.go()
town_car.turn("Лево")
town_car.show_speed()
town_car.stop()

police_car = PoliceCar(80, "Black", "Ford", True)
police_car.go()
police_car.turn("Право")
police_car.show_speed()
police_car.stop()

