class MyClass:
    __attr = "значение"
    def __method(self):
        print("Это приватный метод!")

mc = MyClass()
mc.__method()
print(mc.__attr)
