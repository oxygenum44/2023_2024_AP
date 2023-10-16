import pandas as pd

data = {
  "Person":{
    "0":'Smith John',
    "1":'Smith Mary',
    "2":'Clock Barthlomew',
    "3":'Clock Victoria',
    "4":'Drop Bary',
    "5":'Drop Gary'
  },
  "Number":{
    "0":10,
    "1":17,
    "2":31,
    "3":92,
    "4":17,
    "5":23
  },
  "Bigger number":{
    "6":2008,
    "1":3454,
    "2":4443,
    "3":1212,
    "4":1212,
    "5":3211
  },
  "Mini number":{
    "0":0.124,
    "1":0.849,
    "2":0.343,
    "3":0.182,
    "4":0.496,
    "6":0.424
  }
}

df = pd.DataFrame(data)

print(df)

df2 = pd.read_json('2_ex2.json')
print(df2)
