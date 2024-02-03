from test import time

def time2():
    hourr = int(input("Введите часы:"))
    minn = int(input("Введите минуты:"))
    secc = int(input("Введите секунды:"))

    print(f"За {hourr} ч : {minn} мин : {secc} сек проходит - {time(hourr, minn, secc)} секунд")
time2()

