import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
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
2. Is there any correlation between GDP and life expectancy?
3. What is the average GDP among the 6 nations?
"""


# Inspecting the data
print(df.head())
print(df.info())
df = df.rename(columns={"Life expectancy at birth (years)": "Life"})


# Country-specific data
print(df['Country'].unique())
chile = df[df['Country'] == 'Chile']
china = df[df['Country'] == 'China']
germany = df[df['Country'] == 'Germany']
mexico = df[df['Country'] == 'Mexico']
usa = df[df['Country'] == 'United States of America']
zimbabwe = df[df['Country'] == 'Zimbabwe']
countries = ['Chile', 'China', 'Germany', 'Mexico', 'United States of America', 'Zimbabwe']


# 1.1 How has life expectancy changed over time among the 6 nations featured in the data?
plt.plot(chile['Year'], chile['Life'])
plt.plot(china['Year'], china['Life'])
plt.plot(germany['Year'], germany['Life'])
plt.plot(mexico['Year'], mexico['Life'])
plt.plot(usa['Year'], usa['Life'])
plt.plot(zimbabwe['Year'], zimbabwe['Life'])
plt.title("Life expectancy by year (2000-2015)")
plt.xlabel("Year")
plt.ylabel("Life expectancy at birth")
plt.legend(countries, loc=6)
plt.show()

# 1.2 How has GDP changed over time among the 6 nations featured in the data?
plt.plot(chile['Year'], chile['GDP'])
plt.plot(china['Year'], china['GDP'])
plt.plot(germany['Year'], germany['GDP'])
plt.plot(mexico['Year'], mexico['GDP'])
plt.plot(usa['Year'], usa['GDP'])
plt.plot(zimbabwe['Year'], zimbabwe['GDP'])
plt.title("GDP by year (2000-2015)")
plt.xlabel("Year")
plt.ylabel("GDP")
plt.legend(countries, loc=6)
plt.show()

# 2 Is there any correlation between GDP and Life expectancy?
# Chile
corr_chile_gdp_life, p = pearsonr(chile.GDP, chile.Life)
print("Correlation between GDP and Life expectancy in Chile (2000-2015): " + str(round(corr_chile_gdp_life, 3)))
cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
sns.scatterplot(x='GDP', y='Life', data=chile, hue='Year', palette=cmap)
plt.xlabel("GDP")
plt.ylabel("Life expectancy at birth (years)")
plt.title("Correlation between GDP and Life expectancy in Chile")
plt.show()

# China
corr_china_gdp_life, p = pearsonr(china.GDP, china.Life)
print("Correlation between GDP and Life expectancy in China (2000-2015): " + str(round(corr_china_gdp_life, 3)))
sns.scatterplot(x='GDP', y='Life', data=china, hue='Year', palette=cmap)
plt.xlabel("GDP")
plt.ylabel("Life expectancy at birth (years)")
plt.title("Correlation between GDP and Life expectancy in China")
plt.show()


# Germany
corr_ger_gdp_life, p = pearsonr(germany.GDP, germany.Life)
print("Correlation between GDP and Life expectancy in Germany (2000-2015): " + str(round(corr_ger_gdp_life, 3)))
sns.scatterplot(x='GDP', y='Life', data=germany, hue='Year', palette=cmap)
plt.xlabel("GDP")
plt.ylabel("Life expectancy at birth (years)")
plt.title("Correlation between GDP and Life expectancy in Germany")
plt.show()


# Mexico
corr_mex_gdp_life, p = pearsonr(mexico.GDP, mexico.Life)
print("Correlation between GDP and Life expectancy in Mexico (2000-2015): " + str(round(corr_mex_gdp_life, 3)))
sns.scatterplot(x='GDP', y='Life', data=mexico, hue='Year', palette=cmap)
plt.xlabel("GDP")
plt.ylabel("Life expectancy at birth (years)")
plt.title("Correlation between GDP and Life expectancy in Mexico")
plt.show()


# United States
corr_usa_gdp_life, p = pearsonr(usa.GDP, usa.Life)
print("Correlation between GDP and Life expectancy in the United States of America (2000-2015): " +
      str(round(corr_usa_gdp_life, 3)))
sns.scatterplot(x='GDP', y='Life', data=usa, hue='Year', palette=cmap)
plt.xlabel("GDP")
plt.ylabel("Life expectancy at birth (years)")
plt.title("Correlation between GDP and Life expectancy in USA")
plt.show()


# Zimbabwe
corr_zim_gdp_life, p = pearsonr(zimbabwe.GDP, zimbabwe.Life)
print("Correlation between GDP and Life expectancy in Zimbabwe (2000-2015): " + str(round(corr_zim_gdp_life, 3)))
sns.scatterplot(x='GDP', y='Life', data=zimbabwe, hue='Year', palette=cmap)
plt.xlabel("GDP")
plt.ylabel("Life expectancy at birth (years)")
plt.title("Correlation between GDP and Life expectancy in Zimbabwe")
plt.show()
plt.clf()


# 3 What is the average GDP among the 6 nations?
chile_mean_gdp = chile['GDP'].mean()
print("Average GDP in Chile (2000-2015): " + str(chile_mean_gdp))
china_mean_gdp = china['GDP'].mean()
print("Average GDP in China (2000-2015): " + str(china_mean_gdp))
germany_mean_gdp = germany['GDP'].mean()
print("Average GDP in Germany (2000-2015): " + str(germany_mean_gdp))
mexico_mean_gdp = mexico['GDP'].mean()
print("Average GDP in Mexico (2000-2015): " + str(mexico_mean_gdp))
usa_mean_gdp = usa['GDP'].mean()
print("Average GDP in the United States of America (2000-2015): " + str(usa_mean_gdp))
zimbabwe_mean_gdp = zimbabwe['GDP'].mean()
print("Average GDP in Zimbabwe (2000-2015): " + str(zimbabwe_mean_gdp))


'''
Conclusions:
Overall, all six countries featured in the database experienced an increase in both life expectancy and GDP over the
15-year period.

With all of the linear correlations between GDP and life expectancy for each respective country being close to +1 within
0.1, it is clear there is a high positive linearity between GDP and life expectancy at birth.

Finally, we can also see the average GDP for each country over the course of the 15-year period covered in the dataset. 
The average GDP in Chile was 169,788,845,015.3125. The average GDP in China was 4,957,713,750,000.0. The average GDP in 
Germany was 3,094,775,625,000.0. The average GDP in Mexico was 976,650,625,000.0. The average GDP in the United States 
of America was 14,075,000,000,000.0. And finally, the average GDP in Zimbabwe was 9,062,579,595.0625.
'''
