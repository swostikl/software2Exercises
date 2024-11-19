#Question no 1
#Implement the following class hierarchy using Python: A publication can be either a book or a magazine.Each publication
# has a name. Each book also has an author and a page count, whereas each magazine has a chief editor. Also write the
# required initializers to both classes. Create a print_information method to both subclasses for printing out all
# information of the publication in question. In the main program, create publications Donald Duck (chief editor Aki
# Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages). Print out all information of both publications using
# the methods you implemented.

class Publication:
    def __init__(self,name):
        self.name = name

class Book(Publication):
    def __init__(self,name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book name: {self.name}")
        print(f"Author name: {self.author}")
        print(f"Page count: {self.page_count}")


class Magazine(Publication):
    def __init__(self,name,chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine name: {self.name}")
        print(f"Chief_editor name: {self.chief_editor}")

donald_duck=Magazine("Donald Duck","Aki Hyyppiä")
compartment_no_6=Book("Comparment No. 6","Rosa Liksom",192)

donald_duck.print_information()
print()
compartment_no_6.print_information()

#question no 2
#Extend the previously written Car class by adding two subclasses: ElectricCar and GasolineCar. Electric cars have the
# capacity of the battery in kilowatt-hours as their property. Gasoline cars have the volume of the tank in liters as
# their property. Write initializers for the subclasses. For example, the initializer of electric cars receives the
# registration number, maximum speed and battery capacity as its parameter. It calls the initializer of the base class
# to set the first two properties and then sets its capacity. Write a main program where you create one electric car
# (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l). Select speeds for both cars, make them
# drive for three hours and print out the values of their kilometer counters.

class Car:
    def __init__(self,registration_number,max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self,speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self,hours):
        self.travelled_distance += self.current_speed * hours

    def __str__(self):
        return (f"{self.registration_number}  "
                f"{self.max_speed} km/h  "
                f"{self.current_speed} km/h  "
                f"{self.travelled_distance} km  ")

class ElectricCar(Car):
    def __init__(self,registration_number,max_speed, battery_capacity):
        super().__init__(registration_number,max_speed)
        self.battery_capacity = battery_capacity

    def __str__(self):
        return (f" Electric Car is :  {super().__str__()}  "
                f"Battery capacity : {self.battery_capacity} kWh")


class GasolineCar(Car):
    def __init__(self,registration_number,max_speed, tank_volume):
        super().__init__(registration_number,max_speed)
        self.tank_volume = tank_volume

    def __str__(self):
        return (f" Gasoline Car is :  {super().__str__()}  "
                f"Tank volume : {self.tank_volume} litres")

# creating  cars for both
electric_car=ElectricCar('ABC-15',180,52.5)
gasoline_car=GasolineCar('ACD-123',165,32.3)


# set speed for cars
electric_car.accelerate(80) #set max_speed
gasoline_car.accelerate(60) #set max speed

# drive for 3 hours
electric_car.drive(3)
gasoline_car.drive(3)

#print out values
print(f"Title: "," Registration_number  ", "max_speed  ", "current_speed  ", "travelled_distance  " ," xxx ")
print(f"-" * 100)
print(electric_car)
print(gasoline_car)









