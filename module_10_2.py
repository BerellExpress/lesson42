import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies_left = 100
        self.days_of_battle = 0

    def run(self):
        print(f'{self.name}, на нас напали!')

        while self.enemies_left > 0:
            if self.enemies_left <= self.power:
                self.enemies_left -= self.enemies_left
            else:
                self.enemies_left -= self.power

            self.days_of_battle += 1
            time.sleep(1)  # Задержка на 1 секунду
            print(f'{self.name} сражается {self.days_of_battle} день(дня), '
                  f'осталось {self.enemies_left} воинов.')

        print(f'{self.name} одержал победу спустя {self.days_of_battle} дней(дня)!')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

# Запускаем потоки
first_knight.start()
second_knight.start()

# Ожидаем завершения обоих потоков
first_knight.join()
second_knight.join()

# Сообщение об окончании всех битв
print('Все битвы закончились!')