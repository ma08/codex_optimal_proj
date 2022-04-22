

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/train.csv')

# print(df.head())
# print(df.info())

# sns.countplot(x='Survived', data=df)

# sns.countplot(x='Survived', hue='Sex', data=df)

# sns.countplot(x='Survived', hue='Pclass', data=df)

# sns.distplot(df['Age'].dropna(), kde=False, bins=30)

# df['Age'].plot.hist()

# sns.countplot(x='SibSp', data=df)

# df['Fare'].hist(bins=40, figsize=(10, 4))

# plt.show()
