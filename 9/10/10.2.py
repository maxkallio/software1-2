class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        print("hissi on", self.current_floor, "kerroksella")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
        print("hissi on", self.current_floor, "kerroksella")

    def go_to_floor(self, destination_floor):
        if self.current_floor < destination_floor:
            for i in range(self.current_floor, destination_floor):
                self.floor_up()
        elif self.current_floor > destination_floor:
            for i in range(self.current_floor, destination_floor, -1):
                self.floor_down()
        print("hissi on tullut kerrokselle", destination_floor)


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, destination_floor):
        self.elevators[elevator_number].go_to_floor(destination_floor)


# luodaan talo jossa on 2 hissin kerrosta, jotka voivat mennä 1-10 kerrokseen
building = Building(1, 10, 2)

# lähetetään hissi numero 0 kerrokseen 7
building.run_elevator(0, 7)

# lähetetään hissi numero 1 kerrokseen 3
building.run_elevator(1, 3)

# palautetaan hissi numero 0 kerrokseen 1
building.run_elevator(0, 1)