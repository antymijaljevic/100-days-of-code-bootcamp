from pandas import read_csv, DataFrame


data_frame = read_csv("weather_data.csv")
series = data_frame["temp"]

# print(type(data_frame), type(series))

data_dict = data_frame.to_dict()
print(data_dict)

temp_list = series.to_list()
print(temp_list)

# get average temp my version
sum_all = 0
count = 0

for temp in temp_list:
    sum_all += temp
    count += 1
    
average_temp = sum_all / count
print(average_temp)


# her version
average = sum(temp_list) / len(temp_list)
print(average)

# pandas method
print(series.mean())
print(series.max())

# get data in column
print(data_frame["condition"])
print(data_frame.condition)

# get data in row
print(data_frame[data_frame.day == "Monday"])

# get row where temp is max
print(data_frame[data_frame.temp == data_frame.temp.max()])

# get condition from monday
monday = data_frame[data_frame.day == "Monday"]
print(monday.condition)


# challenge
print("\n\n\n")
"""
    To convert Celsius to Fahrenheit, you can use the following formula:
    °F = (°C x 1.8) + 32
"""

monday = data_frame[data_frame.day == "Monday"]
mon_temp = monday.temp
in_fah = (int(mon_temp) * 1.8) + 32
print(in_fah)

# create a data_frame from scratch
data_dict = {
    "students": ["Mate", "Stipe", "Pero"],
    "scores": [22, 11, 32]
}

data = DataFrame(data_dict)
print(data)

# save to csv
data.to_csv("new_data.csv")