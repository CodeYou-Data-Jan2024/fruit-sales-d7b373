import pandas as pd

fruitsales = pd.DataFrame({"Apples": [35, 41], "Bananas": [21, 34]}, index=["2017 Sales", "2018 Sales"])
print(fruitsales)

fruitsales.to_csv("fruit.csv")
