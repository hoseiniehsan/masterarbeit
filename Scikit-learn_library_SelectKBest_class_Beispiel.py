# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 14:23:02 2018

@author: Ehsan Hosseini
Firma: Rational AG
Projekt: Masterarbeit an der Tenchnische Hochschule Deggendorf
Arbeitspacket: 02
Scikit-learn library SelectKBest class Beispiel
"""

print(__doc__)

from sklearn.datasets import load_digits
from sklearn.feature_selection import SelectKBest, chi2
X, y = load_digits(return_X_y=True)
X.shape
#(1797, 64)
X_new = SelectKBest(chi2, k=20).fit_transform(X, y)
X_new.shape
#(1797, 20)