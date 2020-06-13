'''Assignment 1
In this assignment, you'll be working with messy medical data and using regex to extract relevant 
infromation from the data.
Each line of the dates.txt file corresponds to a medical note. Each note has a date that needs to be 
extracted, but each date is encoded in one of many formats.
The goal of this assignment is to correctly identify all of the different date variants encoded in this 
dataset and to properly normalize and sort the dates.
Here is a list of some of the variants you might encounter in this dataset:

04/20/2009; 04/20/09; 4/20/09; 4/3/09
Mar-20-2009; Mar 20, 2009; March 20, 2009; Mar. 20, 2009; Mar 20 2009;
20 Mar 2009; 20 March 2009; 20 Mar. 2009; 20 March, 2009
Mar 20th, 2009; Mar 21st, 2009; Mar 22nd, 2009
Feb 2009; Sep 2009; Oct 2010
6/2008; 12/2009
2009; 2010
Once you have extracted these date patterns from the text, the next step is to sort them in ascending 
chronological order accoring to the following rules:

Assume all dates in xx/xx/xx format are mm/dd/yy
Assume all dates where year is encoded in only two digits are years from the 1900's (e.g. 1/5/89 is 
January 5th, 1989)
If the day is missing (e.g. 9/2009), assume it is the first day of the month (e.g. September 1, 2009).
If the month is missing (e.g. 2010), assume it is the first of January of that year (e.g. January 1, 2010).
Watch out for potential typos as this is a raw, real-life derived dataset.
With these rules in mind, find the correct date in each note and return a pandas Series in chronological 
order of the original Series' indices.

For example if the original series was this:

0    1999
1    2010
2    1978
3    2015
4    1985
Your function should return this:

0    2
1    4
2    0
3    1
4    3
Your score will be calculated using Kendall's tau, a correlation measure for ordinal data.

This function should return a Series of length 500 and dtype int.'''

import pandas as pd

doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)
df.head(10)

#---------- ANSWER CODE ----------
def date_sorter():

#   df1 =  04/20/2009; 04/20/09; 4/20/09; 4/3/09
    df1 = df.str.extractall(r'(?:(?P<month>[0]?[1-9]|[1][012])[/-](?P<day>[0]?[1-9]|[12][0-9]|[3][01])[/-](?P<year>19\d{2}|20\d{2}|\d{2}))')
    df1.year[df1.year.str.len() == 2] ='19' + df1.year
#     df1 = pd.to_datetime(df1)
    
#   df2 =  20 Mar 2009; 20 March 2009; 20 Mar. 2009; 20 March, 2009
    df2 = df.str.extractall(r'(?:(?P<day>[0]?[1-9]|[12][0-9]|[3][01]) (?P<month>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z., -]*(?P<year>19\d{2}|20\d{2}))')
    
#   df3 =  Mar-20-2009; Mar 20, 2009; March 20, 2009; Mar. 20, 2009; Mar 20 2009
#   df3 +=  Mar 20th, 2009; Mar 21st, 2009; Mar 22nd, 2009
    df3 = df.str.extractall(r'(?:(?P<month>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z., -]*(?P<day>[0]?[1-9]|[12][0-9]|[3][01])[a-z., -]*(?P<year>19\d{2}|20\d{2}))')
    
        
#   df4 =  Feb 2009; Sep 2009; Oct 2010
    df4 = df.str.extractall(r'(?:(?P<month>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z., -]*(?P<year>19\d{2}|20\d{2}))')
    df4['day'] = '1'
#     df4.index = df4.index.get_level_values(0)
    
#   df5 =  6/2008; 12/2009
    df5 = df.str.extractall(r'(?:(?P<month>[0]?[1-9]|[1][012])[/-](?P<year>19\d{2}|20\d{2}))')
    df5['day'] = '1'
    
#   df6 =  2009; 2010
    df6 = df.str.extractall(r'(?:(?P<year>19\d{2}|20\d{2}))')
    df6['day'] = '1'
    df6['month'] = '1'

#     Append
    df2 = df2.append(df3)
    df2 = df2.append(df4)
    df2 = df2[~df2.index.duplicated(keep='first')]
    
    # %b to %m
    df2.month = pd.to_datetime(df2.month,format='%b').apply(lambda x: x.strftime('%m'))
    
#     output = pd.concat([df1,df2],join='outer',verify_integrity=True)
    output = df1.append(df2,verify_integrity=True)
    output = output.append(df5)
    output = output.append(df6)
    output.index = output.index.get_level_values(0)
    output = output[~output.index.duplicated(keep='first')]
    output = pd.to_datetime(output)
    return pd.Series(output.sort_values().index)
#     return output

date_sorter()

#---------- ANSWER ----------
0        9
1       84
2        2
3       53
4       28
      ... 
495    231
496    141
497    186
498    161
499    413
Length: 500, dtype: int64
#-----------------------------------------------------------------------