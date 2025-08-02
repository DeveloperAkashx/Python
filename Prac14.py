myFile = open("Practice.txt","a")

myFile.write("\nHi everyone\nWe are learning File Handling I/O\nusing python\nI like programming in python")


myFile = open("Practice.txt")

data = myFile.read()
newData = data.replace("python","JavaScript")
myFile.close()

myFile = open("Practice.txt","w")
myFile.write(newData)
myFile.close()