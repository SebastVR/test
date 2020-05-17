'''Assignment 3 - More Pandas
This assignment requires more individual learning then the last one did - you are encouraged to check out 
the pandas documentation to find functions or methods you might not have used yet, or ask questions on Stack 
Overflow and tag them as pandas and python related. And of course, the discussion forums are open for 
interaction with your peers and the course staff.

Question 1 (20%)
Load the energy data from the file Energy Indicators.xls, which is a list of indicators of energy supply 
and renewable electricity production from the United Nations for the year 2013, and should be put into a 
DataFrame with the variable name of energy.
Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude 
the footer and header information from the datafile. The first two columns are unneccessary, so you should 
get rid of them, and you should change the column labels so that the columns are:

['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']

Convert Energy Supply to gigajoules (there are 1,000,000 gigajoules in a petajoule). For all countries which 
have missing data (e.g. data with "...") make sure this is reflected as np.NaN values.

Rename the following list of countries (for use in later questions):

"Republic of Korea": "South Korea",
"United States of America": "United States",
"United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
"China, Hong Kong Special Administrative Region": "Hong Kong"

There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these, e.g.
'Bolivia (Plurinational State of)' should be 'Bolivia',
'Switzerland17' should be 'Switzerland'.

Next, load the GDP data from the file world_bank.csv, which is a csv containing countries' GDP from 
1960 to 2015 from World Bank. Call this DataFrame GDP.

Make sure to skip the header, and rename the following list of countries:
"Korea, Rep.": "South Korea", 
"Iran, Islamic Rep.": "Iran",
"Hong Kong SAR, China": "Hong Kong"

Finally, load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from the 
file scimagojr-3.xlsx, which ranks countries based on their journal contributions in the aforementioned area. 
Call this DataFrame ScimEn.
Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). 
Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 
'Rank' (Rank 1 through 15).
The index of this DataFrame should be the name of the country, and the columns should be 
['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document',
'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', 
'2010', '2011', '2012', '2013', '2014', '2015'].
This function should return a DataFrame with 20 columns and 15 entries.'''

import pandas as pd
def Energy():
    energy = pd.read_excel(
        'Energy Indicators.xls',
        skiprows = 17, 
        skip_footer = (38), 
        usecols = [2,3,4,5],
        names = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'],
        na_values = ['...']
    ) 

    energy['Energy Supply'] = energy['Energy Supply']*10**6
    energy['Country'] = energy['Country'].str.replace(r" *\(.*\)","")
    energy['Country'] = energy['Country'].str.replace(r"([0-9]+)","")
    energy.loc[energy['Country'] == 'Republic of Korea', 'Country'] = "South Korea"
    energy.loc[energy['Country'] == 'United States of America', 'Country'] = "United States"
    energy.loc[energy['Country'] == 'United Kingdom of Great Britain and Northern Ireland', 'Country'] = "United Kingdom"
    energy.loc[energy['Country'] == 'China, Hong Kong Special Administrative Region', 'Country'] = "Hong Kong"
    energy.dropna(how='all',inplace=True)
    return energy

def Gpd():
    GPD = pd.read_csv(
        'world_bank.csv', 
        skiprows=4)
    GPD.loc[GPD['Country Name'] == 'Korea, Rep.', 'Country Name'] = "South Korea"
    GPD.loc[GPD['Country Name'] == 'Iran, Islamic Rep.', 'Country Name'] = "Iran"
    GPD.loc[GPD['Country Name'] == 'Hong Kong SAR, China', 'Country Name'] = "Hong Kong"

    GPD.rename(columns={'Country Name':'Country'}, inplace = True)
    GPD = GPD[['Country','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']] 
    GPD.dropna(how='all', inplace=True)
    return GPD

def Scimen():
    ScimEn = pd.read_excel('scimagojr-3.xlsx')
    ScimEn.dropna(how='all', inplace=True)
    return ScimEn

def answer_one():
    energy, GPD, ScimEn = Energy(), Gpd(), Scimen()

    result = pd.merge(ScimEn, energy, how='inner', left_on='Country', right_on='Country')
    result = pd.merge(result, GPD, how='inner', left_on='Country', right_on='Country')

    result = result[result['Rank']<=15]
    result.set_index('Country', inplace=True)
    return result

answer_one()

