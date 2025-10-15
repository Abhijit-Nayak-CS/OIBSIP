# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import calendar
import plotly.graph_objects as go
import plotly.express as px

dataset = pd.read_csv('Unemployment_Rate_upto_11_2020.csv')
dataset.head()

dataset.tail()

# Organize the columns names
dataset.columns=["States","Date","Frequency","Estimated Unemployment Rate","Estimated Employed","Estimated labour participation Rate","Region","Longitude","Latitude"]

dataset.head()

# Check the data size
dataset.shape

# check the describe function
dataset.describe()

# Check for missing values
dataset.isnull().sum()

# check the data duplicates
dataset.duplicated().sum()

# check the state wise data set
dataset.States.value_counts()

dataset['Date'] = pd.to_datetime(dataset['Date'],dayfirst=True)

# Add new column for month place in integer format
dataset['Month int'] = dataset['Date'].dt.month
dataset.head()

# Add new column for month place in string format
dataset['Month'] = dataset['Month int'].apply(lambda x: calendar.month_abbr[x])
dataset.head()

IND = dataset.groupby(["Month"])[['Estimated Unemployment Rate', 'Estimated Employed', 'Estimated labour participation Rate']].mean()
IND = pd.DataFrame(IND).reset_index()

Month = IND.Month
unemployment_rate = IND["Estimated Unemployment Rate"]
labour_participation_rate = IND["Estimated labour participation Rate"]

# Barchart Categorical model
fig = go.Figure()
fig.add_trace(go.Bar(x = Month, y = unemployment_rate, name = 'Unemployment Rate'))
fig.add_trace(go.Bar(x = Month, y = labour_participation_rate, name = 'Labor Participation Rate'))
fig.update_layout(title = 'Unemployment Rate and Labor Participation Rate',
                    xaxis = {"categoryorder": "array", "categoryarray": ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct']})
fig.show()

## Estimated employed people from Jan 2020 to Oct 2020 (month wise)
fig = px.bar(IND, x='Month', y='Estimated Employed', color = 'Month',
            category_orders = {"Month": ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct']},
            title = 'Estimated employed people from Jan 2020 to Oct 2020')

fig.show()


# States Wise Analysis
States = dataset.groupby(["States"])[['Estimated Unemployment Rate', 'Estimated Employed', 'Estimated labour participation Rate']].mean()
States = pd.DataFrame(States).reset_index()


# Box plot Model for Unemployment Rate
fig = px.box(dataset,x='States', y = 'Estimated Unemployment Rate', color = 'States', title = 'Unemployment Rate')
fig.update_layout(xaxis = {'categoryorder': 'total descending'})
fig.show()

# Bar plot Model for Average unemployment Rate(State Wise)
fig = px.bar(States,x='States', y = 'Estimated Unemployment Rate', color = 'States', title = 'Average unemployment Rate(State Wise)')
fig.update_layout(xaxis = {'categoryorder': 'total descending'})
fig.show()

# Bar plot unemployment rate monthly
fig = px.bar(dataset, x='States',y= 'Estimated Unemployment Rate', animation_frame='Month', color='States',
            title= 'Unemployment Rate From Jan 2020 to Oct 2020(State Wise)')
fig.update_layout(xaxis = {'categoryorder': 'total descending'})
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"]= 2000
fig.show()


# Map plot for unemployment rate
fig = px.scatter_geo(dataset, 'Longitude', 'Latitude', color = "States",
                    hover_name='States', size= 'Estimated Unemployment Rate',
                    animation_frame= 'Month', scope= 'asia', title= 'Impact of lockdown on employment rate in India')
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"]= 2000
fig.update_geos(lataxis_range=[5,40], lonaxis_range= [65,100],oceancolor= 'lightgrey',
                showocean= True)
fig.show()

dataset.head()

## Region Wise Analysis
dataset.Region.unique()
dataset['Region'].value_counts()


# Numeric data group by region
region = dataset.groupby(['Region'])[['Estimated Unemployment Rate', 'Estimated Employed', 'Estimated labour participation Rate']].mean()
region = pd.DataFrame(region).reset_index()

fig = px.scatter_matrix(dataset,dimensions= ['Estimated Unemployment Rate', 'Estimated Employed', 'Estimated labour participation Rate'], color = "Region")
fig.show()


# Average Unemployment rate region wise 
fig = px.bar(region, x= 'Region', y= 'Estimated Unemployment Rate', color = 'Region', 
            title= 'Average Unemployment Rate (Region Wise)')
fig.update_layout(xaxis = {'categoryorder': 'total descending'})
fig.show()

## Unemployment rate from Jan 2020 to Oct 2020 (Region wise)
fig = px.bar(dataset,x='Region', y= 'Estimated Unemployment Rate', color='States', animation_frame= 'Month',
            title= 'Unemployment rate from Jan 2020 to Oct 2020')
fig.update_layout(xaxis = {'categoryorder': 'total descending'})
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration']= 2000
fig.show()

# Tabular model data output
Unemployment = dataset.groupby(['Region','States'])['Estimated Unemployment Rate'].mean().reset_index()
Unemployment.head()

fig = px.sunburst(Unemployment, path=['Region','States'], values= 'Estimated Unemployment Rate',
                title= 'Unemployment Rate in every State and Region', height= 700)
fig.show()

# Unemployment rate before and after lockdown
# Data before and after lockdown
before_lockdown = dataset[(dataset['Month int'] >= 1) & (dataset['Month int'] < 4)]
after_lockdown = dataset[(dataset['Month int'] >= 4) & (dataset['Month int'] < 6)]

# Average unemployment rate per state
before_avg = before_lockdown.groupby('States')['Estimated Unemployment Rate'].mean().reset_index()
after_avg = after_lockdown.groupby('States')['Estimated Unemployment Rate'].mean().reset_index()

# Rename columns
before_avg.rename(columns={'Estimated Unemployment Rate': 'Unemployment Rate before lockdown'}, inplace=True)
after_avg.rename(columns={'Estimated Unemployment Rate': 'Unemployment Rate after lockdown'}, inplace=True)

# Merge both DataFrames on 'States'
lockdown = pd.merge(before_avg, after_avg, on='States')

# Display result
lockdown.head()

