#!/usr/bin/python3

import argparse
import os
import png
import csv
import matplotlib
matplotlib.use('Agg')
matplotlib.rc('font', family='DejaVu Sans')
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
ns = []
for i in range(1, len(values)):
    ns.append(values[i][0])

print(ns)

data = []
for i in range(1, len(values[0])):
    _points = []
    for j in range(1, len(values)):
        _points.append(values[j][i])
    data.append(_points)

for i in range(0, len(data)):
    print(data[i])
    print(values[0][i])
    axes = plt.gca()
    axes.set_xlim([0, values[len(values)-1][0] * 1.1])
    axes.set_ylim([0, max(data[i]) * 1.1])
    plt.grid(True)
    plt.xlabel('Мелкость сетки, ячеек на длину нити')
    plt.ylabel('Диаметр отверстия, мм')
    plt.title('Сходимость по сетке, решение для амплитуды импульса ' + str(float(values[0][i]/1e9)) + ' ГПа')
    plt.plot(ns, data[i], color='k', marker='o', linestyle='-')
    plt.savefig("test_" + files[0] + "_" + str(i) + "_diameters.png")
    plt.clf()

