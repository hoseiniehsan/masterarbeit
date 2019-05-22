from __future__ import print_function

try:
    from setuptools import setup
    from setuptools import Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension


import sys
import os

def f(x):
    print(x**x)
    return x**x


def leistung(num, po, output=None):
    rnd = [pow(x, po) for x in range(1, num)]
    #for item in range(len(rnd)):
        #print(rnd[item])
    return rnd


if __name__ == '__main__':
    result_01 = [f(x) for x in [4,5,6,7]]
    print("\n", result_01)

    result_01 = [f(x) for x in [4, 5, 6, 7]]
    print("\n", result_01)

    result_02 = [ leistung(5+x,3+x) for x in range(5)]
    for item in range(len(result_02)):
        print("results {} is {} \n".format(item, result_02[item]))

    result_03 = [f(x) for x in range(4)]
    for item in range(len(result_03)):
        print("results {} is {} \n".format(item, result_03[item]))