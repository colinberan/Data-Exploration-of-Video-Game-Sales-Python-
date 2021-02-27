#Exploratory Data Analysis of Video Game Sales (https://www.kaggle.com/gregorut/videogamesales)
#Script by Colin Beran
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Import .csv file
df = pd.read_csv(r"E:/Users/Colin/Documents/Data Science/Data Sets/vgsales.csv")
df

#Drop N/A values
df.dropna(inplace=True)
df.drop(columns="Rank",inplace=True)
df

#Filter years to 2000-2016
df = df[(df['Year']>=2000.0) & (df['Year']<=2016.0)]

#Plot number of titles with over 100k sales for the years of 2000-2016.
top_year = df[['Year','Global_Sales']]
top_year_df = top_year.groupby(by=['Year']).size().reset_index(name='Count')
year = top_year_df['Year']
count = top_year_df['Count']

plt.figure(figsize=(15, 10))
ax=sns.barplot(x="Year", y = "Count", data=top_year_df)
index = 0
for value in top_year_df['Count'].values:
    ax.text(index, value + 18, str(value), color='#000', size=14, ha="center")
    index += 1
    
plt.title('Number of Titles with over 100K Total Sales (2000-2016)')
plt.show()

#Plot of top 10 performing platforms from 2000-2016.
top_platform = df[['Year', 'Platform']]
top_platform_df = top_platform.groupby(by=['Platform']).size().reset_index(name='Count')
top_platform_df = top_platform_df.sort_values(by=['Count'], ascending = False).iloc[:10].reset_index(drop=True)
platform = top_platform_df['Platform']
count = top_platform_df['Count']

plt.figure(figsize=(15, 10))
ax=sns.barplot(x='Platform', y='Count', data=top_platform_df)
index=0
for value in top_platform_df['Count'].values:
    ax.text(index, value + 18, str(value), color='#000', size=14, ha="center")
    index += 1
    
plt.title('Top 10 Platforms by Titles with over 100K Total Sales (2000-2016)')
plt.show()

#Plot of top 20 publishers 2000-2016.
top_publisher = df[['Year', 'Publisher']]
top_publisher_df = top_publisher.groupby(by=['Publisher']).size().reset_index(name='Count')
top_publisher_df = top_publisher_df.sort_values(by=['Count'], ascending = False).iloc[:20].reset_index(drop=True)
publisher = top_publisher_df['Publisher']
count = top_publisher_df['Count']

plt.figure(figsize=(15, 10))
ax=sns.barplot(x='Publisher', y='Count', data=top_publisher_df)
index=0
for value in top_publisher_df['Count'].values:
    ax.text(index, value + 18, str(value), color='#000', size=14, ha="center")
    index += 1
    
plt.title('Top 20 Publishers by Titles with over 100K Total Sales (2000-2016)')
plt.xticks(rotation=90)
plt.show()

#Plot of top genre by number of games released
top_genre = df[['Year', 'Genre']]
top_genre_df = top_genre.groupby(by=['Genre']).size().reset_index(name='Count')
top_genre_df = top_genre_df.sort_values(by=['Count'], ascending = False).reset_index(drop=True)
genre = top_genre_df['Genre']
count = top_genre_df['Count']

plt.figure(figsize=(15, 10))
ax=sns.barplot(x='Genre', y='Count', data=top_genre_df)
index=0
for value in top_genre_df['Count'].values:
    ax.text(index, value + 18, str(value), color='#000', size=14, ha="center")
    index += 1
    
plt.title('Top Genre by Titles with over 100K Total Sales (2000-2016)')
plt.show()

#Plot of top 10 games in North America (2000-2016).
top_NA = df[['Name','NA_Sales']]
top_NA_df = top_NA.groupby(by=['Name']).sum().reset_index()
top_NA_df = top_NA_df.sort_values(by=['NA_Sales'], ascending = False).iloc[:10].reset_index(drop=True)
sales = top_NA_df['NA_Sales']
name = top_NA_df['Name']

