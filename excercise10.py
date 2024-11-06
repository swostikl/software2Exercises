'''

# question on 1
#Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters. The elevator
# has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor. If you make elevator
#h for example the method call h.go_to_floor(5), the method calls either the floor_up or floor_down methods as many times
#as it needs to get to the fifth floor. The methods run the elevator one floor up or down and tell what floor the elevator
# is after each move. Test the class by creating an elevator in the main program, tell it to move to a floor of your
# choice and then back to the bottom floor.

class Elevator:
    def __init__(self, bottom_floor,top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"elevator is now on {self.current_floor} floor")

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        print(f"elevator is now on {self.current_floor} floor")



    def go_to_floor(self, target_floor):
        if target_floor>self.top_floor or target_floor<self.bottom_floor:
            print(f"There is no such floor {target_floor}.")
            return

        while self.current_floor< target_floor:
            self.floor_up()
        while self.current_floor>target_floor:
            self.floor_down()



h=Elevator(0,5)
h.go_to_floor(4)
h.go_to_floor(2)
h.go_to_floor(5)
h.go_to_floor(6)

#Question no 2
#Extend the previous program by creating a Building class. The initializer parameters for the class are the numbers of
#the bottom and top floors and the number of elevators in the building. When a building is created, the building creates
# the required number of elevators. The list of elevators is stored as a property of the building. Write a method called
# run_elevator that accepts the number of the elevator and the destination floor as its parameters. In the main program,
# write the statements for creating a new building and running the elevators of the building.


class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"elevator is now on {self.current_floor} floor")

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        print(f"elevator is now on {self.current_floor} floor")

    def go_to_floor(self, target_floor):
        if target_floor > self.top_floor or target_floor < self.bottom_floor:
            print(f"There is no such floor {target_floor}.")
            return

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self,elevator_number,destination_floor):
        if elevator_number < 0 or elevator_number >= len(self.elevators):
            print(f" There is no such elevator {elevator_number}!")
            return
        self.elevators[elevator_number].go_to_floor(destination_floor)

building = Building(0,5,5)
building.run_elevator(1,4)
building.run_elevator(0,3)
building.run_elevator(0,0)

#Q.NO.3
#Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators to
# the bottom floor. Continue the main program by causing a fire alarm in your building.

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"elevator is now on {self.current_floor} floor")

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        print(f"elevator is now on {self.current_floor} floor")

    def go_to_floor(self, target_floor):
        if target_floor > self.top_floor or target_floor < self.bottom_floor:
            print(f"There is no such floor {target_floor}.")
            return

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self,elevator_number,destination_floor):
        if elevator_number < 0 or elevator_number >= len(self.elevators):
            print(f" There is no such elevator {elevator_number}!")
            return
        self.elevators[elevator_number].go_to_floor(destination_floor)

    def fire_alarm(self):
        print(f"Fire alarm is activated! Moving all elevator to bottom floor ")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)

building = Building(0,5,5)
building.run_elevator(1,4)
building.run_elevator(0,3)
building.run_elevator(0,0)
#fire alarm
building.fire_alarm()
'''




#Quetion number 4

import random
from tabulate import tabulate
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed =0
        self.travelled_distance = 0

    def accelerate(self, change_speed):
        self.current_speed += change_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed=0

    def drive(self, hour):
        self.travelled_distance += self.current_speed * hour

    def __str__(self):
        return (f'Registration number: {self.registration_number} '
                f'Maximum  speed : {self.maximum_speed} km/h '
                f'current speed : {self.current_speed} km/h '
                f'travelled distance: {self.travelled_distance} km')


class Race:
    def __init__(self,name, distance, car_list):
        self.name = name
        self.distance = distance
        self.cars = car_list

    def hour_passes(self):
        for car in self.cars:
            speed_change=random.randint(-10,15)
            car.accelerate(speed_change)
            car.drive(1) # drive for 1 hour

    def print_status(self):
        car_data=[]
        for car in self.cars:
            car_data.append([car.registration_number, car.maximum_speed, car.current_speed, car.travelled_distance])

        headers = ["Registration Number", "Maximum Speed", "Current Speed", "Travelled Distance"]
        print(f'The table is given below: \n{(tabulate(car_data, headers=headers, tablefmt="fancy_grid"))}')

    def race_finish(self):
        # return true if car has reached or exceeded the race
        return any(car.travelled_distance > self.distance for car in self.cars)


def main():
    cars=[Car(f"ABC-{i+1}", random.randint(100,200)) for i in range (10)]
    #create a race
    race=Race("Grand Demolition deploy",8000,cars)

    #stimulate race
    hours_passed=0
    while not race.race_finish():
        race.hour_passes()
        hours_passed+=1
        #print the status every 10 hours
        if hours_passed % 10 ==0:
            print(f"\n Status at hour {hours_passed}")
            race.print_status()

    #print final status
    print("\n Final Status")
    race.print_status()
    print(f"Race finished after {hours_passed} hours")

main()

