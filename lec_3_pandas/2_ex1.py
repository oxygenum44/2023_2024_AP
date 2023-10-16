import pandas as pd

data = {
  "Boardgame": ["TM", "GWT", "Everdell"],
  "weight": [3.81, 3.78, 3.22],
  "rating": [8.81, 8.32, 8.31]
}

pandas_data_frame = pd.DataFrame(data, index=["A", 3, 7])
print(pandas_data_frame)
print(pandas_data_frame.to_string())
print(pandas_data_frame.keys())

# print(pandas_data_frame['weight'])
#print(pandas_data_frame.loc[3])
#print(pandas_data_frame.loc[2, 3])
#print(pandas_data_frame.loc[["A", 3]])


pandas_data_frame2 = pd.Series(data)
print(pandas_data_frame2)
