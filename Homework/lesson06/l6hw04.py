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
class Car:
    speed = int
    color = str
    name = str
    is_police = bool

    def go(self):
        pass

    def stop(self):
        pass

    def turn(direction):
        pass

    def show_speed(self):
        pass


class TownCar(Car):
    pass

    def show_speed(self):
        pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass

    def show_speed(self):
        pass


class PoliceCar(Car):
    pass
