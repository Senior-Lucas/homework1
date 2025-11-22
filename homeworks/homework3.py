class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    def get_occupation(self):
        return self.__occupation

    def has_higher_education(self):
        return self.__higher_education

    def introduce(self):
        education_status = "have higher education" if self.__higher_education else "don't have higher education"
        print(f"Hello! My name is {self.name}. I am {self.__occupation}, I was born in {self.birth_date}, and I {education_status}.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        education_status = "есть высшее образование" if self.has_higher_education() else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.get_occupation()}. "
              f"Я учился с Айсулуу в группе {self.group}. У меня {education_status}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        education_status = "есть высшее образование" if self.has_higher_education() else "нет высшего образования"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.get_occupation()}. "
              f"Мое хобби {self.hobby}. У меня {education_status}.")




person1 = Person("Lucas", "10.10.1999", "Dantist", True)
person2 = Person("Bob", "09.06.1987", "engineer", True)
person3 = Person("Alex", "15.05.2003", "desiner", False)

person1.introduce()
person2.introduce()
person3.introduce()


cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
cl1.introduce()
fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")


class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def validate_phone_number(phone_number):
        return len(str(phone_number)) == 10 and str(phone_number).isdigit()


class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            new_contact = Contact(name, phone_number)
            cls.all_contacts.append(new_contact)
            print(f"Контакт '{name}' успешно добавлен.")
        else:
            raise ValueError("Некорректный номер телефона. Номер должен содержать ровно 10 цифр.")

try:
    ContactList.add_contact("Иван", "1234567890")
except ValueError as e:
    print(e)

try:
    ContactList.add_contact("Петр", "123")
except ValueError as e:
    print(e)

try:
    ContactList.add_contact("Анна", "123a567890")
except ValueError as e:
    print(e)

print("\nСписок всех контактов:")
for contact in ContactList.all_contacts:
    print(f"Имя: {contact.name}, Телефон: {contact.phone_number}")

print(ContactList.all_contacts) # []

ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone)
    # Вася Пупкин 0700100200
    # Виктор Цой 0500123456

ContactList.add_contact("John Doe", "5551234") # Error
