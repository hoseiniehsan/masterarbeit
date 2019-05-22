# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:49:53 2018

@author: Ehsan Hosseini
Firma: Rational AG
Projekt: Masterarbeit an der Tenchnische Hochschule Deggendorf
Arbeitspacket: 02
Scikit-learn library Rekursive Feature Elimination
"""

print(__doc__)

from sklearn.datasets import make_friedman1
from sklearn.feature_selection import RFE
from sklearn.svm import SVR
X, y = make_friedman1(n_samples=50, n_features=10, random_state=0)
estimator = SVR(kernel="linear")
selector = RFE(estimator, 5, step=1)
selector = selector.fit(X, y)
print(selector.support_)
print(selector.ranking_)