text1 = "Python is a great programming language"
text2 = "Many developers love the Python language"

set1 = set(text1.split())
set2 = set(text2.split())

set3 = set1.intersection(set2)
print(set3)

set4 = set1.union(set2)
print(set4)

unique = set4.difference(set3)
print(unique)

print(len(unique))