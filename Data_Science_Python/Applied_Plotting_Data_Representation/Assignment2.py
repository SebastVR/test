'''Assignment 2
Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to Preview the Grading for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.

An NOAA dataset has been stored in the file data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv. This is the dataset to use for this assignment. Note: The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) Daily Global Historical Climatology Network (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.

Each row in the assignment datafile corresponds to a single observation.

The following variables are provided to you:

id : station identification code
date : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
element : indicator of element type
TMAX : Maximum temperature (tenths of degrees C)
TMIN : Minimum temperature (tenths of degrees C)
value : data value for element (tenths of degrees C)
For this assignment, you must:

Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
The data you have been given is near Ann Arbor, Michigan, United States, and the stations the data comes from are shown on the map below.'''

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')

#---------- ANSWER ----------
def Time_series():
	df = pd.read_csv(
		'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
	df.head()

	#df.shape : (597953, 4)
	df['Data_Value'] = df['Data_Value'] * 0.1 #outof coursera platform memrory
	df['Year'] = df['Date'].apply(lambda x: x[:4])
	df['Date2'] = df['Date'].apply(lambda x: x[-5:])
	df = df[df['Date2'] != '02-29']
	df_05_14 = df[~(df['Year'] == '2015')]
	df_15 = df[df['Year'] == '2015']
	df_05_14.head()

	#temp = pd.DataFrame()
	max_0415 = df_05_14.groupby('Date2').agg({'Data_Value':np.max})
	min_0415 = df_05_14.groupby('Date2').agg({'Data_Value':np.min})
	max_15 = df_15.groupby('Date2').agg({'Data_Value':np.max})
	min_15 = df_15.groupby('Date2').agg({'Data_Value':np.min})
	all_max = pd.merge(max_0415.reset_index(), max_15.reset_index(), left_index=True, on = 'Date2')
	all_min = pd.merge(min_0415.reset_index(), min_15.reset_index(), left_index=True, on = 'Date2')

	break_max = all_max[all_max['Data_Value_y'] > all_max['Data_Value_x']]
	break_min = all_min[all_min['Data_Value_y'] < all_min['Data_Value_x']]
	break_max.head()

	plt.figure(figsize=(16,10))

	plt.plot(max_0415.values, c = '#1b7021', label ='Record Maximun')
	plt.plot(min_0415.values, c = '#00ffc7', label ='Record minimun')

	plt.xlabel('Day', fontsize=20)
	plt.ylabel('Temperature °C', fontsize=20)
	plt.title('Ten Year Record (2005-2014) Was Broken in 2015', fontsize=25)

	plt.scatter(break_max.index.tolist(), break_max['Data_Value_y'].values, c = '#ff4300', label = "Maximun in 2015")
	plt.scatter(break_min.index.tolist(), break_min['Data_Value_y'].values, c = '#d61f1f', label = "Minimun in 2015")

	plt.gca().fill_between(range(len(max_0415)), 
						np.array(max_0415.values.reshape(len(min_0415.values),)), 
						np.array(min_0415.values.reshape(len(min_0415.values),)), 
						facecolor='#fdeea4', 
						alpha=0.25)

	plt.gca().spines['top'].set_visible(True)
	plt.gca().spines['right'].set_visible(True)
	plt.legend(loc = 8, fontsize=18, frameon = False)

	plt.show()
	#plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/Serie(6).png')


	#create link
	'''file ='data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv'
	!cp "$file" .
	from IPython.display import HTML
	link = '<a href="{0}" download>Click here to download {0}</a>'
	HTML(link.format(file.split('/')[-1]))

	#Click here to download fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv'''

	#change days for months
	x = np.arange(0, 365)

	labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	ticks = np.arange(min(x), max(x)+len(x)/12, len(x)/12)

	minor_ticks = ticks + (len(x)/12)/2
	minor_ticks = minor_ticks[:len(minor_ticks)-1]

	ax = plt.gca()

	ax.set_xticks(ticks)
	ax.set_xticklabels('')
	ax.set_xticks(minor_ticks, minor = True)
	ax.set_xticklabels(labels, minor = True)
	ax.tick_params(axis='x', which = 'minor', length= 0)
	plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/Time Series.png')
	return df.head()

Time_series()