from Module12.Topic3.riderClass import Rider

'''
Program: vehicleClasses.py
Author: Reagan Zierke
Last date modified: 11/16/22

This program creates 3 classes for different vehicle types and each class inherits the abstract class of Rider. Driver code then creates 3 objects (1 from each class) and calls methods from each class.
'''

class Bike(Rider):

    def __init__(self):
        self.power = "Human powered, not enclosed"
        self.passengers = "1 or 2 if tandem or a daredevil"

    #required ride method
    def ride(self):
        return self.power

    #required riders method
    def riders(self):
        return self.passengers

    def __str__(self):
        return (f"{self.power}\n{self.passengers}")


class Motorcycle(Rider):

    def __init__(self):
        self.power = "Engine powered, not enclosed"
        self.passengers = "1 or 2"

    #required ride method
    def ride(self):
        return self.power

    #required riders method
    def riders(self):
        return self.passengers

    def __str__(self):
        return (f"{self.power}\n{self.passengers}")

class Car(Rider):

    def __init__(self):
        self.power = "Engine powered, enclosed"
        self.passengers = "1 plus comfortably"

    #required ride method
    def ride(self):
        return self.power

    #required riders method
    def riders(self):
        return self.passengers

    def __str__(self):
        return (f"{self.power}\n{self.passengers}")


if __name__ == "__main__":
    #creates objects
    my_bike = Bike()
    my_motorcycle = Motorcycle()
    my_car = Car()
    #calls methods
    print (f"Bike: {my_bike.ride()}")
    print (f"Bike: {my_bike.riders()}")
    print (f"Motorcycle: {my_motorcycle.ride()}")
    print (f"Motorcycle: {my_motorcycle.riders()}")
    print (f"Car: {my_car.ride()}")
    print (f"Car: {my_car.riders()}")

