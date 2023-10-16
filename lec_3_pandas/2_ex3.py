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

print()
print(games)

print(games.mean())
#brak ratigu?

games['Rating'] = pd.to_numeric(games['Rating'])
print(games.mean())

print(games.duplicated())

games.drop_duplicates(inplace = True)

print(games)

for x in games.index:
    if games["Rating"].loc[x] > 10:
        games.drop(x, inplace = True)

print(games)
print(games.mean())
print(games.corr())

games[["Rating", "Weight"]].plot()

import matplotlib.pyplot as plt
#plt.show()

games.plot(kind = 'scatter', x = 'Rating', y = 'Weight')
#plt.show()

print(games[games["Rating"] > 8])
print(games[(games["Rating"] > 8) & (games["MaxPlayers"] > 5)])
print(games[games["Rating"] == 8.22])


grouped = games["Rating"].groupby(games["BoardGame"])
print(grouped)
#tak nie mozna - trzeba grupowe
print(grouped.mean())

def multi(series):
    return series["Rating"] * series["Weight"]

games["New_col"] = games.apply(multi, axis = 1)
print(games)

