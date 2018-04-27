import os
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from scipy.interpolate import spline

emotions=["neutral","happiness","sadness","pride","guilt","defensive","interest","bored","impatience"]

filename="plotting.txt"
file = open(filename,'r')
timestamp=[]
features=[]
i=0
j=0
for z in range(0,9):
    features.append([])

for line in file:
    if(":" not in line):
        line=line.split(" ")
        del line[-1]
        for i in range(0,9):
            features[i].append(int(line[i]))
    else:
        time=line.split(":")
        timestamp.append(float(time[1])*60+float(time[2].strip('\n')))
print(len(features[0]))
print(len(timestamp))
T=[]
p=[]
tt=np.array(timestamp)
x=np.linspace(tt.min(),tt.max(),20)
for z in range(0,9):
    T.append(np.array(features[z]))
    p.append(spline(tt,T[z],x))
    plt.figure(emotions[z])
    plt.plot(x,p[z])
plt.show()
