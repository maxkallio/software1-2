class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed < 0:
            self.current_speed = 0
        elif new_speed > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed = new_speed

# luodaan uusi auto
new_car = Car("ABC-123", 142)

# lisätään auton nopeutta +30 km, jonka jälkeen +70km/h ja lopuksi +50km/h
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

# printataan auton nykyinen nopeus
print("Текущая скорость: ", new_car.current_speed, "км/ч")

# pysähdys, vähennetään nopeutta -200km/h
new_car.accelerate(-200)

# printataan lopullinen auton nopeus
print("Конечная скорость: ", new_car.current_speed, "км/ч")