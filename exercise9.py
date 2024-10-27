# Python object-oriented exercises
import random
# Question 1
#Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled
# distance. Add a class initializer that sets the first two of the properties based on parameter values. The current
# speed and travelled distance of a new car must be automatically set to zero. Write a main program where you create a
# new car (registration number ABC-123, maximum speed 142 km/h). Finally, print out all the properties of the new car.
'''
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed =0
        self.travelled_distance = 0

    def __str__(self):
        return (f'Registration number: {self.registration_number} '
                f'Maximum  speed : {self.maximum_speed} km/h '
                f'current speed : {self.current_speed} km/h '
                f'travelled distance: {self.travelled_distance} km')

    def get_registration_number(self, registration_number):
        return self.registration_number

    def get_maximum_speed(self, maximum_speed):
        return self.maximum_speed



new_car = Car("ABC-123", 142)
print(str(new_car))


# Question2
# Extend the program by adding an accelerate method into the new class. The method should receive the change of speed
# (km/h) as a parameter. If the change is negative, the car reduces speed. The method must change the value of the speed
# property of the object. The speed of the car must stay below the set maximum and cannot be less than zero. Extend the
# main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h. Then
# print out the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h change on the speed
# and then print out the final speed. The travelled distance does not have to be updated yet.


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed =0
        self.travelled_distance = 0

    def __str__(self):
        return (f'Registration number: {self.registration_number} '
                f'Maximum  speed : {self.maximum_speed} km/h '
                f'current speed : {self.current_speed} km/h '
                f'travelled distance: {self.travelled_distance} km')


    def accelerate(self, speed):
        self.current_speed += speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0



new_car = Car("ABC-123", 142)
print(str(new_car))


new_car.accelerate(30)
print(f'The current speed after increased by speed +30 km/h : {new_car.current_speed}')
new_car.accelerate(70)
print(f'The current speed after increased by speed +70km/h : {new_car.current_speed}')
new_car.accelerate(50)
print(f'The speed of car after increased by speed +50 : {new_car.current_speed}')
new_car.accelerate(-200)
print(f'The speed of car after breaking -200km/h : {new_car.current_speed}')

'''

#Question 3

#Again, extend the program by adding a new drive method that receives the number of hours as a parameter. The method
# increases the travelled distance by how much the car has travelled in constant speed in the given time. Example: The
# travelled distance of car object is 2000 km. The current speed is 60 km/h. Method call car.drive(1.5) increases the
# travelled distance to 2090 km.

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



new_car = Car("ABC-123", 142)
#accelerate
new_car.accelerate(30)
print(f" Current speed after accelerating +30km/h : {new_car.current_speed}")
new_car.accelerate(70)
print(f" Current speed after accelerating +70km/h : {new_car.current_speed}")
new_car.accelerate(50)
print(f"Current speed after accelerating +50km/h : {new_car.current_speed}")
# brake
new_car.accelerate(-200)
print(f"Current speed after accelerating -200km/h : {new_car.current_speed}")
# Travelled distance covered by driving
new_car.drive(1.5)
print(f"Travelled distance after driving 1.5 hours: {new_car.travelled_distance} km")


#Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginning of the
#main program, create a list that consists of 10 car objects created using a loop. The maximum speed of each new car
# is a random value between 100 km/h and 200 km/h. The registration numbers are created as follows: "ABC-1", "ABC-2"
# and so on. Now the race begins. One per every hour of the race, the following operations are performed:

# The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This
# is done using the accelerate method.
# Each car is made to drive for one hour. This is done with the drive method.
# The race continues until one of the cars has advanced at least 10,000 kilometers. Finally, the properties of each
# car are printed out formatted into a clear table.

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed =0
        self.travelled_distance = 0

    def __str__(self):
        return (f'Registration number: {self.registration_number} '
                f'Maximum  speed : {self.maximum_speed} km/h '
                f'current speed : {self.current_speed} km/h '
                f'Travelled distance: {self.travelled_distance} km')

    def accelerate(self, change_speed):
        self.current_speed += change_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0


    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


cars=[]
for i in range (1,11):
    registration_number=f'ABC-{i}'
    maximum_speed = random.randint(100,200)
    car = Car(registration_number, maximum_speed)
    cars.append(car)

race_ongoing = True
while race_ongoing:
    for car in cars:
        change_speed=random.randint(-10 , 15)
        car.accelerate(change_speed)
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_ongoing = False
            break

print(f" Registration \ total max_speed\ total current speed\ total travelled distance")
print("-" * 60)
for car in cars:
    print(car)


















