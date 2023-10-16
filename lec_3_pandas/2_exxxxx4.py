import pandas as pd

games = pd.read_csv('ex3.csv', sep=";")
print(games)

games_clear = games.dropna()
print()
print(games_clear)

games_fill = games.fillna(8)

print()
print(games_fill)

games["Rating"].fillna("8", inplace = True)
games["Weight"].fillna(5.8, inplace = True)

print(games)
print(games.info())
print(games.shape)

