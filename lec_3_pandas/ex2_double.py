import pandas as pd

games = pd.read_csv('ex3.csv', sep=";")

#print(games)

print(games.mean())
print(games.duplicated())
games.drop_duplicates(inplace = True)
print(games)

for x in games.index:
    if games["Rating"].loc[x] > 10:
        games.drop(x, inplace = True)