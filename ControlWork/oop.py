# инкапсуляция
class Person:
    def __init__(self):
        self.__age = 0

    def set_age(self, age):

        if age >= 0:
            self.__age = age
        else:
            print("Ошибка: Возраст не может быть отрицательным.")

    def get_age(self):
        return self.__age

p = Person()
p.set_age(25)
print(f"Возраст: {p.get_age()}")

# Проверка
p.set_age(-5)
print(f"Текущий возраст: {p.get_age()}")


# Наследование
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

dog = Dog("Buddy")
cat = Cat("Kitty")

print(f"{dog.name} {dog.speak()}")
print(f"{cat.name} {cat.speak()}")

# Полиморфизм
class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move_vehicle(vehicle):
    return vehicle.move()

# Пример использования:
car = Car()
bike = Bicycle()

print(move_vehicle(car))
print(move_vehicle(bike))


# Абстракция
import abc
import math

class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Пример использования:
rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())
print(circle.area())



