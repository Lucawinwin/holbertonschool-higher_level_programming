#!/usr/bin/python3
"""
Import the necessary components from the abc module
"""

from abc import ABC, abstractmethod

"""
Define the Animal class, ensuring it inherits from ABC to mark it as abstract
"""


class Animal(ABC):
    """
    Abstract class Animal that requires subclasses to implement
    the sound method.
    """


    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Dog is a subclass of Animal that implements the sound method.
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Cat is a subclass of Animal that implements the sound method.
    """
    def sound(self):
        return "Meow"
