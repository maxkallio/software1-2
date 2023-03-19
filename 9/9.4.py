mport random

class Car:
    def init(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self):
        self.speed += random.randint(-10, 15)
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.max_speed:
            self.speed = self.max_speed

    def drive(self):
        self.distance += self.speed

    def str(self):
        return f"{self.reg_num}\t{self.max_speed} km/h\t{self.speed} km/h\t{self.distance} km"


cars = []
for i in range(1, 11):
    reg_num = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    car = Car(reg_num, max_speed)
    cars.append(car)

# Simulate the car race
winner = None
while winner is None:
    for car in cars:
        car.accelerate()
        car.drive()
        if car.distance >= 10000:
            winner = car
            break

# Print out the properties of each car in a clear table format
print("Registration Number\tMax Speed\tSpeed\tDistance")
for car in cars:
    print(car)
