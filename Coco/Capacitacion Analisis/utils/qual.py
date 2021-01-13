# coding: utf8
# Copyright: MathDecision

import matplotlib.pyplot as plt


def pie_plots(data, cols, piecols=3):

    ncols = len(cols)

    # Adjusting figure
    pierows = (ncols - 1) / piecols + 1
    fig, axes = plt.subplots(pierows, piecols, figsize=(15.0 * piecols / 3, 4.5 * pierows))
    # if pierows == 1:
    #     axes = np.array([axes])

    for col, ax in zip(cols, axes.flatten()):
        data[col].groupby(data[col]).count().plot.pie(ax=ax)
        ax.set_title(col)

    fig.subplots_adjust(wspace=.2)
    plt.show()


def find_implications(data, cols, threshold=0.0):
    """
    :param data:
    :param cols: They must by finite valued columns
    :return:
    """
    implications = []
    N = len(data)
    for col1 in cols:
        for col2 in cols:
            if col1 != col2:
                for id, group in data[[col1, col2]].groupby(col1):
                    vals = group[col2].unique()
                    pr = 1.0 * len(group) / N
                    if len(vals) == 1 and pr > threshold:
                        implications.append((col1, id, col2, vals[0], pr, len(group), N))
    return implications


def find_negations(data, cols, threshold=0.0):
    """
    :param data:
    :param cols: They must by finite valued columns
    :return:
    """
    negations = []
    N = len(data)
    for col1 in cols:
        for col2 in cols:
            allvals = set(data[col2].unique())
            if col1 != col2:
                for id, group in data[[col1, col2]].groupby(col1):
                    vals = group[col2].unique()
                    pr = 1.0 * len(group) / N
                    if len(vals) == len(allvals) - 1 and pr > threshold:
                        negations.append((col1, id, col2, list(allvals - set(vals))[0], pr, len(group), N))
    return negations