# -*- coding: utf-8 -*-
"""
Created on Wed May 27 08:52:24 2020

@author: barbora
"""

# Creating classes
print("\nCreating a class")
class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialise name and age attributes."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# Making an instance out of the class
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

# Making another instance
your_dog = Dog('Lucy', 3)
print(f"My dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")
your_dog.sit()


# Modifying attributes of an instance
print("\n")
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialise attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
my_new_car = Car('audi','a4', 2019)
print(my_new_car.get_descriptive_name())


# Adding in an attribute that changes over time
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialise attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi','a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


# Modifying an attribute's value directly
print("\nModifying an attribute's values directly")
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modying an attribute's value through a method
print("\nModifying an attribute's value through a method")
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialise attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

my_new_car = Car('audi','a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()


# Extension to example above
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialise attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_new_car = Car('audi','a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.update_odometer(10)
my_new_car.read_odometer()


# Incrementing an attribute's value through a method
print("\nIncrementing an attribute's value through a method")
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialise attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


# Inheritance - create ElectricCar child class based on Car parent class
print("\nInheritance")
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialise attributes of the parent class."""
        super().__init__(make, model, year)
        
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())


# Defining attributes and methods for child class
print("\nDefiniting attributes and methods for child class")
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialise attributes of the parent class.
        Then initialise attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# Overriding methods from parent class - same method name, different code
print("\nOverriding methods from parent class")
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialise attributes of the parent class.
        Then initialise attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")


# Instances as attributes - when classes get lengthy > split into smaller 
# classes
print("\nInstances as attributes")
class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialise the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialise attributes of the parent class.
        Then initialise attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()


# Extending example above
class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialise the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
        
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialise attributes of the parent class.
        Then initialise attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# Importing a single class
print("\nImporting")
from c9_examples_car import CarModule

my_new_car = CarModule('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# Importing another class from same module
from c9_examples_car import ElectricCarModule

my_tesla_module = ElectricCarModule('tesla', 'model s', 2019)
print(my_tesla_module.get_descriptive_name())
my_tesla_module.battery.describe_battery()
my_tesla_module.battery.get_range()


# Importing multiple classes from a module
from c9_examples_car import CarModule, ElectricCarModule

my_beetle_module = CarModule('volkswagen', 'beetle', 2019)
print(my_beetle_module.get_descriptive_name())

my_tesla_module = ElectricCarModule('tesla', 'roadster', 2019)
print(my_tesla_module.get_descriptive_name())


# Importing an entire module
import c9_examples_car

my_beetle_module = c9_examples_car.CarModule('volkswagen', 'beetle', 2019)
print(my_beetle_module.get_descriptive_name())

my_tesla_module = c9_examples_car.ElectricCarModule('tesla', 'roadster', 2019)
print(my_tesla_module.get_descriptive_name())


# Importing all classes from a module - not recommended
from c9_examples_car import *

my_beetle_module = CarModule('volkswagen', 'beetle', 2019)
print(my_beetle_module.get_descriptive_name())


# Importing a module into a module
from c9_examples_gascar import CarModule
from c9_examples_electriccar import ElectricCarModule

my_beetle_module = CarModule('volkswagen', 'beetle', 2019)
print(my_beetle_module.get_descriptive_name())

my_tesla_module = ElectricCarModule('tesla', 'roadster', 2019)
print(my_tesla_module.get_descriptive_name())


# Using aliases
from c9_examples_electriccar import ElectricCarModule as ECM

my_tesla_module = ECM('tesla', 'roadster', 2019)
print(my_tesla_module.get_descriptive_name())


# Python standard library
print("\nUsing Python standard library")

# Use randint() to get a random integer between two integers
from random import randint
print(randint(1, 6))

# Use choice() to randomly select an element from a list or tuple
from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)
