import matplotlib
matplotlib.use('Agg')
import matplotlib.patches as mpatches
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import itertools
from matplotlib import rcParams
from matplotlib.backends.backend_pdf import PdfPages




#fileName = 'diffrent_set_size'
fileName = 'trendsI'
folder = 'final_plot/'
perfault = []

# plot in pdf
pp = PdfPages(folder + fileName + '.pdf')

percentageU = 75
title = 'Tasks: '+ repr(10) + ', $U^N_{SUM}$:'+repr(percentageU)+'%' + ', Fault Rate:'+repr(10**-4)

plt.title(title, fontsize=20)
plt.grid(True)
plt.ylabel('$\Phi_{k,j}\cdot$j', fontsize=20)
plt.xlabel('j', fontsize=22)
ax = plt.subplot()
ax.set_yscale("log")
ax.set_xlim([0, 11])
ax.set_ylim([10**-105,10**10])
ax.tick_params(axis='both', which='major',labelsize=18)


x1 = [x+1 for x in range(10)]
"""
DAC'18
y1 = [4.85321271133951e-8, 1.76446939583656e-19, 7.27765501246738e-33, 3.55147656039182e-42, 1.32905669103551e-46, 8.07315175282262e-66, 1.94437868433586e-73, 2.81856379808910e-83, 1.29697126441990e-87, 2.24248374704863e-91]

y2 = [0.0352508010809133, 6.75655947962359e-17, 5.47107719608742e-24, 7.18410327502350e-35, 2.72714740069219e-35, 3.76367161139018e-45, 2.79954615654100e-53, 2.71409087167204e-65, 7.66494686965442e-72, 4.47955070314941e-75]
y3 = [0.000479771691708255, 3.20437610677642e-21, 4.01513158708227e-32, 1.12283078592791e-38, 3.77695649097479e-50, 1.06131114613541e-55, 6.33965733852326e-67, 1.27885540597455e-72, 1.31038431090129e-83, 3.18625979107394e-89]

y4 = [0.0439059454945871, 6.49319024126218e-10, 1.49167894794263e-15, 1.95212079714248e-21, 2.41574732217838e-29, 1.78583528961877e-37, 2.48234095193412e-42, 7.35715422189012e-48, 1.07960691062464e-57, 3.91109813706627e-58]

y5 = [5.83229986785099e-6, 7.41309980003440e-26, 1.04482910154417e-38, 1.43201875514101e-48, 7.31464892943305e-57, 3.49682120425866e-65, 3.60145304933650e-80, 3.34097656839234e-90, 5.58195386186468e-96, 5.56166773970043e-100]
"""
y1 = [0.0401672821484606, 0.00322682111151400, 0.000194418951043188, 1.04123744857124e-5, 5.22795979753804e-7, 2.51991523586149e-8, 1.18087837313895e-9, 5.42087712153575e-11, 2.44959638436969e-12, 1.09326254616842e-13]
y2 = [0.00261279117457638, 1.36533554438885e-5, 5.35100499107193e-8, 1.86414114877159e-10, 6.08826442709386e-13, 1.90888362763178e-15, 5.81876667816461e-18, 1.73751111127173e-20, 5.10722290941657e-23, 1.48267854936866e-25]
y3 = [0.0551796102557270, 0.00608957877594786, 0.000504030875217524, 3.70829696684746e-5, 2.55777976678922e-6, 1.69364748781696e-7, 1.09030609669719e-8, 6.87573319716504e-10, 4.26825312797171e-11, 2.61689493415852e-12]
y4 = [0.0584360419844310, 0.00682954200561235, 0.000598637105061598, 4.66426440064236e-5, 3.40701437928030e-6, 2.38910922371020e-7, 1.62878434719141e-8, 1.08776811995498e-9, 7.15104714678918e-11, 4.64309879224908e-12]
y5 = [0.0496187382840361, 0.00492403837779934, 0.000366486857352863, 2.42461539460408e-5, 1.50382945880381e-6, 8.95417444082519e-8, 5.18343977817062e-9, 2.93937990587555e-10, 1.64079362550368e-11, 9.04601216466464e-13]
try:
    set1,=ax.plot(x1, y1, 'r*', label='Set1')
    set2,=ax.plot(x1, y2, 'bo', label='Set2')
    set3,=ax.plot(x1, y3, 'g^', label='Set3')
    set4,=ax.plot(x1, y4, 'bs', label='Set4')
    set5,=ax.plot(x1, y5, 'rx', label='Set5')
except ValueError:
    print "ValueError"
figure = plt.gcf()
figure.set_size_inches([10,6.5])

plt.legend(handles=[set1, set2, set3, set4, set5], fontsize=12, frameon=True, loc=3)

pp.savefig()
plt.clf()
pp.close()
