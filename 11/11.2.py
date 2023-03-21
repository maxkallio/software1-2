class Car:
    def init(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.km_counter = 0

    def drive(self, hours, speed):
        self.km_counter += hours * speed

class ElectricCar(Car):
    def init(self, reg_number, max_speed, battery_capacity):
        super().init(reg_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def init(self, reg_number, max_speed, tank_volume):
        super().init(reg_number, max_speed)
        self.tank_volume = tank_volume


electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.drive(3, 120)
gasoline_car.drive(3, 100)

print("Electric car km counter:", electric_car.km_counter)
print("Gasoline car km counter:", gasoline_car.km_counter)