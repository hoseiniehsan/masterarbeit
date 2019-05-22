# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 11:03:44 2018
@author: Ehsan Hosseini
Firma: Rational AG
Projekt: Masterarbeit an der Technische Hochschule Deggendorf
Arbeitspacket: 02
Loss function to calculate RMSE (Root Mean Square Error)

"""

import numpy as np
y_hat = np.array([0.000, 0.166, 0.333])
y_true = np.array([0.000, 0.254, 0.998])
def rmse(predictions, targets):
    differences = predictions - targets
    differences_squared = differences ** 2
    mean_of_differences_squared = differences_squared.mean()
    rmse_val = np.sqrt(mean_of_differences_squared)
    return rmse_val
print("d is: " + str(["%.8f" % elem for elem in y_hat]))
print("p is: " + str(["%.8f" % elem for elem in y_true]))
rmse_val = rmse(y_hat, y_true)
print("rms error is: " + str(rmse_val))