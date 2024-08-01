import pandas as pd     # To Handling Missing Data

info = pd.DataFrame({'A':[1,2,None],'B':[4,None,6]})
print(info.isnull())

info.fillna(0, inplace=True)   # To Filling Missing Data

info.dropna(inplace=True)      # To Dropping Missing Data