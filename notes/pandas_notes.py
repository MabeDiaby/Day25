# with open("notes/weather_data.csv") as data_file:
#     data_weather = data_file.readlines()
#     print(data_weather)

# import csv

# with open("notes/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("notes/weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)
# temp_length = len(temp_list)

# print(sum(temp_list) / temp_length)
# print(type(data))
# print(data)

# get rows of data
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# print(monday_temp * 9 / 5 + 32)

# Create dara frame from scratch
data_dict = {
    "students": ["Amy", "James", "Anegla"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
