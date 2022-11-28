import numpy as np
import csv
import argparse

parser = argparse.ArgumentParser(
                    prog = 'python3 zemaxconverter.py',
                    description = 'This program converts data from a value array to something that Zemax can understand')

parser.add_argument('--filename', dest='filename',default='original.txt', help='The name of the data file to be converted')
parser.add_argument('--output', dest='output', default='out.txt', help='The name of the data file with the output. Defaults to out.txt')
parser.add_argument('--xdel', dest='xdel', default=1.0, help='The x axis point separation. Defaults to 1.0')
parser.add_argument('--ydel', dest='ydel', default=1.0, help='The y axis point separation. Defaults to 1.0')

args = parser.parse_args()

original = np.genfromtxt(args.filename, delimiter=',')

result=[]
result.append([np.shape(original)[1], np.shape(original)[0], args.xdel, args.ydel, 0, 0.0, 0.0])

def buildLine(value):
    return [value, 0.0, 0.0, 0.0, 0]

for value in original.flatten():
    if np.isnan(value):
        result.append(buildLine(0.0))
    else:
        result.append(buildLine(value))

with open(args.output, "w", newline="") as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(result)
