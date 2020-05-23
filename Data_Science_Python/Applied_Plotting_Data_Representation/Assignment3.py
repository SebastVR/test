
'''Assignment 3 - Building a Custom Visualization
In this assignment you must choose one of the options presented below and submit a visual as well as your 
source code for peer grading. The details of how you solve the assignment are up to you, although your 
assignment must use matplotlib so that your peers can evaluate your work. The options differ in challenge 
level, but there are no grades associated with the challenge level you chose. However, your peers will be 
asked to ensure you at least met a minimum quality for a given technique in order to pass. Implement the 
technique fully (or exceed it!) and you should be able to earn full grades for the assignment.

Ferreira, N., Fisher, D., & Konig, A. C. (2014, April). Sample-oriented task-driven visualizations: 
allowing users to make better, more confident decisions.       In Proceedings of the SIGCHI Conference on 
Human Factors in Computing Systems (pp. 571-580). ACM. (video)

In this paper the authors describe the challenges users face when trying to make judgements about 
probabilistic data generated through samples. As an example, they look at a bar chart of four years of 
data (replicated below in Figure 1). Each year has a y-axis value, which is derived from a sample of a 
larger dataset. For instance, the first value might be the number votes in a given district or riding 
for 1992, with the average being around 33,000. On top of this is plotted the 95% confidence interval 
for the mean (see the boxplot lectures for more information, and the yerr parameter of barcharts).

A challenge that users face is that, for a given y-axis value (e.g. 42,000), it is difficult to know which 
x-axis values are most likely to be representative, because the confidence levels overlap and their 
distributions are different (the lengths of the confidence interval bars are unequal). One of the solutions 
the authors propose for this problem (Figure 2c) is to allow users to indicate the y-axis value of interest 
(e.g. 42,000) and then draw a horizontal line and color bars based on this value. So bars might be colored 
red if they are definitely above this value (given the confidence interval), blue if they are definitely 
below this value, or white if they contain this value.

Easiest option: Implement the bar coloring as described above - a color scale with only three colors, 
(e.g. blue, white, and red). Assume the user provides the y axis value of interest as a parameter or 
variable.
Harder option: Implement the bar coloring as described in the paper, where the color of the bar is actually 
based on the amount of data covered (e.g. a gradient ranging from dark blue for the distribution being 
certainly below this y-axis, to white if the value is certainly contained, to dark red if the value is 
certainly not contained as the distribution is above the axis).
Even Harder option: Add interactivity to the above, which allows the user to click on the y axis to set the 
value of interest. The bar colors should change with respect to what value the user has selected.
Hardest option: Allow the user to interactively set a range of y values they are interested in, and recolor 
based on this (e.g. a y-axis band, see the paper for more details).

Note: The data given for this assignment is not the same as the data used in the article and as a result the 
visualizations may look a little different.'''

import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995]).T

#---------- ANSWER ----------
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy.stats

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return h

def getColor(val, mini, maxi, cmap):
    # this idea comes from the tutor in the discussion board.
#     if val <= (mean-ci):
#         return 'darkblue'
#     elif val >= (mean+ci):
#         return 'darkred'
#     else:
    print ((val - (mini))/ ((maxi) -(mini) ))
    return cmap ((val - (mini))/ ((maxi) -(mini) ))

#%matplotlib notebook

typColor = '#%02x%02x%02x' % (115,115,115)
plt.rc('axes',labelcolor=typColor, edgecolor=typColor,)#facecolor=typColor)
plt.rc('axes.spines',right=False, top=False, )#left=False, bottom=False)
plt.rc('text',color= typColor)
plt.rc('xtick',color=typColor)
plt.rc('ytick',color=typColor)
#
y = 40000
x = mean_confidence_interval(df)
me = df.mean(axis=0)
cmap = plt.get_cmap('seismic',11)
norm = mpl.colors.Normalize(vmin=me.min(),vmax=me.max())

colors = [getColor(m, me.min(), me.max(), cmap ) for m in me]

ax = me.plot(kind='bar',yerr=x,color=colors)
ax.axhline(y,color='k')
plt.xticks(rotation=0)

sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm, ticks=np.linspace(0,1,11), 
#              boundaries=np.arange(-0.05,1.1,.1),
            extend='both')
plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/BOX.png')
#0.0
#0.592439146455
#0.42831456663
#1.0
#
me.min()
me.max()
#47743.550969267133
#-----------------------------------------------------------------------