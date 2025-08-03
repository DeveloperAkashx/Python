class Student:
    college_name = "DKTE"

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Akash",20)
print(s1.name, s1.age, s1.college_name)

s2 = Student("Viraj",18)
print(s2.name, s2.age, s2.college_name)