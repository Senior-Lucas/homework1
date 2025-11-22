class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self.__name = new_name
        else:
            print("Ошибка: Имя должно быть непустой строкой.")

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age >= 0:
            self.__age = new_age
        else:
            print("Ошибка: Возраст должен быть целым положительным числом.")

    def make_sound(self):
        return "Неизвестный звук"

class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"

class Cat(Animal):
    def make_sound(self):
        return "Мяу-мяу!"

dog = Dog(name="Шарик", age=3)
cat = Cat(name="Барсик", age=5)

print(f"Изначальные данные:")
print(f"Собака: Имя - {dog.get_name()}, Возраст - {dog.get_age()} года")
print(f"Кошка: Имя - {cat.get_name()}, Возраст - {cat.get_age()} лет")
print("-" * 20)

# это демонстрация полиморфизма
print(f"{dog.get_name()} говорит: {dog.make_sound()}")
print(f"{cat.get_name()} говорит: {cat.make_sound()}")
print("-" * 20)

dog.set_name("Рекс")
dog.set_age(4)
cat.set_age(6)
cat.set_name("")

print(f"Данные после изменения через сеттеры:")
print(f"Собака: Имя - {dog.get_name()}, Возраст - {dog.get_age()} года")
print(f"Кошка: Имя - {cat.get_name()}, Возраст - {cat.get_age()} лет")