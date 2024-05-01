import pandas as pd





#create dataframe
fruitSales = pd.DataFrame({"Apples": [35, 41], "Bananas": [21, 34]},index=['2017 Sales', '2018 Sales'])

#verify data
print(fruitSales)

#write to csv
fruitSales.to_csv('fruit.csv')