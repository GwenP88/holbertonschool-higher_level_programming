#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""Abstract animal base class with Dog and Cat implementations"""


class Animal(ABC):
    """Abstract base class for animals"""
    @abstractmethod
    def sound(self):
        """Return the animal sound"""
        pass


class Dog(Animal):
    """Dog implementation of Animal"""
    def sound(self):
        """Return sound of dog"""
        return "Bark"


class Cat(Animal):
    """Cat implementation of Animal."""
    def sound(self):
        """Return sound of cat"""
        return "Meow"
