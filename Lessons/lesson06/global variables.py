class Auto:
    info_1 = "Автомобиль заведен"

    def on_start(self):
        info_2 = "Автомобиль зведен"
        return info_2
a = Auto()
print(a.info_1)