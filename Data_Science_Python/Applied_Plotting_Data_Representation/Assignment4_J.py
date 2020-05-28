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
import datetime as dt

df1 = pd.read_csv(
	'Pluviografo_estacion_70 (1).csv', 
	index_col=['fechas'], 
	parse_dates=['fechas']
)
df2 = pd.read_csv(
	'Pluviografo_estacion_69.csv',
	index_col=['fechas'], 
	parse_dates=['fechas']
)

def plot(df, title, xlabel):
	ax = df.plot(legend=False)
	ax.set_title(title)
	ax.set_ylabel("Precipitation [mm]")
	ax.set_xlabel(xlabel)
	ax.legend([y for m,y in df.columns], title='Years')
	return ax

#----- Monthly Precipitation Cycle of Bermejala's Station ----- 
ppt = df1.groupby([lambda x: x.year, lambda x: x.month]).sum().unstack(0)
ax = plot(ppt, "Monthly Precipitation Cycle of Bermejala's Station", "Months")
ticks =  ax.get_xticks()
ticks = [dt.date(2000, int(val), 1).strftime('%B') if val> 0 and val <13 else val for val in ticks]
ax.set_xticklabels(ticks)
plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/PPTCicloMensual.png')

#----- Daily Precipitation Cycle  of Bermejala's Station -----
dc_ppt = df1.groupby([lambda x: x.year, lambda x: x.hour]).sum().unstack(0)
ax = plot(dc_ppt, "Daily Precipitation Cycle  of Bermejala's Station", "Hours")
plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/PPTCicloDiurno.png')

#------------------------ Trust Bands ------------------------
ppt.quantile([0.25,0.5,0.75], axis=1).T
dq_dr = ppt.quantile([0.25,0.5,0.75], axis=1).T
dq_dr.rename(columns = {0.25:'0.25', 0.5:'0.5',0.75:'0.75'},inplace=True)
ax = dq_dr.plot()
ax.legend(title='Quantiles')
ax.set_title("Quantiles Precipitation Cycle of Bermejala's Station")
ax.set_ylabel("Precipitation [mm]")
ticks =  ax.get_xticks()
ticks = [dt.date(2000, int(val), 1).strftime('%B') if val> 0 and val <13 else val for val in ticks]
ax.set_xticklabels(ticks)
plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/PPTstaticsCicloDiurno.png')
#-----------------------------------------------------------------------