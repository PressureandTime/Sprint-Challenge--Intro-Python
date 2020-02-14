# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    #super class or base class
    pass

class FlightVehicle(Vehicle):
    # subclass of Vehicle class
    pass


class Starship(FlightVehicle):
    # subclass of FlightVehicle class
    pass

class GroundVehicle(Vehicle):
    # subclass of Vehicle class
    pass


class Car(GroundVehicle):
    # subclass of GroundVehicle class
    pass


class Motorcycle(GroundVehicle):
    # subclass of GroundVehicle class
    pass


class Airplane(FlightVehicle):
    # subclass of FlightVehicle class
    pass
