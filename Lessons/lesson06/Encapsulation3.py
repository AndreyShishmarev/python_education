class MyClass:
    __attr = "значение"
    def __method(self):
        print("Это защищённый метод!")

mc = MyClass()
mc._MyClass__method()
print(mc._MyClass__attr)
