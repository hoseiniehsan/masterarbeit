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

sklearn.__version__

''' import libraries '''
from sklearn import tree
from sklearn.externals.six import StringIO

# conda install python-graphviz or conda install GraphViz
import graphviz #   output as graph

# pip install decision-tree-id3
from id3 import Id3Estimator
from id3 import export_graphviz #   output as pdf data file
from id3 import export_text

# Visualization
from matplotlib import pyplot


# conda install -c https://conda.binstar.org/sstromberg pydot
import pydot # Output tree

# Decisison-Tree Regression
from sklearn import tree

# Combine Models into Ensemble Predictions Bagging Algorithms
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
# Random Forest Classification

from sklearn.ensemble import RandomForestClassifier

# Confussion Matrix
from sklearn import metrics
# make random train test
from sklearn.cross_validation import train_test_split

# Bossting Algorithms
# AdaBoost Classification
from sklearn.ensemble import AdaBoostClassifier
# Stochastic Gradient Boosting
from sklearn.ensemble import GradientBoostingClassifier
# Bagging Classification
from sklearn.tree import DecisionTreeClassifier # CART
from sklearn.ensemble import BaggingClassifier
# Extra Trees
from sklearn.ensemble import ExtraTreesClassifier

import numpy as np

data = pd.DataFrame({"Gas":["True","True","True","False","True","True","True","True","True","False"],
                     "Alt":["True","True","False","True","True","True","False","False","True","False"],
                     "Sauber":["True","True","True","True","True","True","False","True","True","True"],
                     "Kalk":["True","True","False","True","True","True","False","False","True","True"],
                     "Ausfallrisiko":["hoch","hoch","niedrig","hoch","hoch","hoch","niedrig","niedrig","hoch","niedrig"]}, 
                    columns=["Gas","Alt","Sauber","Kalk","Ausfallrisiko"])

features = data[["Gas","Alt","Sauber","Kalk"]]

target = data["Ausfallrisiko"]

print(data)

feature_names = ["Alt",
                 "Kalk",
                 "type",
                 "Sauber"]

X = np.array([[900 , "True"    , "Gas"     , "True"],
              [1000, "False"   , "Gas"     , "True"],
              [1220, "other"   , "Elektro" , "False"],
              [800 , "True"    , "Gas"     , "none"],
              [680 , "False"   , "Gas"     , "none"],
              [660 , "True"    , "Elektro" , "none"],
              [860 , "other"   , "Gas"     , "True"],
              [700 , "True"    , "Gas"     , "True"],
              [680 , "False"   , "Gas"     , "True"],
              [700 , "True"    , "Elektro" , "True"],
              [680 , "other"   , "Elektro" , "True"],
              [680 , "other"   , "Elektro" , "False"],
              [680 , "False"   , "Elektro" , "False"],
              [680 , "True"    , "Elektro" , "False"],
              [680 , "False"   , "Gas"     , "False"],
              [680 , "True"    , "Gas"     , "False"],
              [680 , "other"   , "Gas"     , "False"]])

y = np.array(["Höch",
              "Höch",
              "Höch",
              "Niedrig",
              "Niedrig",
              "Niedrig",
              "M-Höch",
              "M-Höch",
              "M-Höch",
              "M-Niedrig",
              "M-Niedrig",
              "M-Niedrig",
              "M-Niedrig",
              "M-Niedrig",
              "M-Höch",
              "M-Höch",
              "M-Höch"])

clf = Id3Estimator()
clf.fit(X, y, check_input=True)

print(export_text(clf.tree_, feature_names))

# export tree.dot as pdf file to write Decision Tree as a graph
dot_data = StringIO()
#tree.export_graphviz(clf, out_file = dot_data)
export_graphviz(clf.tree_, 'Ausfallrisiko.dot', feature_names)
graph = pydot.graph_from_dot_file('Ausfallrisiko.dot')

graph[0].write_pdf("Ausfallrisiko.pdf")





# Accuracy

X = np.array([[900 , 1   , int(True)     , int(True)],
              [1000, 0  , int(True)     , int(True)],
              [1220, 2   , int(False) , int(False)],
              [800 , 1    , int(True)     , 2],
              [680 , 0   , int(True)     , 2],
              [660 , 1    , int(False) , 2],
              [860 , 2   , int(True)     , int(False)],
              [700 , 1    , int(True)     , int(True)],
              [680 , 0   , int(True)     , int(True)],
              [700 , 1    , int(False) , int(True)],
              [680 , 2   , int(False) , int(True)],
              [680 , 2   , int(False) , int(False)],
              [680 , 0   , int(False) , int(False)],
              [680 , 1    , int(False) , int(False)],
              [680 , 0   , int(True)     , int(False)],
              [680 , 1    , int(True)     , int(False)],
              [680 , 2   , int(True)     , int(False)],
              [950 , 1   , int(True)     , int(True)]
              ])
'''
y = np.array(["Höch",
              "Höch",
              "Höch",
              "Niedrig",
              "Niedrig",
              "Niedrig",
              "M-Höch",
              "M-Höch",
              "M-Höch",
              "M-Niedrig",
              "M-Niedrig",
              "M-Niedrig",
              "M-Niedrig",
              "M-Niedrig",
              "M-Höch",
              "M-Höch",
              "M-Höch"])
'''

