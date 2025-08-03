#class & object

class Car:
    # brand = "BMW"

    def __init__(self):
        print("Student obj has been created")

    def start(self):
        print(self)

car1 = Car()
print(car1)

car1.start()