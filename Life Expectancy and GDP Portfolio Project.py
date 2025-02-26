import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
"""
For this project, you will analyze data on GDP and life expectancy from the World Health Organization and the World Bank
to try and identify the relationship between the GDP and life expectancy of six countries.

During this project, you will analyze, prepare, and plot data in order to answer questions in a meaningful way.

After you perform your analysis, you’ll be creating a blog post to share your findings on the World Health Organization
website.
"""


"""
Scoping Data and Project Goals:
Problem description: What is the relationship between GDP and life expectancy in six different countries? Is there a 
lower life expectancy among lower-income nations (i.e. Nations with low GDP scores)?
Priority: The World Bank issues loans to low-income countries. This information determines which countries they should
issue loans to based on countries with lower life expectancies.
"""


df = pd.read_csv('all_data.csv')


"""
Research Questions:
1.1. How has life expectancy changed over time among the 6 nations featured in the data?
1.2. How has GDP changed over time among the 6 nations featured in the data?
2.1. In a given year, what country has had the greatest life expectancy?
2.2. In a given year, what country has had the highest GDP?
3. Is there any correlation between GDP and life expectancy?
4. 
"""


# Inspecting the data
print(df.head())
print(df.info())


# Country-specific data
print(df['Country'].unique())
chile = df[df['Country'] == 'Chile']
china = df[df['Country'] == 'China']
germany = df[df['Country'] == 'Germany']
mexico = df[df['Country'] == 'Mexico']
usa = df[df['Country'] == 'United States of America']
zimbabwe = df[df['Country'] == 'Zimbabwe']
countries = ['Chile', 'China', 'Germany', 'Mexico', 'United States of America', 'Zimbabwe']


#1.1 How has life expectancy changed over time among the 6 nations featured in the data?
plt.plot(chile['Year'], chile['Life expectancy at birth (years)'])
plt.plot(china['Year'], china['Life expectancy at birth (years)'])
plt.plot(germany['Year'], germany['Life expectancy at birth (years)'])
plt.plot(mexico['Year'], mexico['Life expectancy at birth (years)'])
plt.plot(usa['Year'], usa['Life expectancy at birth (years)'])
plt.plot(zimbabwe['Year'], zimbabwe['Life expectancy at birth (years)'])
plt.title("Life expectancy by year (2000-2015)")
plt.xlabel("Year")
plt.ylabel("Life expectancy at birth")
plt.legend(countries, loc=6)
plt.show()
plt.clf()

#1.2 How has GDP changed over time among the 6 nations featured in the data?
plt.plot(chile['Year'], chile['GDP'])
plt.plot(china['Year'], china['GDP'])
plt.plot(germany['Year'], germany['GDP'])
plt.plot(mexico['Year'], mexico['GDP'])
plt.plot(usa['Year'], usa['GDP'])
plt.plot(zimbabwe['Year'], zimbabwe['GDP'])
plt.title("GDP by year (2000-2015")
plt.xlabel("Year")
plt.ylabel("GDP")
plt.legend(countries, loc=6)
plt.show()
plt.clf()
