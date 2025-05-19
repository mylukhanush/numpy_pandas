# import pandas as pd
# x = {'cars': ["BMW", "VOLVO", "FORD"],    'parking slot': [3, 7, 2]}
# y = pd.DataFrame(x)
# print(y)
# print(pd. __version__)

#Series
#a pandas series is like a column in a table
#it is one dimensional array holding data of any type
# import pandas as pd
# a = [1, 7, 2]
# myvar = pd.Series(a)
# print(myvar)
# print(myvar[1])

# import pandas as pd
# a = [1, 7, 2]
# myvar = pd.Series(a, index = ["x", "y", "z"])
# print(myvar)
# print(myvar["y"])

#Key/Value Objects as Series
# import pandas as pd
# a = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(a)
# print(myvar)
# print(myvar["day2")

#DATA FRAME
#Create a DataFrame from two Series
# import pandas as pd
# data = { "calories": [420, 380, 390],"duration": [50, 40, 45]}
# myvar = pd.DataFrame(data)
# print(myvar)

#Locate Row
# import pandas as pd
# data = {"calories": [420, 380, 390],"duration": [50, 40, 45]}
# df = pd.DataFrame(data)
# print(df)
# print(df.loc[1])

#Named Indexes
# import pandas as pd
# data = {"calories": [420, 380, 390],"duration": [50, 40, 45]}
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# print(df)

#Locate Named Indexes
# import pandas as pd
# data = {"calories": [420, 380, 390],"duration": [50, 40, 45]}
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# print(df)
# print(df.loc["day2"])

# import pandas as pd
# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }
# df = pd.DataFrame(data)
# print(df)