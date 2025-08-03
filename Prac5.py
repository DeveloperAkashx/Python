class Student:

    
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks

    def student_info(self):
        print(f"Name = {self.name}")
        print(f"Marks = {self.marks}")

    @staticmethod

    def avg(self):
        sum = 0
        for i in self.marks:
            sum += i
            avg = sum/3
            return avg

s1 = Student("Akash",[90,80,70])
ans = s1.avg()

print(f"{s1.name}s avg marks is {ans}")
