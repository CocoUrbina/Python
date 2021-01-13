# coding: utf8
# Copyright: MathDecision

from copy import copy

def descat(data, catcols):
    nocatcols = [col for col in data.columns if col not in catcols]
    datanew = copy(data[nocatcols])
    for col in catcols:
        for val in data[col].unique():
            newcol = str(col + '_' + str(val))
            datanew[newcol] = (data[col] == val).astype(int)
    return datanew
