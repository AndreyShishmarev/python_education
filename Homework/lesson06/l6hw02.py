# 2.	Реализовать класс Road (дорога).
#
# ●	определить атрибуты: length (длина), width (ширина);
# ●	значения атрибутов должны передаваться при создании экземпляра класса;
# ●	атрибуты сделать защищёнными;
# ●	определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ●	использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# ●	проверить работу метода.
#
# Например: 20м*5000м*25кг*5см = 12500 т.

class Road:
    _length = int
    _width = int
    _thickness = 0.5
    _weight = 25

    def __init__(self, lenght, width):
        self._length = lenght
        self._width = width

    def calculation(self):
        calculation = self._length * self._width * self._weight * self._thickness / 1000
        print(f'Необходимо {calculation} тонны асфальта для покрытия всей дороги')


village_road = Road(20, 5000)
village_road.calculation()
