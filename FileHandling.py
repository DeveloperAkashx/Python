#File handling

myFile = open("Demo.txt","r")

data = myFile.readline()
myFile.close()


print(data)