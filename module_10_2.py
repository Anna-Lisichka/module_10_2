from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name, power, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 100
        for i in range(100-self.power, -10, -self.power):
            days = (100 - i) / self.power
            sleep(1)
            print(f'{self.name} сражается {int(days)} день(дня)..., осталось {i} войнов')
        print(f'{self.name} одержал победу спустя {int(days)} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(f'Все битвы закончились!')
