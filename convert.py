import numpy as np
import csv


a = np.genfromtxt('original.txt', delimiter=',')

l=[]
for y in range(np.shape(a)[0]):
    for x in range(np.shape(a)[1]):
        if not np.isnan(a[x,y]):
            l.append([y,x,a[x,y]])

with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(l)
