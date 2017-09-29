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

values[0] = list(zip(*values[0]))

for i,fl in enumerate(values):
    if (i>0):
        for j,row in enumerate(fl):
            plt.plot(row)
    else:
        plt.plot(fl[1])
    plt.savefig(files[i] + ".png")
    plt.clf()

