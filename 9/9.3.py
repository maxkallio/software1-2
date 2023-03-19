class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, speed_change):
        self.speed += speed_change
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.max_speed:
            self.speed = self.max_speed

    def drive(self, hours):
        self.distance += self.speed * hours


# tehdään pelin objekti Car
car = Car("ABC-123", 142)

# lisätään nopeutta +30km/h
car.accelerate(30)

# lisätään lisää nopeutta +30km/h
car.accelerate(70)

# lisätään lisää nopeutta +30km/h
car.accelerate(50)

# printataan nykyinen nopeus
print("Nykyinen nopeus: {} km/h".format(car.speed))

# pysähdys
car.accelerate(-200)

# printataan lopullinen nopeus
print("lopullinen nopeus: {} км/ч".format(car.speed))

# lisätään etäisyyttä pouolitoista tuntia nopeudella 60km/h
car.drive(1.5)

# printataan etäisyys joka ajettiin
print("ajettu etäisyys: {} km".format(car.distance))