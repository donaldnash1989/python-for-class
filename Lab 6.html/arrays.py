#!/bin/usr/python
import numpy as np

def convert2Dto3D(a, e):
    l = [0]*9
    for i in range(len(e)):
        l[i] = np.empty((0,4), dtype = np.float32)

    for r in a:
        for i in range(len(e)):
            if(r[0] == e[i]):
                l[i] = np.vstack((l[i], r[1:]))

    #return np.stack(l, axis = 0)
    return np.array(l)
elements = [2003,2004,2005,2006,2007,2008,2009,2010,2011]
arr = np.array(
[[2003,54,35,43,45],
 [2003,67,37,15,26],
 [2004,90,95,43,45],
 [2004,90,95,43,45],
 [2004,73,37,15,26],
 [2005,26,54,43,45],
 [2005,26,54,43,45],
 [2006,26,54,43,45],
 [2006,26,54,43,45],
 [2007,26,54,43,45],
 [2007,26,54,43,45],
 [2008,26,54,43,45],
 [2008,26,54,43,45],
 [2009,26,54,43,45],
 [2009,26,54,43,45],
 [2010,26,54,43,45],
 [2010,26,54,43,45],
 [2011,26,54,43,45],
 [2011,18,73,15,26]],
 dtype = np.int
 )
newArr = convert2Dto3D(arr,elements)
print(newArr)
