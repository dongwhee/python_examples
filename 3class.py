# define vehicle
class Vehicle:
    def __init__(self, wheels=3):
        self.wheels = wheels
    def run(self):
        print 'Br' + 'o' * self.wheels + 'ng'

default = Vehicle()
default.run()

# define car
class Car(Vehicle):
    def __init__(self):
        self.wheels = 4

car = Car()
car.run()

# define car
class AutonomousCar(Car):
    def run(self):
        print 'Beep' * self.wheels

autonomous = AutonomousCar()
autonomous.run()
