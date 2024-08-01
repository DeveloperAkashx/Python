import pandas as pd

student = {"Name":['Akash','Sujal','Aneesh'],"PRN":[22087,22072,22088]}
info = pd.DataFrame(student)
print(info)

grouped = info.groupby('Name').sum()
print(grouped)