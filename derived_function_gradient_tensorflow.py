# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 15:30:13 2018

@author: Ehsan Hosseini
Firma: Rational AG
Projekt: Masterarbeit an der Tenchnische Hochschule Deggendorf
Arbeitspacket: 02
gradient function

"""

import tensorflow as tf
tf.enable_eager_execution()
"""
bei dieser Error:

NotFoundError: C:\ProgramData\Anaconda3\lib\site-packages\tensorflow\contrib\data\python\ops\..\..\_dataset_ops.so not found

falls die tfe funktioniert nicht richtig die Loesung waere :
    
follow the path and locate _dataset_ops.so

\Anaconda3\envs\tensorflow\Lib\site-packages\tensorflow\contrib\data

then move _dataset_ops.so file out of that folder to another location.

I got the same issue and doing this solved the issue.
"""
tfe = tf.contrib.eager # Shorthand for some symbols

from math import pi

def f(x):
  return tf.square(tf.sin(x))

def grad(f):
  return lambda x: tfe.gradients_function(f)(x)[0]

x = tf.lin_space(-2*pi, 2*pi, 100)  # 100 points between -2pi and +2pi

import matplotlib.pyplot as plt

plt.plot(x, f(x), label="f")
plt.plot(x, grad(f)(x), label="first derivative")
plt.plot(x, grad(grad(f))(x), label="second derivative")
plt.plot(x, grad(grad(grad(f)))(x), label="third derivative")
plt.legend()
plt.show()