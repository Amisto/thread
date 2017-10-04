#!/usr/bin/python3

import argparse
import os
import png
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser(description=' ')

parser.add_argument(
    'files',
    metavar='FILES',
    nargs='+',
    help='List of CSV files with data'
)

args = parser.parse_args()

files = []
for f in args.files:
    fname = os.path.basename(f)
    files.append(f)

values = []
for fpath in files:
    with open(fpath) as f:
        values.append([[float(x) for x in l.split()] for l in f.readlines()])

for i,fl in enumerate(values):
    values[i] = list(zip(*values[i]))

colors = ['r', 'g', 'b', 'c', '#00F0FF', '#30C0FF', '#6090FF', '#9060FF', '#C030FF', '#F000FF', '#FF0000', '#FF3030', '#FF6060', '#FF9090', '#FFC0C0', '#FFF0F0']
labels = ['cos^2', 'cos^4', 'cos', 'sq', 'tri']

#ax = plt.subplot(111)
plt.grid(True)
#box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
for i,fl in enumerate(values):
#    for j,row in enumerate(fl):
    plt.semilogx(fl[0], fl[1], color=colors[i], marker='v', label=labels[i])
plt.legend(loc='upper left', bbox_to_anchor=(0, 1))
plt.axis([5.0, 145.0, 0.0, 150.0])
plt.savefig(files[0] + "_diameters.png")
    #plt.clf()

