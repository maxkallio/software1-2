import random

class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def drive(self):
        self.distance += self.speed

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.speed += random.randint(-5, 5)
            car.drive()

    def print_status(self):
        print(f"{'Name':<10}{'Speed':<10}{'Distance':<10}")
        for car in self.cars:
            print(f"{car.name:<10}{car.speed:<10}{car.distance:<10}")

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False

# luodaan autot
car1 = Car("Car 1", 100)
car2 = Car("Car 2", 120)
car3 = Car("Car 3", 110)
car4 = Car("Car 4", 105)
car5 = Car("Car 5", 90)
car6 = Car("Car 6", 95)
car7 = Car("Car 7", 115)
car8 = Car("Car 8", 130)
car9 = Car("Car 9", 125)
car10 = Car("Car 10", 135)

# luodaan kilpailu
race = Race("Grand Demolition Derby", 8000, [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10])

# Aloitetaan kilpailu
hours = 0
while not race.race_finished():
    if hours % 10 == 0:
        print(f"\nCurrent status after {hours} hours:")
        race.print_status()
    race.hour_passes()
    hours += 1