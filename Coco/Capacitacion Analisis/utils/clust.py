# coding: utf8
# Copyright: MathDecision


from matplotlib import pyplot
from sklearn.mixture import GaussianMixture
from sklearn.covariance import EllipticEnvelope
import numpy as np

def classes_histogram(vals, clas, nclas):
    pyplot.figure(figsize=(10, 5))
    for i in range(nclas):
        valsclas = [x for x, c in zip(vals, clas) if c == i]
        pyplot.hist(valsclas, bins='auto', alpha=0.5, label=str(i))
    pyplot.legend(loc='best')
    pyplot.show()


def gaussian_mixt(X, k0, k1):
    bicopt = np.inf
    kopt = 0
    clfopt = None
    for k in range(k0, k1):
        print(k)
        
        
        clf = GaussianMixture(n_components=k)
        clf.fit(X)
        newbic = clf.bic(X)
        if newbic < bicopt:
            bicopt = newbic
            kopt = k
    return GaussianMixture(n_components=kopt).fit(X)


def outliers(X, contamination, Nclusters):
    if Nclusters == 1:
        Xs = [X]
        Is = [range(len(X))]
    else:
        clf = GaussianMixture(n_components=Nclusters)
        clf.fit(X)
        y = clf.predict(X)
        Xs = []
        Is = []
        for k in range(Nclusters):
            Iclt = [i for i, yy in enumerate(y) if yy == k]
            Is.append(Iclt)
            Xclt = np.array([X[i] for i in Iclt])
            Xs.append(Xclt)
    out = []
    for Iclt, Xclt in zip(Is, Xs):
        clf = EllipticEnvelope(contamination=contamination, assume_centered=True)
        clf.fit(Xclt)
        out = [Iclt[i] for i, o in enumerate(clf.predict(Xclt)) if o == -1]
    return out


def outrate(out, y):
    Lpos = len([y[i] for i in out if y[i] == 1])
    Lneg = len(out) - Lpos
    Tpos = sum(y)
    Tneg = len(y) - Tpos
    tpr = 1.0 * Lpos / Tpos
    fpr = 1.0 * Lneg / Tneg
    print('TPR: {:.3%} \n FPR: {:.3%}'.format(tpr, fpr))