#---------- ANSWER ----------
'''
                   Rank  Documents  ...          2014          2015
Country                              ...                            
China                  1     127050  ...  8.230121e+12  8.797999e+12
United States          2      96661  ...  1.615662e+13  1.654857e+13
Japan                  3      30504  ...  5.642884e+12  5.669563e+12
United Kingdom         4      20944  ...  2.605643e+12  2.666333e+12
Russian Federation     5      18534  ...  1.678709e+12  1.616149e+12
Canada                 6      17899  ...  1.773486e+12  1.792609e+12
Germany                7      17027  ...  3.624386e+12  3.685556e+12
India                  8      15005  ...  2.200617e+12  2.367206e+12
France                 9      13153  ...  2.729632e+12  2.761185e+12
South Korea           10      11983  ...  1.234340e+12  1.266580e+12
Italy                 11      10964  ...  2.033868e+12  2.049316e+12
Spain                 12       9428  ...  1.375605e+12  1.419821e+12
Iran                  13       8896  ...  4.639027e+11           NaN
Australia             14       8831  ...  1.272520e+12  1.301251e+12
Brazil                15       8668  ...  2.412231e+12  2.319423e+12

[15 rows x 20 columns]'''

#-----------------------------------------------------------------------
'''Question 2 (6.6%)
The previous question joined three datasets then reduced this to just the top 15 entries. 
When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?
This function should return a single number.'''
'''
%%HTML
<svg width="800" height="300">
  <circle cx="150" cy="180" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="blue" />
  <circle cx="200" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="red" />
  <circle cx="100" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="green" />
  <line x1="150" y1="125" x2="300" y2="150" stroke="black" stroke-width="2" fill="black" stroke-dasharray="5,3"/>
  <text  x="300" y="165" font-family="Verdana" font-size="35">Everything but this!</text>
</svg>'''
#Everything but this!

def answer_two():
    energy, GPD, ScimEn = Energy(), Gpd(), Scimen()

    inner = pd.merge(ScimEn, energy, how='inner', left_on='Country', right_on='Country')
    inner = pd.merge(inner, GPD, how='inner', left_on='Country', right_on='Country')

    outer = pd.merge(ScimEn, energy, how='outer', left_on='Country', right_on='Country')
    outer = pd.merge(outer, GPD, how='outer', left_on='Country', right_on='Country')

    return  len(outer) -len(inner)

answer_two()
#---------- ANSWER ----------
'''156'''

#-----------------------------------------------------------------------
'''Question 3 (6.6%)
What is the average GDP over the last 10 years for each country? (exclude missing values from this 
calculation.) This function should return a Series named avgGDP with 15 countries and their average 
GDP sorted in descending order.'''

import numpy as np
def answer_three():
    Top15 = answer_one()
    Top15['avgGDP'] = Top15[np.arange(2006, 2016).astype(str)].mean(axis=1)
    Top15.sort_values(by='avgGDP',ascending=False,inplace=True)
    return Top15['avgGDP']

answer_three()

#---------- ANSWER ----------
'''
Country
United States         1.536434e+13
China                 6.348609e+12
Japan                 5.542208e+12
Germany               3.493025e+12
France                2.681725e+12
United Kingdom        2.487907e+12
Brazil                2.189794e+12
Italy                 2.120175e+12
India                 1.769297e+12
Canada                1.660647e+12
Russian Federation    1.565459e+12
Spain                 1.418078e+12
Australia             1.164043e+12
South Korea           1.106715e+12
Iran                  4.441558e+11
Name: avgGDP, dtype: float64'''

#-----------------------------------------------------------------------
'''Question 4 (6.6%)
By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
This function should return a single number.'''

def answer_four():
    index = answer_three().index[5]
    Top15 = answer_one()
    return Top15.loc[index, '2015'] - Top15.loc[index, '2006']

answer_four()

#---------- ANSWER ----------
'''246702696075.3999'''

#-----------------------------------------------------------------------
'''Question 5 (6.6%)
What is the mean Energy Supply per Capita?.  This function should return a single number.''''

def answer_five():
    Top15 = answer_one()['Energy Supply per Capita'].mean()
    return Top15

answer_five()

#---------- ANSWER ----------
'''157.59999999999999'''

#-----------------------------------------------------------------------
'''Question 6 (6.6%)
What country has the maximum % Renewable and what is the percentage?
This function should return a tuple with the name of the country and the percentage'''

