# coding: utf8
# Copyright: MathDecision

import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np


def plot_regularization(X, y, cols, alphas, method='ridge'):
    if method == 'ridge':
        model = linear_model.Ridge
    elif method == 'lasso':
        model = linear_model.Lasso
    else:
        raise NotImplementedError
    ms = []
    for alpha in alphas:
        reg = model(alpha=alpha).fit(X, y)
        ms.append(reg.coef_)
    ms = np.transpose(ms)
    plt.figure(figsize=(12,4))
    for m, cl in zip(ms, cols):
        plt.plot(alphas, m, label=cl)
    plt.xlabel('alpha')
    plt.legend(loc='best')
    plt.show()