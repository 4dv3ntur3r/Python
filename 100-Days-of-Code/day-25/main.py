# import csv
import pandas
import math

# with open("./weather_data.csv") as weather_txt:
#     data = csv.reader(weather_txt)
#     tempretures = []
#     for item in data:
#         print(item)
#         if item[1] != 'temp':
#             tempretures.append(int(item[1]))
# print(tempretures)

# data = pandas.read_csv("./weather_data.csv")
# print(type(data))

# temp_list = data["temp"].to_list()

# avg = sum(temp_list)/len(temp_list)

# print(data["temp"].mean())
# print(data["temp"].max())

# Get data in a column
# data["condition"]
# data.condition

# get data in a Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp_F = (int(monday.temp) * 9 / 5) + 32
# print(monday_temp_F)

# data frame from scratch

# data_dict = {
#     "student": ["Amy", "Leo", "John"],
#     "scores": [45, 54, 67],
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("New_data.csv")

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_column = data["Primary Fur Color"]

gray_colored = len(data[color_column == "Gray"])
cinnamon_colored = len(data[color_column == "Cinnamon"])
black_colored = len(data[color_column == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_colored, cinnamon_colored, black_colored]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count")