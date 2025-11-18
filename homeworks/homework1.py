class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education_status = "have higher education" if self.higher_education else "dont have higher education"
        print(f"Hello! My name is {self.name}. I am {self.occupation}, i was birn in {self.birth_date}, and I {education_status}.")

person1 = Person("Lucas", "10.10.1999", "Dantist", True)
person2 = Person("Bob", "09.06.1987", "engineer", True)
person3 = Person("Alex", "15.05.2003", "desiner", False)

person1.introduce()
person2.introduce()
person3.introduce()