import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectFromModel

from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold

from sklearn.pipeline import Pipeline

# Data
df = pd.read_csv("data.csv")

# Data Exploration
print(df.head())
print(df.info())

# Data Cleaning
df.drop(['Unnamed: 32', 'id'], axis=1, inplace=True)

# Data Exploration
print(df["diagnosis"].value_counts())

# Plotting
sns.countplot(df["diagnosis"], label="Count")

# Plotting
plt.figure(figsize=(10,10))
sns.heatmap(df.corr(), annot=True)

# Data Encoding
label_encoder = LabelEncoder()
df["diagnosis"] = label_encoder.fit_transform(df["diagnosis"])

# Plotting
sns.pairplot(df, hue="diagnosis")

# Splitting
x = df.drop("diagnosis", axis=1)
y = df["diagnosis"]

# Feature Scaling
scaler = MinMaxScaler()
x = scaler.fit_transform(x)

# Splitting
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=101)

# Logistic Regression
log_reg = LogisticRegression()
log_reg.fit(x_train, y_train)
y_pred = log_reg.predict(x_test)

# Evaluation
print("Accuracy score: ", accuracy_score(y_test, y_pred))
print("Confusion matrix: \n", confusion_matrix(y_test, y_pred))

# Roc Curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred)

# Plotting
plt.plot(fpr, tpr, label="Logistic Regression")
plt.plot([0,1], [0,1], "r--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Logistic Regression ROC Curve")
plt.legend(loc="lower right")

# ROC AUC Score
print("ROC AUC score: ", roc_auc_score(y_test, y_pred))

# Feature Selection
best_features = SelectKBest(score_func=chi2, k=10)
fit = best_features.fit(x, y)

# Printing
print(fit.scores_)
df_scores = pd.DataFrame(fit.scores_)
df_columns = pd.DataFrame(df.columns)

# Concatenation
feature_scores = pd.concat([df_columns, df_scores], axis=1)
feature_scores.columns = ["Feature", "Score"]

# Printing
print(feature_scores.nlargest(10, "Score"))

# Variance Threshold
threshold = VarianceThreshold(threshold=0.1)
x = threshold.fit_transform(x)

# Splitting
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=101)

# Logistic Regression
log_reg = LogisticRegression()
log_reg.fit(x_train, y_train)
y_pred = log_reg.predict(x_test)

# Evaluation
print("Accuracy score: ", accuracy_score(y_test, y_pred))
print("Confusion matrix: \n", confusion_matrix(y_test, y_pred))

# Feature Selection
model = LinearSVC(C=0.1, penalty="l1", dual=False)
model.fit(x, y)
model = SelectFromModel(model, prefit=True)
x = model.transform(x)

# Splitting
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=101)

# Logistic Regression
log_reg = LogisticRegression()
log_reg.fit(x_train, y_train)
y_pred = log_reg.predict(x_test)

# Evaluation
print("Accuracy score: ", accuracy_score(y_test, y_pred))
print("Confusion matrix: \n", confusion_matrix(y_test, y_pred))

# Pipeline
pipeline = Pipeline([
    ("scaler", MinMaxScaler()),
    ("model", LogisticRegression())
])

# Cross Validation
cv_scores = cross_val_score(pipeline, x, y, cv=10, scoring="accuracy")

# Printing
print(cv_scores)
print(cv_scores.mean())
