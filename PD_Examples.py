import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)

print(pd.__version__)

import pandas as pd

a = [3, 5, 9]

myvar = pd.Series(a)
print(myvar)

#---------------------------------------------------------------#

import pandas as pd 

a = [3,5,6]
myvar= pd.Series(a, index=["x", "y", "z"])

print(myvar)
print(myvar["x"])
print(myvar["y"])
print(myvar["z"])

#------------------------------------#

#import pandas as pd

calories = {"day1":300, "day2":400, "day3":380}
myvar= pd.Series(calories)
print(myvar)

# DATA FRAMES OF PANDAS :

data = {
    "calories" :  [350, 240, 345],
    "duration": [50, 40, 45]
}   
df = pd.DataFrame(data)
print(df)

# locate Row

print(df.loc[1])
print(df.loc[[0, 1]]) # 2 rows location

#----------------------------------------------#

# Named Indexes

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)
print(df.loc[["day2","day3"]]) # 2 rows location


# import csv files
'''
import pandas as pd

df = pd.read_csv('data.csv')

print(df)
'''

