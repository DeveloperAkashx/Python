import pandas as pd

Data = {'A':[1,2,3,4,5],'B':[6,7,8,9,10]}
info = pd.DataFrame(Data)
# print(info['A'])

# print(info['B'])

# print(info[info['A']>2])
# print(info[info['A']<4])

info['Sum']= info['A'] + info['B']
print(info['Sum'])