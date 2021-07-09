# Liskov Substitution Principle

# Objects in a program should be replaceable with instances of their subtypes
# without altering the correctness of that program
'''
As we can see here, we are trying to loop through a list of car objects.
And here we break the Liskov Substitution principle as
we cannot replace Super type Car’s objects with objects of Sub type PetrolCar in the function written to find Red cars.
'''
# from dataclasses import dataclass
#
#
# @dataclass
# class Car:
#     type: str
#
#
# @dataclass
# class PetrolCar(Car):
#     type: super(type)
#
#
# car = Car("SUV")
# car.properties = {"Color": "Red", "Gear": "Auto", "Capacity": 6}
#
# petrol_car = PetrolCar("Sedan")
# petrol_car.properties = ("Blue","Manual",4)
#
# cars = [car, petrol_car]
# print(cars)
#
#
# def find_red_cars(carlist):
#     redc = [i+1 for i,red_cars in enumerate(carlist) if red_cars.properties['Color']=='Red']
#     print(redc)
#
# find_red_cars(cars)

# Objects in a program should be replaceable with instances of their subtypes
# without altering the correctness of that program
'''
A better way to implement this would be to introduce setter and getter methods in the Super class Car 
using which we can set and get Car’s properties without leaving that implementation to individual developers. 
This way we just get the properties through a setter method and its implementation remains internal to the Super class.
'''
from dataclasses import dataclass


@dataclass
class Car:
    type1: str

    def set_properties(self, color, gear, capacity):
        self.car_properties = {"Color" : color, "Gear": gear, "Capacity": capacity}

    def get_properties(self):
        return self.car_properties


@dataclass
class PetrolCar(Car):
    type1: str

car = Car("SUV")
car.set_properties("Red","Auto",6)
# car.properties = {"Color": "Red", "Gear": "Auto", "Capacity": 6}
#
petrol_car = PetrolCar("Sedan")
petrol_car.set_properties("Blue","Manual",4)
petrol_car1 = PetrolCar("Volvo")
petrol_car1.set_properties("Blue","Auto",4)
# petrol_car.properties = ("Blue","Manual",4)
#
carss = [car, petrol_car, petrol_car1]
print(carss)


def find_red_cars(carlist):
    # total = 0
    # redc = [i+1 for i,red_cars in enumerate(carlist) if red_cars.get_properties()['Color']=='Blue']
    # print(redc)
    red_cars = 0
    for car in carlist:
        if car.get_properties()['Color'] == "Blue":
            red_cars += 1
    print(f'Number of Red Cars = {red_cars}')

find_red_cars(carss)

