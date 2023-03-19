import random


class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        print(f"Lift is now on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
        print(f"Lift is now on floor {self.current_floor}")

    def go_to_floor(self, floor):
        if floor > self.current_floor:
            for i in range(self.current_floor, floor):
                self.floor_up()
        elif floor < self.current_floor:
            for i in range(floor, self.current_floor):
                self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        elevator = self.elevators[elevator_number]
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)


# Esimerkki käytöstä

my_building = Building(1, 20, 3)

# Hissin liikkuvuus
my_building.run_elevator(0, 5)  # lähetetään hissi numero 0 kerrokseen 5
my_building.run_elevator(1, 10)  # lähetetään hissi numero 1 kerrokseen 10

# palovaroitin
my_building.fire_alarm()  # lähetetään kaikki hissit ensimmäiselle kerrokselle