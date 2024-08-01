import pandas as pd

data = {'A':['Foo','bar','Too'],'B':[1,2,3]}
info = pd.DataFrame(data)
grouped = info.groupby('A').sum()
print(grouped)

new = info.pivot_table(values='B', index='A', aggfunc='sum')
print(new)