# coding: utf8
# Copyright: MathDecision

from random import randint, shuffle

def oversampling(X, y, n=None):
    X0 = [xx for xx, yy in zip(X, y) if yy < 0.5]
    y0 = [yy for xx, yy in zip(X, y) if yy < 0.5]
    X1 = [xx for xx, yy in zip(X, y) if yy > 0.5]
    y1 = [yy for xx, yy in zip(X, y) if yy > 0.5]
    n0 = len(y0)
    n1 = len(y1)
    if n is None:
        n = max(len(y0), len(y1))
    i0 = [randint(0, n0 - 1) for _ in range(n)]
    i1 = [randint(0, n1 - 1) for _ in range(n)]
    Xnew = [X0[i] for i in i0] + [X1[i] for i in i1]
    ynew = [y0[i] for i in i0] + [y1[i] for i in i1]
    ii = list(range(0, 2 * n))
    shuffle(ii)
    Xnew = [Xnew[i] for i in ii]
    ynew = [ynew[i] for i in ii]
    return Xnew, ynew


if __name__ == '__main__':
    print(oversampling([3, 4, 5, 6], [0, 0, 0, 1]))