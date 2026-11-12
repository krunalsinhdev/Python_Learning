# Method Overriding
# A child class can replace a method inherited from its parent class.

class Vehicle:
    def start(self):
        print("Vehicle is starting.")

class Car(Vehicle):
    def start(self):
        print("Car engine started.")

vehicle = Vehicle()
car = Car()

vehicle.start()
car.start()
