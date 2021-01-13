# coding: utf8
# Copyright: MathDecision

from copy import copy

def shift_data(data, cols, shifts):
    data_shifts = copy(data)
    shifted_cols = []
    for col in cols:
        for k in range(shifts):
            newcol = col + str(k + 1)
            shifted_cols.append(newcol)
            data_shifts[newcol] = data[col].shift(k)
    data_shifts = data_shifts.iloc[shifts:, :]
    return data_shifts, shifted_cols