plt.figure(figsize=(15, 10))
ax=sns.barplot(x='Name', y='NA_Sales', data=top_NA_df)
index=0
for value in top_NA_df['NA_Sales'].values:
    ax.text(index, value + 0.5, str(round(value,2)), color='#000', size=14, ha="center")
    index += 1
plt.ylabel('Sales (Millions)')
plt.title('Top 10 Games in North America (2000-2016)')
plt.xticks(rotation=90)
plt.show()

#Plot of top 10 games in Japan (2000-2016).
top_JP = df[['Name','JP_Sales']]
top_JP_df = top_JP.groupby(by=['Name']).sum().reset_index()
top_JP_df = top_JP_df.sort_values(by=['JP_Sales'], ascending = False).iloc[:10].reset_index(drop=True)
sales = top_JP_df['JP_Sales']
name = top_JP_df['Name']

plt.figure(figsize=(15, 10))
ax=sns.barplot(x='Name', y='JP_Sales', data=top_JP_df)
index=0
for value in top_JP_df['JP_Sales'].values:
    ax.text(index, value + 0.1, str(round(value,2)), color='#000', size=14, ha="center")
    index += 1
plt.ylabel('Sales (Millions)')
plt.title('Top 10 Games in Japan (2000-2016)')
plt.xticks(rotation=90)
plt.show()

#Plot of top 10 games in Europe (2000-2016).
top_EU = df[['Name','EU_Sales']]
top_EU_df = top_EU.groupby(by=['Name']).sum().reset_index()
top_EU_df = top_EU_df.sort_values(by=['EU_Sales'], ascending = False).iloc[:10].reset_index(drop=True)
sales = top_EU_df['EU_Sales']
name = top_EU_df['Name']

plt.figure(figsize=(15, 10))
ax=sns.barplot(x='Name', y='EU_Sales', data=top_EU_df)
index=0
for value in top_EU_df['EU_Sales'].values:
    ax.text(index, value + 0.1, str(round(value,2)), color='#000', size=14, ha="center")
    index += 1
plt.ylabel('Sales (Millions)')
plt.title('Top 10 Games in Europe (2000-2016)')
plt.xticks(rotation=90)
plt.show()

#Plot of top 10 games globally (2000-2016).
top_global = df[['Name','Global_Sales']]
top_global_df = top_global.groupby(by=['Name']).sum().reset_index()
top_global_df = top_global_df.sort_values(by=['Global_Sales'], ascending = False).iloc[:10].reset_index(drop=True)
sales = top_global_df['Global_Sales']
name = top_global_df['Name']

plt.figure(figsize=(15, 10))
ax=sns.barplot(x='Name', y='Global_Sales', data=top_global_df)
index=0
for value in top_global_df['Global_Sales'].values:
    ax.text(index, value + 0.1, str(round(value,2)), color='#000', size=14, ha="center")
    index += 1
plt.ylabel('Sales (Millions)')
plt.title('Top 10 Games Globally (2000-2016)')
plt.xticks(rotation=90)
plt.show()

#Compare how genres perform in each region.
compare_genre = df[['Genre', 'NA_Sales', 'EU_Sales', 'JP_Sales']]
compare_genre_df = compare_genre.groupby(by=['Genre']).sum()
#Heatmap
plt.figure(figsize=(15,10))
ax = sns.heatmap(compare_genre_df, annot=True, fmt = '.1f')
plt.title('Genre Performance by Region')
plt.show()
#Barplot
comp_plt = compare_genre_df.reset_index()
comp_plt = pd.melt(comp_plt, id_vars=['Genre'], value_vars=['NA_Sales', 'EU_Sales', 'JP_Sales'], var_name='Region', value_name='Total Sales')

plt.figure(figsize=(15, 10))
sns.barplot(x='Genre', y='Total Sales', hue = 'Region', data=comp_plt)
plt.ylabel('Sales (Millions)')
plt.title('Genre Perfromance by Region')
plt.show()