y = np.array(["Höch",
              "Höch",
              "Höch",
              "Niedrig",
              "Niedrig",
              "Niedrig",
              "Höch",
              "Niedrig",
              "Niedrig",
              "Niedrig",
              "Niedrig",
              "Niedrig",
              "Niedrig",
              "Niedrig",
              "Höch",
              "Höch",
              "Höch",
              "Niedrig"])

'''
y = np.array([1,
              1,
              1,
              4,
              4,
              4,
              2,
              2,
              2,
              3,
              3,
              3,
              3,
              3,
              2,
              2,
              2])
'''

# plot class (target feature) Ausfallrisiko distribution
pyplot.plot(y)
pyplot.show()

# combine Models into Ensemble Predictions
# Bagging Algorithms(Bootstrap Aggregation)
num_trees = 17
seed = 7
max_features = 4
kfold = KFold(n_splits=10, random_state=7)

# model Random Forest
model = RandomForestClassifier(n_estimators = num_trees, max_features=max_features)
results = cross_val_score(model, X, y, cv=kfold)
print("Genauigkeit mittels RandomForest -> %.3f" % results.mean())

# model Bagged Decision Tree via CART Algorithm
cart = DecisionTreeClassifier()
model = BaggingClassifier(base_estimator=cart, n_estimators=num_trees, random_state=seed)
results = cross_val_score(model, X, y, cv=kfold)
print("Genauigkeit mittels Bagging -> %.3f" % results.mean())

# model Extra Trees
model = ExtraTreesClassifier(n_estimators=num_trees, max_features=max_features)
results = cross_val_score(model, X, y, cv=kfold)
print("Genauigkeit mittels Extra Trees -> %.3f" % results.mean())

# Boosting Algorithms
# AdaBoost
kfold = KFold(n_splits = 10, random_state=seed) # max n_split define as the number of samples
model = AdaBoostClassifier(n_estimators=num_trees, random_state=seed)
results = cross_val_score(model, X, y, cv=kfold)
print("Boosting Genauigkeit mittels AdaBoosting -> %.3f" % results.mean())

# Stochastic Gradient Boosting
model = GradientBoostingClassifier(n_estimators=num_trees, random_state=seed)
results = cross_val_score(model, X, y, cv=kfold)
print("Boosting Genauigkeit mittels Gradient Boosting -> %.3f" % results.mean())

# Decision-Tree Regression
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)
# ValueError: Number of features of the model must match the input. Model n_features is 4 and input n_features is 2
#clf.predict([[950, 2, int(True), int(False)]])
#clf.predict_proba([[950, 2, int(True), int(False)]])

clf.predict(X, check_input=True)
clf.predict_proba(X)

# version v1 pdf output
dot_data = tree.export_graphviz(clf, out_file='Decision-Tree-Regression.dot')

graph = pydot.graph_from_dot_file('Decision-Tree-Regression.dot')

graph[0].write_pdf("Decision-Tree-Regression.pdf")

# version v2 pdf output
dot_data = tree.export_graphviz(clf, out_file="Decision-Tree-Regression-v2", feature_names=feature_names, class_names=target, filled=True, rounded=True, special_characters=True)

#dot_data = tree.export_graphviz(clf, out_file="Decision-Tree-Regression-v2", feature_names=feature_names, class_names=target.name, filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data)
# print graph this is done correct as lang as out_file=None
graph
# save graph version 2 as pdf data file
graph = pydot.graph_from_dot_file('Decision-Tree-Regression-v2')

graph[0].write_pdf("Decision-Tree-Regression-v2.pdf")



class Compare_Algorithms(object):
    
    def __init__(self):
        # call libraries
        self.call_libraries
        
    
    def call_libraries():
        from sklearn.model_selection import KFold
        from sklearn.model_selection import cross_val_score
        from sklearn.linear_model import LogisticRegression
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.discriminant_analysis import  LinearDiscriminantAnalysis
        from sklearn.naive_bayes import GaussianNB
        from sklearn.svm import SVC # support vector classifier
    
    def evaluate(self, X, y):
        models = []
        models.append(('LR', LogisticRegression()))
        models.append(('LDA', LinearDiscriminantAnalysis()))
        models.append(('KNN', KNeighborsClassifier()))
        models.append(('CART', DecisionTreeClassifier()))
        models.append(('NB', GaussianNB())) # Naive bayes
        models.append(('SVM', SVC()))
        # evaluate models in turn
        results = []
        names = []
        scoring = 'accuracy'
        for name, model in models:
            kfold = KFold(n_splits = 10, random_state = 7)
            cv_results = cross_val_score(model, X, y, cv = kfold, scoring=scoring)
            results.append(cv_results)
            names.append(name)
            message = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
            print(message)
            
        # boxplot comparison of Algorithms
        fig = pyplot.figure()
        fig.suptitle('Algorithm Comparison')
        ax = fig.add_subplot(111)
        pyplot.boxplot(results)
        ax.set_xticklabels(names)
        pyplot.show()
        
        return True
        
    
comp_alg = Compare_Algorithms()
Compare_Algorithms.evaluate(comp_alg, X, y)

# make accuracy via sklearn metrics
logreg = LogisticRegression()
#from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
logreg.fit(X_train, y_train)
y_pred_class = logreg.predict(X_test)
# print accuracy
print("Accuracy via sklearn metrics ->", metrics.accuracy_score(y_test, y_pred_class))

# print Confussion Matrix
print("Confussion matrix", metrics.confusion_matrix(y_test, y_pred_class))
