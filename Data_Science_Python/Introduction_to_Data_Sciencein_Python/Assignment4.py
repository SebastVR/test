import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

'''Assignment 4 - Hypothesis Testing
This assignment requires more individual learning than previous assignments - you are encouraged to check 
out the pandas documentation to find functions or methods you might not have used yet, or ask questions on 
Stack Overflow and tag them as pandas and python related. And of course, the discussion forums are open for 
interaction with your peers and the course staff.

Definitions:

A quarter is a specific three month period, Q1 is January through March, Q2 is April through June, Q3 is July 
rough September, Q4 is October through December.
A recession is defined as starting with two consecutive quarters of GDP decline, and ending with two 
consecutive quarters of GDP growth.
A recession bottom is the quarter within a recession which had the lowest GDP.
A university town is a city which has a high percentage of university students compared to the total 
population of the city.
Hypothesis: University towns have their mean housing prices less effected by recessions. Run a t-test to 
compare the ratio of the mean price of houses in university towns the quarter before the recession starts 
compared to the recession bottom. (price_ratio=quarter_before_recession/recession_bottom)

The following data files are available for this assignment:

From the Zillow research data site there is housing data for the United States. In particular the datafile 
for all homes at a city level, City_Zhvi_AllHomes.csv, has median home sale prices at a fine grained level.
From the Wikipedia page on college towns is a list of university towns in the United States which has been 
copy and pasted into the file university_towns.txt.
From Bureau of Economic Analysis, US Department of Commerce, the GDP over time of the United States in 
current dollars (use the chained value in 2009 dollars), in quarterly intervals, in the file gdplev.xls. 
For this assignment, only look at GDP data from the first quarter of 2000 onward.
Each function in this assignment below is worth 10%, with the exception of run_ttest(), which is worth 50%.'''

#-----------------------------------------------------------------------
'''Returns a DataFrame of towns and the states they are in from the 
university_towns.txt list. The format of the DataFrame should be:
DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
columns=["State", "RegionName"]  )
    
The following cleaning needs to be done:

1. For "State", removing characters from "[" to the end.
2. For "RegionName", when applicable, removing every character from " (" to the end.
3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    
def get_list_of_university_towns():
    import pandas as pd
    import re
    rute = 'university_towns.txt'	
    with open(rute) as file:
        townslist = file.readlines()
    townslist = [x.rstrip() for x in townslist]
    townslist2 =[]
    for i in townslist:
        if '[edit]' in i:
            state_string = re.sub(r" *\(.*\)| *\[.*\]","",i)
        else:
            region_string  = re.sub(r" *\(.*\)| *\[.*\]","",i)
            townslist2.append([state_string,region_string])
    df = pd.DataFrame(townslist2, columns=['State','RegionName'])
    return df

get_list_of_university_towns()

#---------- SHAPE 2 ----------
def get_list_of_university_towns():
	State = []
	RegionName = []

	with open ('university_towns.txt', "r") as fileObj:
		line = fileObj.readline().strip()

		while line != '':

			if line[-6:] == '[edit]':
				st = line[:-6]
			else:
				State.append(st)
				RegionName.append(line)

			line = fileObj.readline().strip()

	ut = pd.DataFrame(list(zip(State,RegionName)),columns=['State','RegionName'])
	ut.RegionName.replace(r" \([^(]*|\([^(]*","", inplace=True,regex = True) 

	return ut

get_list_of_university_towns()

#---------- ANSWER ----------
'''
         State     RegionName
0      Alabama         Auburn
1      Alabama       Florence
2      Alabama   Jacksonville
3      Alabama     Livingston
4      Alabama     Montevallo
..         ...            ...
512  Wisconsin    River Falls
513  Wisconsin  Stevens Point
514  Wisconsin       Waukesha
515  Wisconsin     Whitewater
516    Wyoming        Laramie

