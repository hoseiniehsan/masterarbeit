# -*- coding: utf-8 -*-
"""
Created on Fri Nov 09 13:23:34 2018

@author: Ehsan Hosseini
Firma: Rational AG
Projekt: Masterarbeit
Arbeitspacket: 02
Aufgaben: Computational example in python emplementation of the gradient descent
is applied to find a local minimum of the function f(x)=x^2 - 3x^4 + 2
# From calculation, it is expected that the local minimum occurs at x=9/4
"""
print(__doc__)

cur_x = 6 # The algorithm starts at x=6
gamma = 0.01 # step size multiplier
precision = 0.00001
previous_step_size = 1 
max_iters = 10000 # maximum number of iterations
iters = 0 #iteration counter

df = lambda x: 4 * x**3 - 9 * x**2

while (previous_step_size > precision) & (iters < max_iters):
    prev_x = cur_x
    cur_x -= gamma * df(prev_x)
    previous_step_size = abs(cur_x - prev_x)
    iters+=1

print("The local minimum occurs at", cur_x)
#The output for the above will be: ('The local minimum occurs at', 2.2499646074278457)