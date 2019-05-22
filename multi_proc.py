from __future__ import print_function
import multiprocessing as mp
import os
import sys
try:
    from setuptools import setup
    from setuptools import Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension

#%load_ext Cython

def f(x):
    print(x**x)
    return x**x

output = mp.Queue()

def leistung(num, po, output):
    rnd = [pow(x, po) for x in range(1, num)]
    #for item in range(len(rnd)):
        #print(rnd[item])
    output.put(rnd)
    return rnd


if __name__ == '__main__':
    # first variate
    pool = mp.Pool(4)
    print(pool.map(f, [4,5,6,7]))

    # second variate
    p = mp.Process(target=f, args=(5, ) )
    p.start()
    p.join()


    #pool = mp.Pool(4)
    #print(pool.map(leistung, (5,3) ))
    #pool.close()
    processes = [mp.Process(target=leistung, args=(5+x,3+x,output) ) for x in range(5)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    results = [output.get() for p in processes]
    #%%time
    for item in range(len(results)):
        print("results {} is {} \n".format(item, results[item]))

    #print("results is {} \n".format( results[x] for x in range(len(results)) ) )



    #pool = mp.Pool(3)
    #print(pool.map(leistung, [{(5,3, output), (6,4, output), (7,5, output)}] ))

    output = mp.Queue()
    pool = mp.Pool(processes=4)
    #processes_01 = [pool.apply_async(leistung, args=(5*x, 2+x, output) ) for x in range(4)]
    processes_01 = [pool.apply_async(f, args=(x,) ) for x in range(4)]
    results_01 = [p.get() for p in processes_01]
    for item in range(len(results_01)):
        print("results set_01 {} is {} \n".format(item, results_01[item]))


    # run i jupyter Lab console
    # %%time
    # %run C:\Users\hoeh\PycharmProjects\SAP_import_daten\\pack\multi_proc.py