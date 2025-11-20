from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        print("")


class Dog(Animal):
        def make_sound(self):
            print("gav gav")

class Cat(Animal):
        def make_sound(self):
            print("may may")