def answer_six():
    Top15 = answer_one()
    maxR = Top15['% Renewable'].max()
    country = Top15[Top15['% Renewable']==maxR].index[0]
    return country, maxR

answer_six()

#---------- ANSWER ----------
'''('Brazil', 69.648030000000006)'''

#-----------------------------------------------------------------------
'''Question 7 (6.6%)
Create a new column that is the ratio of Self-Citations to Total Citations. 
What is the maximum value for this new column, and what country has the highest ratio?
This function should return a tuple with the name of the country and the ratio.'''

def answer_seven():
    Top15 = answer_one()
    Top15['ratio'] = Top15['Self-citations'] / Top15['Citations']
    maxR = Top15['ratio'].max()
    country = Top15[Top15['ratio']==maxR].index[0]
    return country, maxR

answer_seven()

#---------- ANSWER ----------
'''('China', 0.68931261793894216)'''

#-----------------------------------------------------------------------
'''Question 8 (6.6%)
Create a column that estimates the population using Energy Supply and Energy Supply per capita. 
What is the third most populous country according to this estimate?
This function should return a single string value.'''

def answer_eight():
    Top15 = answer_one()
    Top15['population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15.sort_values(by='population',ascending=False, inplace=True)
    return Top15.index[2]

answer_eight()

#---------- ANSWER ----------
'''United States'''

#-----------------------------------------------------------------------
'''Question 9 (6.6%)
Create a column that estimates the number of citable documents per person. What is the correlation 
between the number of citable documents per capita and the energy supply per capita? Use the .corr() 
method, (Pearson's correlation).
This function should return a single number.

(Optional: Use the built-in function plot9() to visualize the relationship between 
Energy Supply per Capita vs. Citable docs per Capita)'''

def answer_nine():
    Top15 = answer_one()
    Top15['Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['Population']
    corr = Top15[['Citable docs per Capita','Energy Supply per Capita']].corr()
    return corr.iloc[0,1]

answer_nine()

#---------- ANSWER ----------
'''0.79400104354429435'''

#---------- ANSWER OPTIONAL ----------
def plot9():
    import matplotlib as plt
    #%matplotlib inline
    import matplotlib.pyplot as plt

    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])
    plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/Optional.png')
    #plt.show()
    return Top15.index[2]

plot9()

#-----------------------------------------------------------------------
'''Question 10 (6.6%)
Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries 
in the top 15, and a 0 if the country's % Renewable value is below the median.
This function should return a series named HighRenew whose index is the country name sorted in ascending 
order of rank.'''

def answer_ten():
    Top15 = answer_one()
    Top15['HighRenew'] = 0 
    Top15.loc[Top15['% Renewable']>=Top15['% Renewable'].median(),'HighRenew'] = 1 
    return Top15['HighRenew']

answer_ten()

#---------- ANSWER ----------
'''
Country
China                 1
United States         0
Japan                 0
United Kingdom        0
Russian Federation    1
Canada                1
Germany               1
India                 0
France                1
South Korea           0
Italy                 1
Spain                 1
Iran                  0
Australia             0
Brazil                1
Name: HighRenew, dtype: int64'''

#-----------------------------------------------------------------------
'''Question 11 (6.6%)
Use the following dictionary to group the Countries by Continent, then create a dateframe that displays the 
sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the 
estimated population of each country.

ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
This function should return a DataFrame with index named Continent 
['Asia', 'Australia', 'Europe', 'North America', 'South America'] and columns ['size', 'sum', 'mean', 'std']'''

def answer_eleven():
    import pandas as pd
    import numpy as np
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    continent = pd.Series({'China':'Asia', 
    'United States':'North America', 
    'Japan':'Asia', 
    'United Kingdom':'Europe', 
    'Russian Federation':'Europe', 
    'Canada':'North America', 
    'Germany':'Europe', 
    'India':'Asia',
    'France':'Europe', 
    'South Korea':'Asia', 
    'Italy':'Europe', 
    'Spain':'Europe', 
    'Iran':'Asia',
    'Australia':'Australia', 
    'Brazil':'South America'}, name='Continent').to_frame()

    df = pd.merge(Top15, continent, how='inner', left_index=True, right_index=True)
    group = df.groupby('Continent')['PopEst'].agg({'sum': np.sum,'mean': np.mean, 'std':np.std})
    group['size'] = df.groupby('Continent')['Rank'].count()
    group = group.astype(np.float64)
    return group

