import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# データの読み込み
data = pd.read_csv('file.csv')

# データの確認
data.head()

# 欠損値の確認
data.isnull().sum()

# 欠損値の補完
data['Age'] = data['Age'].fillna(data['Age'].mean())
data['Fare'] = data['Fare'].fillna(data['Fare'].mean())

# 文字列を数値に変換
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data['Embarked'] = data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# 不要なデータを削除
data = data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)

# データの確認
data.head()

# データの分割
X = data.iloc[:, 1:].values
y = data.iloc[:, 0].values

# 学習データとテストデータに分割
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# モデルの構築
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# 予測
y_pred = model.predict(X_test)

# 評価
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)

# 提出用データの作成
submit_data = pd.read_csv('file.csv')
submit_data.head()

# 不要なデータを削除
submit_data = submit_data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)

# 文字列を数値に変換
submit_data['Sex'] = submit_data['Sex'].map({'male': 0, 'female': 1})
submit_data['Embarked'] = submit_data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# 欠損値の補完
submit_data['Age'] = submit_data['Age'].fillna(submit_data['Age'].mean())
submit_data['Fare'] = submit_data['Fare'].fillna(submit_data['Fare'].mean())

# 予測
submit_pred = model.predict(submit_data)

# 提出用ファイルの作成
submit_file = pd.read_csv('file.csv', header=None)
submit_file.columns = ['PassengerId', 'Survived']
submit_file['Survived'] = submit_pred
submit_file.to_csv('file.csv', index=False)





















































































































































































































































































































































































































































































































































ans = 0
for i in range(N):
    if i % 2 == 0:
        ans += a[i]
    else:
        ans -= a[i]

for i in range(N):
    if i % 2 == 0:
        print(ans, end=" ")
    else:
        print(-ans, end=" ")
