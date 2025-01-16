import re

# Search - check string start with "The" and End with "Spain"

txt = "The rain in Spain"

x = re.search("^The.*Spain$",txt)

if x:
    print("Yes, We have a match!")

else:
    print("No Match Found!")


# My Example
    
txt = "Three types of Freedom - Financial , Time , Location. defined by Akash"

x = re.search("Freedom",txt)

if x:
    print("Yes, match is Found!")

else:
    print("No match Found")
          


# Find - Find word/character using findall() function
    
txt = "The rain in Spain"

x = re.findall("ai",txt)

print(x)

x = re.findall("india",txt)

print(x)

# My Example

txt = "Three types of Freedom - Financial , Time , Location. defined by Akash"

x = re.findall("Akash",txt)

print(x)


# Split() Function 

txt = "The rain in Spain"

x = re.split("\s",txt)

print(x)

x = re.split("\s",txt,1)

print(x)

# My Example 

txt = "Three types of Freedom - Financial , Time , Location. defined by Akash"

x = re.split("\s",txt)

print(x)



# sub() Function - to replace elements

txt = "The rain in Spain"

x = re.sub("\s","8",txt)

print(x)

x = re.sub("\s","_",txt,2)  # To how many times you want add "_"

print(x)

# My Example

txt = "Three types of Freedom - Financial , Time , Location. defined by Akash"

x = re.sub("\s","_",txt)

print(x)