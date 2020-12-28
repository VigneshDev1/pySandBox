import pandas as pd
dataset = 'https://sololearn.com/uploads/files/titanic.csv'
# DataFrame : table of data

df = pd.read_csv(dataset)
print(df.head())  # head() method shows the first 5 rows of dataset
pd.options.display.max_columns = 6
# print(df.describe())  # describe() method shows statistical summary (ie. mean, std, min, 25%, 50%, max)
# print(list(df.columns))  # prints all column headers

getAgeData = df['Age']  # extracts as data series
getmultiCol = df[['Age', 'Survived', 'Fare']]  # Use double square brackets for multiple columns

print(getmultiCol)
