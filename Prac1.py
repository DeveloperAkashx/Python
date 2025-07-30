dict = {}

for i in range(3):
    sub = input("Enter Sub name : ")
    marks = int(input("Enter the marks: "))

    # dict[sub] = marks
    dict.update({sub: marks})
    
print(dict)
