list = [1,"abc","abc",1]

newlist = list.copy()
newlist.reverse()

print(newlist)

if(list == newlist):
    print("List is Palindrone")
else:
    print("List is not Palindrone")