[517 rows x 2 columns]'''

#-----------------------------------------------------------------------
# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 
'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 
'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 
'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 
'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 
'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 
'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 
'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 
'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 
'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 
'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 
'VA': 'Virginia'}

#-----------------------------------------------------------------------
'''Returns the year and quarter of the recession start time as a string value in a format such as 2005q3'''

def get_recession_start():
    import pandas as pd
    gdp= pd.read_excel(
        'gdplev.xls', 
        skiprows= 219)
    gdp = gdp[['1999q4', 12323.3]]
    gdp = gdp.rename(columns={'1999q4':'Quarter', 12323.3:'GDP in billions'})
    for i in range(0,gdp.shape[0]-1):
        if (gdp.iloc[i-2][1]> gdp.iloc[i-1][1]) and (gdp.iloc[i-1][1]> gdp.iloc[i][1]):
            startdate = gdp.iloc[i-3][0]
    return  startdate

get_recession_start()

#---------- ANSWER ----------
'''2008q3'''

#-----------------------------------------------------------------------
'''Returns the year and quarter of the recession end time as a string value in a format such as 2005q3'''

def get_recession_end():
    import pandas as pd
    gdplev = pd.ExcelFile('gdplev.xls')
    gdplev = gdplev.parse("Sheet1", skiprows=219)
    gdplev = gdplev[['1999q4', 9926.1]]
    gdplev.columns = ['Quarter','GDP']
    start = get_recession_start()
    start_index = gdplev[gdplev['Quarter'] == start].index.tolist()[0]
    gdplev = gdplev.iloc[start_index:]
    for i in range(2, len(gdplev)):
        if (gdplev.iloc[i-2][1] < gdplev.iloc[i-1][1]) and (gdplev.iloc[i-1][1] < gdplev.iloc[i][1]):
            return gdplev.iloc[i][0]

get_recession_end()

#---------- ANSWER ----------
'''2009q4'''

#-----------------------------------------------------------------------
'''Returns the year and quarter of the recession bottom time as a string value in a format such as 2005q3'''

def get_recession_bottom():
    import pandas as pd
    gdplev = pd.ExcelFile('gdplev.xls')
    gdplev = gdplev.parse("Sheet1", skiprows=219)
    gdplev = gdplev[['1999q4', 9926.1]]
    gdplev.columns = ['Quarter','GDP']
    start = get_recession_start()
    start_index = gdplev[gdplev['Quarter'] == start].index.tolist()[0]

    end = get_recession_end()
    end_index = gdplev[gdplev['Quarter'] == end].index.tolist()[0]

    gdp = gdplev.iloc[start_index:end_index+1]
    bottom = gdp['GDP'].min()
    bottom_index = gdp[gdp["GDP"]== bottom].index.tolist()[0]-start_index

    return gdp.iloc[bottom_index]['Quarter']

get_recession_bottom()

#---------- ANSWER ----------
'''2009q2'''

#-----------------------------------------------------------------------
'''Converts the housing data to quarters and returns it as mean 
values in a dataframe. This dataframe should be a dataframe with
columns for 2000q1 through 2016q3, and should have a multi-index
in the shape of ["State","RegionName"].

Note: Quarters are defined in the assignment description, they are
not arbitrary three month periods.

The resulting dataframe should have 67 columns, and 10,730 rows.'''

def convert_housing_data_to_quarters():
    import pandas as pd 
    house = pd.read_csv(
        'City_Zhvi_AllHomes.csv',header = 0)

    a = list(range(3,51))
    house.drop(house.columns[a],axis=1,inplace=True)
    house.drop(house.columns[0],axis=1,inplace=True)

    states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 
    'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 
    'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 
    'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 
    'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 
    'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 
    'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 
    'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 
    'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 
    'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

    house.replace({'State':states}, inplace = True)
    house.set_index(['State','RegionName'],inplace = True)
    house = house.groupby(pd.PeriodIndex(house.columns, freq='Q'), axis=1).mean()

    return house

convert_housing_data_to_quarters()

#---------- ANSWER ----------
'''
                                         2000Q1  ...    2016Q3
State        RegionName                          ...          
New York     New York                       NaN  ...  587200.0
California   Los Angeles          207066.666667  ...  584050.0
Illinois     Chicago              138400.000000  ...  212000.0
Pennsylvania Philadelphia          53000.000000  ...  128700.0
Arizona      Phoenix              111833.333333  ...  195200.0
...                                         ...  ...       ...
Wisconsin    Town of Wrightstown  101766.666667  ...  155000.0
New York     Urbana                79200.000000  ...  143000.0
Wisconsin    New Denmark          114566.666667  ...  197600.0
California   Angels               151000.000000  ...  269950.0
Wisconsin    Holland              151033.333333  ...  234950.0

[10730 rows x 67 columns]'''

#-----------------------------------------------------------------------
'''First creates new data showing the decline or growth of housing prices
between the recession start and the recession bottom. Then runs a ttest
comparing the university town values to the non-university towns values, 
return whether the alternative hypothesis (that the two groups are the same)
is true or not as well as the p-value of the confidence. 

Return the tuple (different, p, better) where different=True if the t-test is
True at a p<0.01 (we reject the null hypothesis), or different=False if 
otherwise (we cannot reject the null hypothesis). The variable p should
be equal to the exact p value returned from scipy.stats.ttest_ind(). The
value for better should be either "university town" or "non-university town"
depending on which has a lower mean price ratio (which is equivilent to a
reduced market loss).'''

def run_ttest():
    import numpy as np
    from scipy import stats
    start = pd.Period(get_recession_start())
    bottom = pd.Period(get_recession_bottom())
    house = convert_housing_data_to_quarters().loc[:,[start,bottom]]
    house.columns = ["Start","Bottom"]
    house["Ratio"] = house.Start / house.Bottom #NAN不用处理，反正数据不使用
    house = house.dropna(axis=0,how="any")
    collage = get_list_of_university_towns().set_index(["State","RegionName"])
    collage["isUnv"] = "Yes"
    res = pd.merge(house,collage,how="left",left_index=True,right_index=True)
    res.isUnv = res.isUnv.fillna("No")

    res_u = res[res.isUnv == "Yes"].Ratio
    res_n = res[res.isUnv == "No"].Ratio
    #print(res_n)
    _,p = stats.ttest_ind(res_u,res_n)
    different = (True if p < 0.01 else False)
    better = ("university town" if np.nanmean(res_u) < np.nanmean(res_n) else "non-university town")
    return different, p, better

run_ttest()

#---------- ANSWER ----------
'''(True, 0.0026673736473538773, 'university town')'''
#-----------------------------------------------------------------------