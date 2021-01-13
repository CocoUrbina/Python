# coding: utf8
# Copyright: MathDecision

from sklearn import metrics
import matplotlib.pyplot as plt


def adjustedR2(r2, n, p):
    return r2 - (1 - r2) * p / (n - p - 1)


def draw_roc(clf, X, y):
    yp = clf.predict_proba(X)
    yp = [yy[1] for yy in yp]
    fpr, tpr, thresholds = metrics.roc_curve(y, yp, pos_label=1)
    plt.figure(figsize=(8, 4))
    plt.plot(fpr, tpr)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Curva ROC')
    plt.show()