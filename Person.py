from datetime import date

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
        
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        
        if today  < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age
    
person1 = Person("John Smith", "France", date(2002, 8, 6))
person2 = Person("Setephen Curry", "USA", date(2003, 10, 7))
person3 = Person("Klay Thompson", "USA", date(2010, 5, 29))


print("Person 1:")
print("Name:", person1.name)
print("Country:", person1.country)
print("Date of Birth:", person1.date_of_birth)
print("Age:", person1.calculate_age())

print("\nPerson 2:")
print("Name:", person2.name)
print("Country:", person2.country)
print("Date of Birth:", person2.date_of_birth)
print("Age:", person2.calculate_age())

print("\nPerson 3:")
print("Name:", person3.name)
print("Country:", person3.country)
print("Date of Birth:", person3.date_of_birth)
print("Age:", person3.calculate_age())