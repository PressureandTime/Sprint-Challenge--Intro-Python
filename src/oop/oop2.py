# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class Vehicle:
    def __init__(self):
        pass


class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass



class GroundVehicle(Vehicle):
    def __init__(self, num_wheels=4):
        super().__init__()
        self.num_wheels = num_wheels

    def drive(self):
        return "vrooooom"


class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels):
        super().__init__(num_wheels)
        self.num_wheels = num_wheels

    def drive(self):
        return "BRAAAP!!"


honda = Motorcycle(2)
print(honda)


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO

vehicles = [
    GroundVehicle(3),
    GroundVehicle(4),
    Motorcycle(5),
    GroundVehicle(6),
    Motorcycle(7),
]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO

for vehicle in vehicles:
    print(vehicle.drive())
