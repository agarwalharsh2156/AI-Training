from dataclasses import dataclass

# You use dataclass decorator in python when you want to create a very simple data structure
# @dataclass gives you the boilerplate functions already defined like __init__().
# minimizes writing a lot of boilerplate code when you want a class to store some data.

@dataclass
class Student:
    name:str
    div:str
    birth_date:str

    # You can create your own functions too and @dataclass doesn't restrict you from that.
    def data(self):
        print(f"Name: {self.name}\nDivision: {self.div}\nBirth Date: {self.birth_date}")

student = Student("Harsh", "A", "15/08/2004")

# Printing everything by accessing the instance variables directly.
print("Name - ", student.name)
print("Div - ", student.div)
print("Birth Date - ", student.birth_date)

# Printing using the method of object instance created for Student class
student.data()
