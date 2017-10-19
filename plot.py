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
colors = ['#FF0000', '#EE0000', '#DD0000', '#CC0000', '#BB0000', '#AA0000', '#990000', '#880000', '#770000', '#660000', '#550000', '#440000', '#330000', '#220000', '#E010FF', '#F000FF', '#00FF00', '#00DD00', '#00AA00', '#005500']
for i,fl in enumerate(values):
    plt.grid(True)
    if (i>0):
        for j,row in enumerate(fl):
            plt.plot(row, color=colors[j])
    else:
        axes = plt.gca()
        axes.set_xlim([0, max(fl[0]) * 1.1])
        axes.set_ylim([0, max(fl[1]) * 1.1])
        plt.xlabel('Диаметр внутреннего ежа, мм')
        plt.ylabel('Диаметр наружного ужа, мм')
        plt.title('Зависимость ужа от ежа')
        plt.plot(fl[0], fl[1], 'ok-')
    plt.savefig(files[i] + ".png")
    plt.clf()

