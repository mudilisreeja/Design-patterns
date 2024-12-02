class car:
    def type(self):
        pass
class mercedes(car):
    def type(self):
        return mercedes
class swift(car):
    def type(self):
        return swift
class Bike:
    def type(self):
        pass
class SportsBike(Bike):
    def type(self):
        return SportsBike
class Activa(Bike):
    def type(self):
        return Activa
class Vehicle_Factory:
    def create_car(self):
        pass
    def create_bike(self):
        pass
class LuxuryVehicleFactory(Vehicle_Factory):
    def create_car(self):
        return mercedes()
    def create_bike(self):
        return SportsBike()
class EconomicalVehicleFactory(Vehicle_Factory):
    def create_car(self):
        return swift()
    def create_bike(self):
        return Activa()

luxury_factory = LuxuryVehicleFactory()
luxury_car=luxury_factory.create_car()
luxury_bike=luxury_factory.create_bike()
print(luxury_bike.type())
print(luxury_car.type())






