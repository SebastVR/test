'''Practice Assignment: Understanding Distributions Through Sampling
This assignment is optional, and I encourage you to share your solutions with me and your peers in the 
discussion forums!

To complete this assignment, create a code cell that:

Creates a number of subplots using the pyplot subplots or matplotlib gridspec functionality.
Creates an animation, pulling between 100 and 1000 samples from each of the random variables (x1, x2, x3, x4) 
for each plot and plotting this as we did in the lecture on animation.
Bonus: Go above and beyond and "wow" your classmates (and me!) by looking into matplotlib widgets and adding 
a widget which allows for parameterization of the distributions behind the sampling animations.
Tips:

Before you start, think about the different ways you can create this visualization to be as interesting and effective as possible.
Take a look at the histograms below to get an idea of what the random variables look like, as well as their positioning with respect to one another. This is just a guide, so be creative in how you lay things out!
Try to keep the length of your animation reasonable (roughly between 10 and 30 seconds).''''

#---------- ANSWER ----------
import numpy as np
import matplotlib.pyplot as plt
import glob
from PIL import Image

x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)
x4 = np.random.uniform(14,20, 10000)

x = [x1, x2, x3, x4]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharey = True)

ax = [ax1, ax2, ax3, ax4]

axis1 = [-7.5, 2.5, 0, 0.6]
axis2 = [0, 10, 0, 0.6]
axis3 = [7, 17, 0, 0.6]
axis4 = [12, 22, 0, 0.6]
axis = [axis1, axis2, axis3, axis4]

bins1 = np.arange(-7.5, 2.5, 0.2)
bins2 = np.arange(0, 10, 0.2)
bins3 = np.arange(7, 17, 0.2)
bins4 = np.arange(12, 22, 0.2)
bins = [bins1, bins2, bins3, bins4]

titles = ['x1 Normal', 'x2 Gamma', 'x3 Exponential', 'x4 Normed Frequency']
color = ['#b5ef10', '#1b0045', '#cc0000', '#333333']

for i in range(len(ax)):
	#ax[i].cla()
	ax[i].hist(x[i],  density= True, bins = bins[i], color = color[i])
	ax[i].axis(axis[i])
	ax[i].set_title(titles[i])
	ax[i].set_ylabel('Normed Frequency')
	ax[i].set_xlabel('Value')
	plt.tight_layout()
	plt.savefig('/mnt/d/SebasUbuntu/Documentos/GraficasHis/%s.png'  % (titles[i]))

#--------- CREATE GIF ---------
imgs = glob.glob("/mnt/d/SebasUbuntu/Documentos/GraficasHis/*.png")#Save all imagen in file
# Create the frames
frames = []
#imgs = glob.glob("/mnt/d/SebasUbuntu/Documentos/Graficas/*x*.png")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)
 
# Save into a GIF file that loops forever
frames[0].save('/mnt/d/SebasUbuntu/Documentos/GraficasHis/Hist.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=1000, loop=0)
#-----------------------------------------------------------------------