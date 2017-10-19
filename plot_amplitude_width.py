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
markers = ['o', 'v', '^', 's', 'o', 'v', '^', 's', 'o', 'v', '^', 's', 'o', 'v', '^', 's']
ls = ['-', '-', '-', '-', '--', '--', '--', '--', '-.', '-.', '-.', '-.', '..', '..', '..', '..']
plt.grid(True)
for i,fl in enumerate(values):
    if (i > 0):
        axes = plt.gca()
        axes.set_xlim([0, max(values[0]) * 1.1])
        axes.set_ylim([0, max(fl[1:]) * 1.1])
        plt.xlabel('Диаметр внутреннего ежа, мм')
        plt.ylabel('Диаметр наружного ужа, мм')
        plt.title('Зависимость ужа от ежа для разной мелкости сетки')
#        plt.plot(fl[0], fl[1], 'ok-')
        plt.plot(values[0], fl[1:], color='k', marker=markers[i-1], linestyle=ls[i-1], label=str(fl[0]))
plt.legend(loc='upper left', bbox_to_anchor=(0, 1))
plt.savefig(files[0] + "_diameters.png")

