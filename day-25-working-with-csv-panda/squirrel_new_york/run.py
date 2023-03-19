from pandas import read_csv, DataFrame

given_data = "2018.csv"
squirrel_df = read_csv(given_data)

gray_squirrels = len(squirrel_df[squirrel_df["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(squirrel_df[squirrel_df["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(squirrel_df[squirrel_df["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

new_csv = DataFrame(data_dict)
new_csv.to_csv("sorted_data.csv")