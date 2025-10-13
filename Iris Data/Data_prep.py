# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

iris = pd.read_csv('Iris.csv')

# First 5 Rows of the Dataset
print(iris.head())

# Dataset Summary
print(iris.describe())

# Checking for missing values
print(iris.isnull().sum())

# Pairplot to visualize feature relationships
sns.pairplot(iris, hue='Species')
plt.suptitle("Pairplot of Iris Features by Species", y=1.02)
plt.show()

# Correlation heatmap
numeric_data = iris.select_dtypes(include=['float64', 'int64'])
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()


# Splitting the dataset into training and testing sets
train, test = train_test_split(iris, test_size=0.25, random_state=42)

# training data
train_x = train[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
train_y = train['Species']

# testing data
test_x = test[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
test_y = test['Species']

#  SVM Model Accuracy
svm_model = svm.SVC()
svm_model.fit(train_x, train_y)
pred_svm = svm_model.predict(test_x)
svm_acc = metrics.accuracy_score(test_y, pred_svm)
print("\n✅ SVM Model Accuracy:", svm_acc)


# Decision Tree Model Accuracy
dt_model = DecisionTreeClassifier()
dt_model.fit(train_x, train_y)
pred_dt = dt_model.predict(test_x)
dt_acc = metrics.accuracy_score(test_y, pred_dt)
print("✅ Decision Tree Model Accuracy:", dt_acc)

# KNN model Accuracy
knn_model = KNeighborsClassifier()
knn_model.fit(train_x, train_y)
pred_knn = knn_model.predict(test_x)
knn_acc = metrics.accuracy_score(test_y, pred_knn)
print("✅ KNN Model Accuracy:", knn_acc)

# All Accuracy models
accuracies = {
    'SVM': svm_acc,
    'Decision Tree': dt_acc,
    'KNN': knn_acc
}

plt.bar(accuracies.keys(), accuracies.values(), color=['skyblue', 'orange', 'green'])
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.show()


