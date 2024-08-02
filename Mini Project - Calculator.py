# Mini Project - Calculator

first = input("Enter the First Number : ")
operator = input("Enter the operator (+,-,*,/,%) : ")
second = input("Enter the Second Number : ")

first = int(first)
second = int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("Invalid Operator")