'''Assignment 4
Before working on this assignment please read these instructions fully. In the submission area, you will 
notice that you can click the link to Preview the Grading for each step of the assignment. 
This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria 
before beginning the assignment.
This assignment requires that you to find at least two datasets on the web which are related, and that you 
visualize these datasets to answer a question with the broad topic of religious events or traditions 
(see below) for the region of Ann Arbor, Michigan, United States, or United States more broadly.
You can merge these datasets with data from different regions if you like! For instance, you might want to 
compare Ann Arbor, Michigan, United States to Ann Arbor, USA. In that case at least one source file must be 
about Ann Arbor, Michigan, United States.
You are welcome to choose datasets at your discretion, but keep in mind they will be shared with your peers, 
so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good 
choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link 
to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the 
Coursera terms of service with respect to intellectual property.
Also, you are welcome to preserve data in its original language, but for the purposes of grading you should 
provide english translations. You are welcome to provide multiple visuals in different languages if you 
would like!
As this assignment is for the whole course, you must incorporate principles discussed in the first week, 
such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, 
function, and insight.
Here are the assignment instructions:
State the region and the domain category that your data sets are about (e.g., Ann Arbor, Michigan, United 
States and religious events or traditions).
You must state a question about the domain category and region that you identified as being interesting.
You must provide at least two links to available datasets. These could be links to files such as CSV or 
Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
You must upload an image which addresses the research question you stated. In addition to addressing the 
question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and 
insightfulness.
You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your 
stated research question.
What do we mean by religious events or traditions? For this category you might consider calendar events, 
demographic data about religion in the region and neighboring regions, participation in religious events, or 
how religious events relate to political events, social movements, or historical events.
Tips
Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
Many governments run open data initiatives at the city, region, and country levels, and these are wonderful 
resources for localized data sources.
Several international agencies, such as the United Nations, the World Bank, the Global Open Data Index are 
other great places to look for data.
This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how 
to do this from various sources, and share your successes with your fellow students!
Example
Looking for an example? Here's what our course assistant put together for the Ann Arbor, MI, USA area using 
sports and athletics as the topic. Example Solution File'''

#---------- ANSWER ----------
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

df1 = pd.read_csv('Pluviografo_estacion_70 (1).csv')
df2 = pd.read_csv('Pluviografo_estacion_69.csv')
df3 = pd.read_csv('Pluviografo_estacion_8.csv')

def call_df(df0):
	df0.sort_values(by = ['fechas'] , ascending = True, inplace=True)
	df0['Year'] = df0['fechas'].apply(lambda x: x[:4])
	df0['Date2'] = df0['fechas'].apply(lambda x: x[-5:])
	df0['Acum'] = df0['muestra'].cumsum()
	return df0

def statistics(df0):
	df = call_df(df0).groupby('Year').agg({'muestra': ['mean', 'max','std']})
	return df

Stats1 = statistics(df1)
Stats2 = statistics(df2)
Stats3 = statistics(df3)

#-------- PLOT --------
fig, axes = plt.subplots(nrows=2, ncols=1)
plt.subplot(3, 1, 1)
Stats1['muestra']['mean'].plot(label ='Q.Bermejala',); 
Stats2['muestra']['mean'].plot(label = 'Q.Doctora'); 
plt.title('Bored Valley Precipitation', fontsize=10)
plt.ylabel('Average value')
#plt.ticklabel_format(style='sci', axis='y',useMathText=True,useOffset=True,scilimits=(0, 0))
plt.xlabel(None)
plt.legend(loc='upper left', ncol=1, fontsize=8, frameon=True,shadow=True)

plt.subplot(3, 1, 2)
Stats1['muestra']['max'].plot(label = 'Q.Bermejala')
Stats2['muestra']['max'].plot(label = 'Q.Doctora')
plt.ylabel('Maximun value')
plt.legend(loc='upper left', ncol=1, fontsize=8, frameon=True, shadow=True)
#plt.tight_layout()
plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/Precipitation.png')
#-----------------------------------------------------------------------