# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 15:12:38 2018

@author: Ehsan Hosseini
Firma: Rational AG
Projekt: Masterarbeit an der Tenchnische Hochschule Deggendorf
Arbeitspacket: 02
Decision Tree Reparatur Features Beispiel

"""

print(__doc__)
import pandas as pd

data = pd.DataFrame({"Gas":["True","True","True","False","True","True","True","True","True","False"],
                     "Alt":["True","True","False","True","True","True","False","False","True","False"],
                     "Sauber":["True","True","True","True","True","True","False","True","True","True"],
                     "Kalk":["True","True","False","True","True","True","False","False","True","True"],
                     "Ausfallrisiko":["hoch","hoch","niedrig","hoch","hoch","hoch","niedrig","niedrig","hoch","niedrig"]}, 
                    columns=["Elektro","Alt","Sauber","Kalk","Reparatur"])

features = data[["Gas","Alt","Sauber","Kalk"]]

target = data["Ausfallrisiko"]

print(data)