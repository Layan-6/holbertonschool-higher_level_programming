#!/usr/bin/env python3
"""Task 0: Abstract Animal Class and its Subclasses"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class representing an Animal"""
    
    @abstractmethod
    def sound(self):
        """Abstract method that should return the animal's sound"""
        pass

class Dog(Animal):
    """Dog class that implements the Animal interface"""
    
    def sound(self):
        """Returns the sound a dog makes"""
        return "Bark"

class Cat(Animal):
    """Cat class that implements the Animal interface"""
    
    def sound(self):
        """Returns the sound a cat makes"""
        return "Meow"
