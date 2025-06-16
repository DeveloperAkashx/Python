num1 = int(input("Enter Num 1st: "))
num2 = int(input("Enter Num 2nd: "))
num3 = int(input("Enter Num 3rd: "))

if(num1>num2>num3):
    print(num1)
elif(num1<num2<num3):
    print(num3)
else:
    print(num2)