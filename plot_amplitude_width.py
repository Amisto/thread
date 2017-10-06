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

plt.grid(True)
for i,fl in enumerate(values):
    if (i > 0):
        plt.scatter(values[0], fl[1:], color=colors[i-1], marker='v', label=str(fl[0]))
plt.legend(loc='upper left', bbox_to_anchor=(0, 1))
plt.savefig(files[0] + "_diameters.png")

