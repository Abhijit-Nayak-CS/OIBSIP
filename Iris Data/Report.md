## 🌸 Iris Flower Classification Project Report
### 🧭 1. Objective

The aim of this project is to build a machine learning model that can classify Iris flowers into one of the three species —
Setosa, Versicolor, or Virginica — based on their sepal and petal measurements.

Although the scikit-learn library provides a built-in Iris dataset, we used a CSV version of the same dataset (Iris.csv) to perform the analysis from scratch.

### 🧩 2. Problem Statement

The Iris flower dataset consists of measurements for three species: Setosa, Versicolor, and Virginica.
Each flower is described by four features:

Sepal Length (cm)

Sepal Width (cm)

Petal Length (cm)

Petal Width (cm)

The goal is to train a machine learning model that can learn from these measurements and accurately classify new iris flowers into their respective species.

### 📊 3. Dataset Description

Dataset name: Iris.csv

Number of rows: 150

Number of columns: 5

Features:

SepalLengthCm

SepalWidthCm

PetalLengthCm

PetalWidthCm

Target Variable: Species (Setosa, Versicolor, Virginica)

### 🔍 4. Data Exploration and Visualization
#### a. Checking Dataset

The dataset was loaded using pandas and examined with .head(), .describe(), and .isnull() to ensure no missing values.

#### b. Pairplot Visualization

We used Seaborn’s pairplot() to visualise relationships between the four numeric features.
The pairplot clearly shows that Petal Length and Petal Width are strong indicators for separating the three species.

#### c. Correlation Heatmap

A correlation heatmap was generated using:

sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')


The heatmap shows:

Strong positive correlation between Petal Length and Petal Width

Weak correlation between Sepal Length and Sepal Width

This means petal measurements are more useful for classification.

### ⚙️ 5. Data Preprocessing

The dataset was divided into training (75%) and testing (25%) sets using train_test_split().

train, test = train_test_split(iris, test_size=0.25, random_state=42)


Then, we separated the features and target variable:

train_x = train[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
train_y = train['Species']
test_x = test[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
test_y = test['Species']

### 🤖 6. Model Building and Training

Three different supervised learning algorithms were used:

#### a. Support Vector Machine (SVM)

SVM is a classification algorithm that finds the best boundary (hyperplane) between different classes.

Model used:

svm_model = svm.SVC()
svm_model.fit(train_x, train_y)
pred_svm = svm_model.predict(test_x)


Accuracy: Printed using metrics.accuracy_score()

#### b. Decision Tree Classifier

Decision Trees split data based on feature values and make decisions in a tree-like structure.

Model used:

dt_model = DecisionTreeClassifier()
dt_model.fit(train_x, train_y)
pred_dt = dt_model.predict(test_x)


Accuracy: Calculated with metrics.accuracy_score()

#### c. K-Nearest Neighbors (KNN)

KNN classifies data points based on the majority of their nearest neighbors.

Model used:

knn_model = KNeighborsClassifier()
knn_model.fit(train_x, train_y)
pred_knn = knn_model.predict(test_x)


Accuracy: Calculated with metrics.accuracy_score()

### 📈 7. Model Performance
Model	Accuracy
Support Vector Machine (SVM)	~0.97
Decision Tree	~0.97
K-Nearest Neighbors (KNN)	~0.95

(The exact numbers may vary slightly due to random split.)

### 🧮 8. Model Comparison Visualization

A bar chart was plotted to compare model accuracies:

plt.bar(accuracies.keys(), accuracies.values(), color=['skyblue', 'orange', 'green'])
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.show()


The chart clearly shows that SVM and Decision Tree both perform extremely well on this dataset.

### 🧾 9. Evaluation Metrics

Although accuracy was high, further evaluation can be done using a confusion matrix and classification report to see precision and recall for each class.

print(confusion_matrix(test_y, pred_dt))
print(classification_report(test_y, pred_dt))


These metrics show that all three classes (Setosa, Versicolor, and Virginica) are classified accurately with almost 100% precision and recall.

### 🏆 10. Results and Conclusion

The models successfully classified iris flowers into their correct species.

SVM and Decision Tree performed the best, achieving accuracy around 97–100%.

Petal Length and Petal Width are the most important features for distinguishing species.

The project fulfills the recruitment requirement:

“Train a machine learning model that learns from iris flower measurements and classifies them.”

### 🧠 11. Learnings from the Project

Through this project, I learned:

How to load and explore real-world datasets in Python.

How to visualize relationships using Seaborn.

How to split data into training and testing sets.

How to train, test, and compare multiple classification models.

How to evaluate performance using accuracy, confusion matrix, and classification report.

### 📚 12. Technologies and Libraries Used
Tool / Library	Purpose
Python	Main programming language
NumPy	Numerical operations
Pandas	Data loading and manipulation
Matplotlib, Seaborn	Data visualization
Scikit-learn (sklearn)	Machine learning models and evaluation
### 🧾 13. Final Remarks

This project demonstrates the complete process of building and evaluating classification models using Python.
It satisfies the given requirement and showcases practical knowledge of data preprocessing, visualization, and supervised machine learning techniques.