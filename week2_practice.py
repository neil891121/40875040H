import pandas as pd

data = pd.read_csv('special_edu.csv')
data.head()
# print(data)

temp = data[['縣市','學校', '地址']]
print(temp)



data2016 = pd.read_csv('2016.csv')
data2017 = pd.read_csv('2017.csv')
data2018 = pd.read_csv('2018.csv')
new = data2016[['Complex2Name', 'FValue']].groupby(['Complex2Name'])['FValue'].sum().reset_index()
new['year'] = 2016


frames = [type, new]
result = pd.concat(frames)
print(result)