import random

class Car:
    def init(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.curr_speed = 0
        self.trav_dist = 0

    def accelerate(self, acc_val):
        self.curr_speed = min(self.curr_speed + acc_val, self.max_speed)

    def drive(self, duration):
        self.trav_dist += self.curr_speed * duration

# Main program
new_car = Car("ABC-123", 142)
print(f"Registration number: {new_car.reg_num}")
print(f"Maximum speed: {new_car.max_speed} km/h")
print(f"Current speed: {new_car.curr_speed} km/h")
print(f"Travelled distance: {new_car.trav_dist} km")
