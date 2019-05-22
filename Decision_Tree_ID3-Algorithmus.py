# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:50:15 2019

@author: Ehsan Hosseini
Firma: Rational AG
Projekt: Masterarbeit an der Tenchnische Hochschule Deggendorf
Arbeitspacket: 03
Decission-Tree ID3 Algorithmus
"""

import sklearn

print(__doc__)
sklearn.__version__

''' import libraries '''
from sklearn import tree
from sklearn.externals.six import StringIO

# conda install python-graphviz or conda install GraphViz
import graphviz

# pip install decision-tree-id3
from id3 import Id3Estimator
from id3 import export_graphviz
from id3 import export_text

# load sample dataset
from sklearn.datasets import load_breast_cancer

# conda install -c https://conda.binstar.org/sstromberg pydot
import pydot


import numpy as np


# load data example #1
bunch = load_breast_cancer()

estimator = Id3Estimator()

estimator.fit(bunch.data, bunch.target)

export_graphviz(estimator.tree_, 'breast_cancer.dot', bunch.feature_names)
graph = pydot.graph_from_dot_file('breast_cancer.dot')

graph[0].write_pdf("breast_cancer.pdf")



# Example #2

feature_names = ["age",
                 "gender",
                 "sector",
                 "degree"]

X = np.array([[45, "male", "private", "m"],
              [50, "female", "private", "m"],
              [61, "other", "public", "b"],
              [40, "male", "private", "none"],
              [34, "female", "private", "none"],
              [33, "male", "public", "none"],
              [43, "other", "private", "m"],
              [35, "male", "private", "m"],
              [34, "female", "private", "m"],
              [35, "male", "public", "m"],
              [34, "other", "public", "m"],
              [34, "other", "public", "b"],
              [34, "female", "public", "b"],
              [34, "male", "public", "b"],
              [34, "female", "private", "b"],
              [34, "male", "private", "b"],
              [34, "other", "private", "b"]])

y = np.array(["(30k,38k)",
              "(30k,38k)",
              "(30k,38k)",
              "(13k,15k)",
              "(13k,15k)",
              "(13k,15k)",
              "(23k,30k)",
              "(23k,30k)",
              "(23k,30k)",
              "(15k,23k)",
              "(15k,23k)",
              "(15k,23k)",
              "(15k,23k)",
              "(15k,23k)",
              "(23k,30k)",
              "(23k,30k)",
              "(23k,30k)"])

clf = Id3Estimator()
clf.fit(X, y, check_input=True)

print(export_text(clf.tree_, feature_names))

# export tree.dot as pdf file to write Decision Tree as a graph
dot_data = StringIO()
#tree.export_graphviz(clf, out_file = dot_data)
export_graphviz(clf.tree_, 'schwangerschaft.dot', feature_names)
graph = pydot.graph_from_dot_file('schwangerschaft.dot')

graph[0].write_pdf("schwangerschaft.pdf")


