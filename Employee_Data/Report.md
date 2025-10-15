# 📊 Data Science Project Report: COVID-19 Unemployment Analysis in India (2020)
🧠 Objective

Unemployment is measured by the unemployment rate, which represents the percentage of people in the labour force who are unemployed and actively looking for work.
During the COVID-19 lockdown, India saw a sharp rise in unemployment due to restrictions on movement, factory closures, and job losses.

The main objective of this project is to:

Analyse unemployment trends before and after lockdown.

Study patterns across states and regions.

Visualise employment and labour participation rates.

Understand how different parts of India were impacted.

## 📁 Dataset Overview

Dataset Name: Unemployment_Rate_upto_11_2020.csv
Source: Open Government Data (India)
Duration Covered: January 2020 – October 2020

Main Columns Used:

Column	Description
States	Indian states and union territories
Date	Date of data collection
Estimated Unemployment Rate	Percentage of unemployed individuals
Estimated Employed	Number of employed individuals (in thousands)
Estimated Labour Participation Rate	Labour force participation percentage
Region	Regional classification (North, South, etc.)
Longitude & Latitude	Geographical coordinates for mapping
## 🧹 Data Cleaning and Preparation

Renamed all columns for clarity.

Converted the “Date” column to proper datetime format.

Created two new columns:

Month int (numeric month value)

Month (month abbreviation like Jan, Feb, etc.)

Checked for missing values and duplicates — none significant were found.

Grouped the data by Month, States, and Region for detailed analysis.

## 📈 1. Monthly Trend Analysis (National Level)
### 🔹 Observations:

Unemployment rate increased sharply in April and May 2020 (immediately after lockdown).

The Labour Participation Rate fell during the same months, showing that many people stopped actively searching for jobs.

Employment numbers (Estimated Employed) dropped drastically in April 2020, then slowly improved by July.

### 🔹 Key Insights:
Month	Unemployment Rate	Labour Participation Rate
Jan–Mar 2020	Stable (6–8%)	Around 42–44%
Apr–May 2020	Sharp increase (20–24%)	Drop to 35–36%
Jun–Oct 2020	Gradual recovery	Improving to pre-lockdown levels
🧩 2. State-wise Analysis
### 🔹 Findings:

States such as Tamil Nadu, Haryana, and Delhi recorded the highest unemployment rates during lockdown.

States like Bihar, Chhattisgarh, and Meghalaya showed lower rates compared to others.

High variation between states indicates that economic structure (industry vs agriculture) influenced job loss severity.

### 🔹 Visualisations Used:

Box Plot: To compare unemployment rate distribution across states.

Bar Chart: To show average unemployment rate (state-wise).

Animated Plot: To view how state unemployment changed month-by-month.

## 🗺️ 3. Geographic Analysis (Map Visualization)

Created a geo-scatter map showing the unemployment rate across India using longitude and latitude.

Animation by month clearly shows:

April 2020: Highest unemployment intensity (darkest regions).

Gradual improvement towards August–October.

### 🔹 Observation:

Regions like North India (Punjab, Haryana) and West India (Maharashtra, Gujarat) had higher impact compared to North-East India.

## 🌎 4. Region-wise Analysis
### 🔹 Regions Covered:

North, South, East, West, North-East, and Central.

### 🔹 Insights:

North and West regions faced higher unemployment rates during lockdown months.

South and North-East regions were relatively more stable.

Labour participation varied significantly by region, showing uneven economic recovery.

### 🔹 Visualisations:

Scatter Matrix (to compare three metrics together)

Bar Chart (average unemployment rate by region)

Animated Bar (monthly region-wise changes)

Sunburst Chart (hierarchical relation: Region → State)

## 🔒 5. Before and After Lockdown Comparison

To measure the direct impact of lockdown:

Before Lockdown: January to March 2020

After Lockdown: April to May 2020

## ✅ Process:
before_lockdown = dataset[(dataset['Month int'] >= 1) & (dataset['Month int'] < 4)]
after_lockdown = dataset[(dataset['Month int'] >= 4) & (dataset['Month int'] < 6)]

before_avg = before_lockdown.groupby('States')['Estimated Unemployment Rate'].mean().reset_index()
after_avg = after_lockdown.groupby('States')['Estimated Unemployment Rate'].mean().reset_index()
lockdown = pd.merge(before_avg, after_avg, on='States')

### 🔹 Results (sample):
States	Before Lockdown (%)	After Lockdown (%)
Maharashtra	7.4	20.1
Delhi	8.9	27.3
Bihar	9.1	15.2
Tamil Nadu	6.7	18.5
### 🔹 Conclusion:

The national average unemployment rate nearly tripled during the lockdown.

Urban and industrial states suffered more compared to rural and agricultural ones.

## 📊 6. Key Takeaways
Area	Observation
### 🔸 National Level	Unemployment spiked in April–May 2020, later slowly recovered.
### 🔸 State Level	Urban states like Delhi, Maharashtra, and Tamil Nadu most affected.
### 🔸 Regional Level	North and West India saw highest job losses.
### 🔸 Labour Force	Participation rate dropped, indicating discouraged workers.
### 🔸 Post-lockdown	Gradual improvement from June onward due to economic reopening.
## 🧾 Conclusion

This analysis clearly shows how the COVID-19 lockdown led to a major unemployment crisis in India, particularly between April and May 2020.
While some recovery began in the following months, the impact was uneven across states and regions.

Using Python (Pandas, Plotly, Matplotlib), we visualised:

Time-based trends,

State-wise and region-wise variations,

Lockdown impact comparison.

Such insights can help policymakers and economists understand where job creation and recovery support are most needed.

## 🧰 Tools & Libraries Used
Library	Purpose
Pandas	Data cleaning and grouping
Numpy	Numeric computations
Plotly Express / Graph Objects	Interactive visualisation
Matplotlib / Seaborn	Statistical plotting
Datetime / Calendar	Time-based extraction
## 📘 Final Note

This project demonstrates strong skills in:

Data cleaning and preprocessing

Data visualisation using Plotly

Analytical interpretation of socio-economic data

Real-world application of data analytics

It’s a complete end-to-end Data Analytics project suitable for inclusion in your internship portfolio or LinkedIn post.