# coding: utf8
# Copyright: MathDecision

import random
import numpy as np

def float_columns(data):
    return [col for col, tp in data.dtypes.iteritems() if tp == 'float64']

def qual_columns(data):
    return [col for col, tp in data.dtypes.iteritems() if tp == 'object']

def density(data, col):
    dt = data[col].values
    random.shuffle(dt)
    dt = dt if len(dt) < 20000 else dt[:20000]
    vals = set()
    x = range(1, len(dt) + 1)
    y = []
    cnt = 0
    for val in dt:
        if val not in vals:
            vals.add(val)
            cnt += 1
        y.append(cnt)
    N = len(dt) / 5
    mm = np.cov(x[N:], y[N:])
    return np.inf if mm[0, 1] < 1e-10 else -np.log10(mm[0, 1] / mm[0, 0])

def densities(data, cols):
    types = {}
    for col in cols:
        dens = density(data, col)
        if dens > 2:
            types[col] = 'f'
        elif dens > 1:
            types[col] = 's'
        else:
            types[col] = 'd'
    return types