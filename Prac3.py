class Student:
    college_name = "DKTE"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_info(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"College = {self.college_name}")


s1 = Student("Akash",20)
s1.student_info()

s2 = Student("Viraj",18)
s2.student_info()

s3 = Student("Nik", 20)
s3.student_info()