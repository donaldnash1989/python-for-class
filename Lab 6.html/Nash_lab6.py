#!/bin/usr/python
import numpy as np
import os.path
import subprocess

    #Ｏ(≧▽≦)Ｏ GOOD LUCK READING THIS!!

fname = 'stock_px.csv'
delim = ','
el = []

if(os.path.isfile(fname)):
    colNames = np.genfromtxt(fname, dtype=str, delimiter=delim, max_rows=1)
    stockRaw = np.genfromtxt(fname, delimiter=delim, skip_header=1, dtype=None, names=('Date', colNames[1], colNames[2], colNames[3], colNames[4]))
    stockArray = np.array([np.array([row[0][:4], row[1], row[2], row[3], row[4]], dtype = np.float) for row in stockRaw])
    [el.append(e[0]) for e in stockArray if e[0] not in el]
else:
    print('couldn\'t find \'', fname, '\'. Please make sure the file path is correct.')

def convert2Dto3D(a, e):
    l = []*len(el)
    [l.append(np.empty((0,4), dtype = np.float)) for i in range(len(el))]
    [l.insert(i, np.vstack((l[i], np.array(r[1:], dtype = np.float))) ) for r in a for i in range(len(el)) if(r[0] == e[i])]
    return np.array(l)

stockByYear = convert2Dto3D(stockArray,el)
np.set_printoptions(precision=5, suppress=True, formatter={'float': '{: 0.3f}'.format})
print('               ', colNames[1], '   ', colNames[2], '   ', colNames[3], '   ', colNames[4])
for year in range(len(el)):
    print(2003 + year)
    print('    MIN:     ', np.amin(stockByYear[year], axis=0))
    print('    MAX:     ', np.amax(stockByYear[year], axis=0))
    print('    MEAN:    ', np.mean(stockByYear[year], axis=0))
    print('    MEDIAN:  ', np.median(stockByYear[year], axis=0))
    print('    ST. DEV.:', np.std(stockByYear[year], axis=0))
    print('    VARIANCE:', np.var(stockByYear[year], axis=0))
