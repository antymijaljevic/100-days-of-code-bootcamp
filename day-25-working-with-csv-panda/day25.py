# pip3 install pandas
# https://pandas.pydata.org/docs/reference/index.html
# https://pandas.pydata.org/docs/

from csv import reader
from pandas import read_csv

FILE = "weather_data.csv"
# normal
with open(FILE) as file:
    data = file.readlines()
    print(data)

# with csv library
with open(FILE) as data:
    data = reader(data)
    temperatures = []
    
    # get temp list
    for row in data:
        if row[1].isdigit():
            temperatures.append(int(row[1]))
        
    print(temperatures)
    
    
# with pandas
data = read_csv(FILE)

# entire doc
print(data)

# column
print(data["temp"])