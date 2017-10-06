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

with open(files[0]) as f:
    values = [[float(x) for x in l.split()] for l in f.readlines()]


colors = ['r', 'g', 'b', 'c', '#00F0FF', '#30C0FF', '#6090FF', '#9060FF', '#C030FF', '#F000FF', '#FF0000', '#FF3030', '#FF6060', '#FF9090', '#FFC0C0', '#FFF0F0']
labels = ['0', '10', '20', '30', '40', '50', '60']

plt.grid(True)
for i,fl in enumerate(values):
    if (i > 0):
        plt.scatter(values[0], fl, color=colors[i-1], marker='v', label=labels[i-1])
plt.legend(loc='upper left', bbox_to_anchor=(0, 1))
plt.savefig(files[0] + "_diameters.png")

