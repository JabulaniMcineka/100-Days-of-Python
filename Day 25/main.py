# with open("Day 25/weather_data.csv") as data_file:
#     data = data_file.readlines()
# weather_data = []
# for line in data:
#     weather_data.append(line.strip().split(",")) 
# print(weather_data)       


import csv

# with open("Day 25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))

#     print(temperature)

import pandas


# data = pandas.read_csv("Day 25/weather_data.csv")
#print(type(data))
# print(data["temp"])

# calc_avg = data["temp"].mean()
# print(calc_avg)

# calc_max = data["temp"].max()
# print(calc_max)

# #get data in columns
# print(data["condition"])
# print(data.condition)

# #get data in rows
# print(data[data.day == "Monday"])       

# #get row with max temp
# print(data[data.temp == data.temp.max()])   

#convert monday temp to fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)


# #create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("Day 25/new_data.csv")




data = pandas.read_csv("Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])    
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]

}


data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("Day 25/squirrel_counts.csv")
