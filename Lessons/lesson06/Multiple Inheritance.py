# Механизм наследования может быть реализован с использованием нескольких родителей у одного класса.
# И наоборот, один класс-родитель будет передавать свои характеристики нескольким дочерним классам.

# Несколько дочерних классов у одного родителя

# Пример:

# класс Transport
class Transport:
    def transport_method(self):
        print("Родительский метод класса Transport")


# класс Auto, наследующий Transport
class Auto(Transport):
    def auto_method(self):
        print("Дочерний метод класса Auto")


# класс Bus, наследующий Transport
class Bus(Transport):
    def bus_method(self):
        print("Дочерний метод класса Bus")


# В этом примере у нас есть класс-родитель Transport, наследуемый дочерними классами Auto и Bus.
# В обоих дочерних классах возможен доступ к методу transport_method() класса-родителя.
# Для запуска скрипта создадим экземпляры класса.

# Пример:

a = Auto()
a.transport_method()
b = Bus()
b.transport_method()


# Рассмотрим ещё один пример, в котором класс-родитель Shape определяет атрибуты.
# Эти атрибуты могут быть характерны для всех классов-наследников.
# Например, цвет фигуры, ширина и высота, основание и высота.
# Здесь в конструкторах классов-наследников инициализируются параметры.
# Часть их — собственные атрибуты классов-наследников, а некоторые наследуются от родителей.
# Чтобы работать с унаследованными атрибутами, нужно их перечислить, например,
# super().__init__(color, param_1, param_2).
# Тем самым мы показываем, что хотим иметь возможность работы с атрибутами класса-родителя.
# Если атрибуты не перечислить, то при попытке обращения к ним через экземпляр класса-наследника возникнет ошибка.

# Пример:

class Shape:
    def __init__(self, color, param_1, param_2):
        self.color = color
        self.param_1 = param_1
        self.param_2 = param_2

    def square(self):
        return self.param_1 * self.param_2


class Rectangle(Shape):
    def __init__(self, color, param_1, param_2, rectangle_p):
        super().__init__(color, param_1, param_2)
        self.rectangle_p = rectangle_p

    def get_r_p(self):
        return self.rectangle_p


class Triangle(Shape):
    def __init__(self, color, param_1, param_2, triangle_p):
        super().__init__(color, param_1, param_2)
        self.triangle_p = triangle_p

    def get_t_p(self):
        return self.triangle_p


r = Rectangle("white", 10, 20, True)
print(r.color)
print(r.square())
print(r.get_r_p())
t = Triangle("red", 30, 40, False)
print(t.color)
print(t.square())
print(t.get_t_p())


# Несколько родителей у одного класса

# Пример:

class Player:
    def player_method(self):
        print("Родительский метод класса Player")


class Navigator:
    def navigator_method(self):
        print("Родительский метод класса Navigator")


class MobilePhone(Player, Navigator):
    def mobile_phone_method(self):
        print("Дочерний метод класса MobilePhone")


# В этом примере создаются классы: Player, Navigator, MobilePhone.
# Причём классы Player и Navigator — родительские для класса MobilePhone.
# Поэтому класс MobilePhone имеет доступ к методам классов Player и Navigator. Проверим это.

# Пример:

m_p = MobilePhone()
m_p.player_method()
m_p.navigator_method()


# Возможна ситуация, когда у классов-родителей совпадают имена атрибутов и методов.
# В этом случае обращение к такому атрибуту или методу через «наследник» будет адресовано к атрибуту или методу
# того класса-родителя, который значится первым.

# Пример:

class Shape:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def get_params(self):
        return f"Параметры Shape: {self.param_1}, {self.param_2}"


class Material:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def get_params(self):
        return f"Параметры Material: {self.param_1}, {self.param_2}"


class Triangle(Shape, Material):
    def __init__(self, param_1, param_2):
        super().__init__(param_1, param_2)
        pass


t = Triangle(10, 20)
print(t.get_params())
