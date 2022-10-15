import pandas as pd

df = pd.read_csv('data/Womens Clothing E-Commerce Reviews.csv')
print(df.head())

# df.to_json('data/Womens Clothing E-Commerce Reviews.json')

# df.to_excel('data/Womens Clothing E-Commerce Reviews.xlsx')



# def load_dataframe(path="Womens Clothing E-Commerce Reviews.csv"):
#     df = pd.read_csv('data/Womens Clothing E-Commerce Reviews.csv')
#     print(df.head())