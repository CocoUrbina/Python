# coding: utf8
# Copyright: MathDecision

import matplotlib.pyplot as plt
from sklearn import linear_model

def plot_regresions(data, threshold_up=0.9, threshold_down=0.1):
    numcols = len(data.columns)
    if numcols == 1:
        raise NotImplementedError('El número de columnas debe ser mayor a 1')
    reg = linear_model.LinearRegression()
    fig, axs = plt.subplots(numcols, numcols, sharex='col', sharey='row', figsize=(25, 25))
    for i, colx in enumerate(data.columns):
        for j, coly in enumerate(data.columns):
            if i == 0:
                axs[i, j].xaxis.set_label_position('top')
                axs[i, j].set_xlabel(coly)
            if j == 0:
                axs[i, j].set_ylabel(colx)
            reg.fit(data[[colx]].values, data[coly].values)
            b = reg.intercept_
            m = reg.coef_[0]
            r2 = reg.score(data[[colx]].values, data[coly].values)
            axs[i, j].scatter(data[[colx]].values, data[coly].values, color='black', alpha=0.5)
            axs[i, j].plot(data[[colx]].values, reg.predict(data[[colx]].values),
                     color='red', linewidth=3, label='m: {:.2f}\nb: {:.2f}\nR2: {:.2f}'.format(m, b, r2))
            axs[i, j].legend(loc='best')
            if i == j:
                pass
            elif r2 > threshold_up:
                axs[i, j].set_facecolor('green')
            elif r2 < threshold_down:
                axs[i, j].set_facecolor('gray')
            else:
                axs[i, j].set_facecolor('blue')
    plt.show()