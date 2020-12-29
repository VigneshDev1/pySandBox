# Learn SciKit module : Machine Learning Algorithms
# more documentation can be found at scikit-learn.org
import pandas as pd
from sklearn.linear_model import LogisticRegression as LReg
import numpy as np

dataset = 'https://sololearn.com/uploads/files/titanic.csv'

df = pd.read_csv(dataset)
df['male'] = df['Sex'] == 'male'
X = df[['Fare', 'Age']].values
X1 = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
Y = df['Survived'].values
print(X1)
# print(Y)
model = LReg()
model.fit(X1, Y)
print(Y[:5])
Y_pred = model.predict(X1)
print(Y_pred[:5])

print(model.coef_, model.intercept_)
print(model.coef_)
# print(Y_pred)
# region .....PLOTTING.....
from matplotlib import pyplot as plt

linx = np.linspace(20, 110, 100)
print(model.coef_[0][1])
liny = (model.coef_[0][0] * linx + model.intercept_) / (-1 * model.coef_[0][1])
plt.scatter(df['Fare'], df['Age'], c=df['Survived'])
plt.plot(linx, liny, '-r', label='Linear Regression')
plt.xlabel('Fare')
plt.ylabel('Age')
plt.show()

# endregion
