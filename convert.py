import numpy as np
import csv


original = np.genfromtxt('original.txt', delimiter=',')

xdel=1.0
ydel=1.0

result=[]
result.append([np.shape(original)[1], np.shape(original)[0], xdel, ydel, 0, 0.0, 0.0])


def buildLine(value):
    return [value, 0.0, 0.0, 0.0, 0]


for value in original.flatten():
    if np.isnan(value):
        result.append(buildLine(0.0))
    else:
        result.append(buildLine(value))



with open("out.txt", "w", newline="") as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(result)