answer_eleven()

#---------- ANSWER ----------
'''	                sum	        mean	            std	        size
Continent				
Asia	        2.898666e+09	5.797333e+08	6.790979e+08	5.0
Australia	    2.331602e+07	2.331602e+07	NaN	            1.0
Europe	        4.579297e+08	7.632161e+07	3.464767e+07	6.0
North America	3.528552e+08	1.764276e+08	1.996696e+08	2.0
South America	2.059153e+08	2.059153e+08	NaN	            1.0'''

#-----------------------------------------------------------------------
'''Question 12 (6.6%)
Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. 
How many countries are in each of these groups?
This function should return a Series with a MultiIndex of Continent, then the bins for % Renewable. 
Do not include groups with no countries.'''

def answer_twelve():
    import pandas as pd
    Top15 = answer_one()

    Top15['bin'] = pd.cut(Top15['% Renewable'], 5)

    continent = pd.Series({'China':'Asia', 
                    'United States':'North America', 
                    'Japan':'Asia', 
                    'United Kingdom':'Europe', 
                    'Russian Federation':'Europe', 
                    'Canada':'North America', 
                    'Germany':'Europe', 
                    'India':'Asia',
                    'France':'Europe', 
                    'South Korea':'Asia', 
                    'Italy':'Europe', 
                    'Spain':'Europe', 
                    'Iran':'Asia',
                    'Australia':'Australia', 
                    'Brazil':'South America'}, name='Continent').to_frame()


    df = pd.merge(Top15, continent, how='inner', left_index=True, right_index=True)
    df['bin']= pd.Categorical(df['bin'],categories=[
        '(2.212, 15.753]','(15.753, 29.227]','(29.227, 42.701]','(56.174, 69.648]' 
    ], ordered=True)
    group = df.groupby(['Continent','bin'])['Rank'].count().dropna()
    return group

answer_twelve()

#---------- ANSWER ----------
'''
Continent      bin             
Asia           (2.212, 15.753]     0
               (15.753, 29.227]    0
               (29.227, 42.701]    0
               (56.174, 69.648]    0
Australia      (2.212, 15.753]     0
               (15.753, 29.227]    0
               (29.227, 42.701]    0
               (56.174, 69.648]    0
Europe         (2.212, 15.753]     0
               (15.753, 29.227]    0
               (29.227, 42.701]    0
               (56.174, 69.648]    0
North America  (2.212, 15.753]     0
               (15.753, 29.227]    0
               (29.227, 42.701]    0
               (56.174, 69.648]    0
South America  (2.212, 15.753]     0
               (15.753, 29.227]    0
               (29.227, 42.701]    0
               (56.174, 69.648]    0
Name: Rank, dtype: int64'''

#-----------------------------------------------------------------------
'''Question 13 (6.6%)
Convert the Population Estimate series to a string with thousands separator (using commas). Do not round the 
results. e.g. 317615384.61538464 -> 317,615,384.61538464
This function should return a Series PopEst whose index is the country name and whose values are the 
population estimate string.'''

def answer_thirteen():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['PopEst'] = Top15['PopEst'].map('{:,}'.format)
    return Top15['PopEst']

answer_thirteen()

#---------- ANSWER ----------
'''
Country
China                 1,367,645,161.2903225
United States          317,615,384.61538464
Japan                  127,409,395.97315437
United Kingdom         63,870,967.741935484
Russian Federation            143,500,000.0
Canada                  35,239,864.86486486
Germany                 80,369,696.96969697
India                 1,276,730,769.2307692
France                  63,837,349.39759036
South Korea            49,805,429.864253394
Italy                  59,908,256.880733944
Spain                    46,443,396.2264151
Iran                    77,075,630.25210084
Australia              23,316,017.316017315
Brazil                 205,915,254.23728815
Name: PopEst, dtype: object'''

#-----------------------------------------------------------------------
'''Optional
Use the built in function plot_optional() to see an example visualization'''

def plot_optional():
    import matplotlib as plt
    #import matplotlib.pyplot as plt
    #%matplotlib inline
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. \
    This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
    2014 GDP, and the color corresponds to the continent.")
    #plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/plot_optional.pdf')
    #plt.show()

plot_optional()