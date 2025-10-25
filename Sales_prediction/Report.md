# Sales Prediction using Machine Learning
## 1. Title

### Project Title: Sales Prediction using Machine Learning (Linear Regression Model)

This project is about predicting product sales using the amount of money spent on different types of advertisements such as TV, Radio, and Newspaper.

## 2. Objective

The main aim of this project is to predict sales based on advertising spending.
This helps the company to understand which advertisement method increases sales the most and where they should spend more money to get better profit.

## 3. Dataset Description

The dataset used for this project is called Advertising.csv.
It contains 200 rows and 4 columns.

Column Name	Description
TV	Amount of money spent on TV advertisement
Radio	Amount of money spent on Radio advertisement
Newspaper	Amount of money spent on Newspaper advertisement
Sales	Total number of sales (Target variable)

An extra column (Unnamed: 0) was dropped as it was not required.

## 4. Data Analysis

We first checked the relationship between the features (TV, Radio, Newspaper) and Sales.
To do this, we used a Correlation Matrix.

Feature	TV	Radio	Newspaper	Sales
TV	1.00	0.05	0.06	0.78
Radio	0.05	1.00	0.35	0.57
Newspaper	0.06	0.35	1.00	0.23
Sales	0.78	0.57	0.23	1.00
Observation:

TV has the strongest positive relation (0.78) with sales.

Radio has a good relation (0.57) with sales.

Newspaper has a very low relation (0.23) with sales.

So, spending on TV and Radio gives better results compared to Newspaper.

We also made scatter plots (Pair Plot) which showed that TV and Radio advertising have a clear upward trend with sales, meaning as spending increases, sales also increase.

## 5. Model Building

We used Linear Regression from scikit-learn to build the prediction model.

Steps followed:

Split data into Training (80%) and Testing (20%) sets.

Applied StandardScaler to normalize the data.

Trained the Linear Regression model using training data.

Predicted sales values using test data.

## 6. Model Output

Model Coefficients:

Feature	Coefficient
TV	3.80
Radio	2.82
Newspaper	0.10
Intercept	14.02

Evaluation Metrics:

Metric	Value
Mean Squared Error (MSE)	2.36
Mean Absolute Error (MAE)	1.10
R² Score (Accuracy)	0.89

✅ Model Accuracy = 89%

This means our model can correctly predict 89% of the variation in sales using advertising data.

## 7. Model Results (Predicted vs Actual Sales)
Actual Sales	Predicted Sales
14.6	13.9
18.0	18.2
21.4	20.9
12.5	12.0
16.7	16.9

The predicted values are very close to actual sales, which shows that the model is performing very well.

## 8. Visualization Summary

True vs Predicted Plot:
Shows predicted sales vs actual sales. The points are near the diagonal line — so predictions are accurate.

Residual Plot:
Residuals (errors) are close to zero — this means the model fits the data properly.

## 9. Conclusion

The Linear Regression model is successful in predicting sales with 89% accuracy.

The TV and Radio advertisement budgets are the most effective in increasing sales.

Newspaper advertisements have very little impact on sales.

So, for better profit:

The company should spend more money on TV and Radio advertisements.

The company can reduce Newspaper advertisement spending, as it gives very little return.

## 10. Business Benefit

From this project, the company learns that:

TV advertising gives the highest benefit — it directly increases sales.

Radio advertising is also helpful, especially when combined with TV.

Newspaper is the least effective channel.

By focusing more on TV and Radio, the company can:

Save advertising cost

Increase total sales

Improve marketing strategy and profit margin

## 11. Final Summary
Factor	Effect on Sales	Business Decision
TV	Highest Impact	Increase Budget
Radio	Moderate Impact	Maintain or Slightly Increase
Newspaper	Very Low Impact	Reduce Budget
Model Accuracy	89%	Reliable Results

### Final Result:
✅ TV and Radio advertising give the most benefit to the company.
✅ Linear Regression model predicts sales accurately (R² = 0.89).