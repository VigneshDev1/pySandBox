import pandas as pd  # Human readable table format
import numpy as np  # package to do lot of statistical calculations

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
# To create a boolean value series out of the data
df['male'] = df['Sex'] == 'male'  # New column created to record boolean value
print(df.head())

# To convert dataframe to numpy array
arr = df[['Fare', 'Age']].values
print(arr.shape)  # shape object returns rows and columns count

print(str(arr[0, 0]) + "  " + str(arr[1, 1]))  # access array elements [row, col] 0 being first row/col
# to access a whole row eg. arr[0]
# to access a single col eg. arr[:,1]
mask = arr[:, 1] < 18  # Boolean values created on a mask variable
print(arr[mask])  # Assign the mask and get new array data for 'true' values only
print(mask.sum())  # sum() method returns the sum of values in the array
print(arr[mask].shape)
print(df['male'])

#region .....PLOTTING.....
from matplotlib import pyplot as plt
plt.scatter(df['Age'],df['Fare'],c=df['male'])
plt.xlabel('Age')
plt.ylabel('Fare')
plt.plot([0,80],[85,5])  # Plotting line ([set of x values], [set of y values])
plt.show()

#endregion
