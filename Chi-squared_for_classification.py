# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 14:51:18 2018

@author: Ehsan Hosseini
Firma: Rational AG
Projekt: Masterarbeit an der Tenchnische Hochschule Deggendorf
Arbeitspacket: 02
Scikit-learn library SelectKBest class Chi_squared Beispiel
"""

print(__doc__)

import sklearn
print('sklearn Version : ', sklearn.__version__)

import numpy as np

# Feature Extraction with Univariate Statistical Tests (Chi-squared for classification)
from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

from sklearn.svm import SVC # C-Support Vector Classification
from sklearn.externals.six import StringIO
from sklearn.model_selection import KFold
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import cross_val_score
import graphviz
import pydot

from sklearn import tree
from id3 import export_text
from id3 import export_graphviz
from id3 import Id3Estimator
from sklearn.tree import DecisionTreeClassifier


filename = 'Service-Reparatur.data.csv'
names = ['sauber', 'door', 'pres', 'type', 'pump', 'gas', 'kalk', 'alt', 'ausfallrisiko']
#filename = 'pima-indians-diabetes.data.csv'
#names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']



class SVC_prediction(object):
    def __init__(self, filename, names):
        SVC_prediction.call_lib
        self.filename = filename
        self.names = names
        self.load_data()
        
    def call_lib():
        import sklearn
        print('sklearn Version : ', sklearn.__version__)
        
        import numpy as np
        
        # Feature Extraction with Univariate Statistical Tests (Chi-squared for classification)
        from pandas import read_csv
        from numpy import set_printoptions
        from sklearn.feature_selection import SelectKBest
        from sklearn.feature_selection import chi2
        
        from sklearn.svm import SVC # C-Support Vector Classification
        from sklearn.externals.six import StringIO
        from sklearn.model_selection import KFold
        from sklearn.ensemble import ExtraTreesClassifier
        from sklearn.model_selection import cross_val_score
        import graphviz
        import pydot
        from sklearn import tree
        from id3 import export_text
        from id3 import export_graphviz
        from id3 import Id3Estimator
        from sklearn.tree import DecisionTreeClassifier

        return True
    
    def load_data(self):
        # load data
        filename = self.filename
        names = self.names
        dataframe = read_csv(filename, names=names)
        dataframe.ausfallrisiko[dataframe.ausfallrisiko == 1] = 'Hoch'
        dataframe.ausfallrisiko[dataframe.ausfallrisiko == 0] = 'Niedrig'
        self.features = dataframe[['sauber','type','kalk', 'alt']]
        self.target = dataframe['ausfallrisiko']        
        self.feature_names = ['sauber',
                         'type',
                         'kalk',
                         'alt']
        #array = dataframe.values
        X = dataframe.iloc[:,0:8]
        Y = dataframe.iloc[:,8]
        # feature extraction
        self.sel_KBest(X, Y, k=4)
        #show best features with columns head
        df_test = dataframe.groupby(['door', 'pump', 'gas', 'alt']).size().reset_index(name='count')
        print(df_test.iloc[0:5, :4])
        self.ensemble_accuracy(dataframe, X, Y)
        x_, y_ = self.svc_predict(dataframe, X, Y)
        self.draw_graph(x_, y_)
        return True
    
    def sel_KBest(self, X, Y, k):
        # feature extraction
        test = SelectKBest(score_func=chi2, k=4)
        fit = test.fit(X, Y)
        # summarize scores
        set_printoptions(precision=3)
        print(fit.scores_)
        features = fit.transform(X)
        # summarize selected features
        print(features[0:5,:])
        return True
    
    def ensemble_accuracy(self, dataframe, X, Y):
        # combine Models into Ensemble Predictions
        # Bagging Algorithms(Bootstrap Aggregation)
        num_trees = 17
        seed = 7
        max_features = 4
        split_point = int(len(dataframe) * 0.63)
        kfold = KFold(n_splits = split_point, random_state=seed)
        # model Extra Trees
        model = ExtraTreesClassifier(n_estimators=num_trees, max_features=max_features)
        results = cross_val_score(model, X, Y, cv=kfold)
        print("Genauigkeit mittels Extra Trees -> %.3f" % results.mean())
        return True
    
    def svc_predict(self, dataframe, X, Y):
        # prediction via C-Support Vector Classification
        clf = SVC(gamma='auto')
        clf.fit(X, Y)
        print("Prediction via C-Support Vector Classification", clf.predict(X))
        y = clf.predict(X)
        y = y.tolist()
        y = np.array(y)
        x = dataframe[['sauber','type','kalk', 'alt']]
        x = x.astype('float32')
        return x, y
    
    def draw_graph(self, x, y):
        # Decision Tree Graph
        clf = Id3Estimator()
        clf.fit(x, y, check_input=True)
        #clf.predict_proba(x)
        print(export_text(clf.tree_, self.feature_names))
        
        # export tree.dot as pdf file to write Decision Tree as a graph
        dot_data = StringIO()
        #tree.export_graphviz(clf, out_file = dot_data)
        export_graphviz(clf.tree_, 'SVC_Tree.dot', self.feature_names)
        graph = pydot.graph_from_dot_file('SVC_Tree.dot')
        graph[0].write_pdf("SVC_Tree.pdf")
        
        clf = DecisionTreeClassifier()
        clf = clf.fit(x,y)
        clf.predict(x, check_input=True)
        clf.predict_proba(x)
        
        # version v1 pdf output
        dot_data = tree.export_graphviz(clf, out_file='SVC_Tree_v1.dot')
        graph = pydot.graph_from_dot_file('SVC_Tree_v1.dot')
        graph[0].write_pdf("SVC_Tree_v1.pdf")
        
        # version v2 pdf output
        dot_data = tree.export_graphviz(clf, out_file="SVC_Tree_v2", feature_names=self.feature_names, class_names=self.target, filled=True, rounded=True, special_characters=True)
        #dot_data = tree.export_graphviz(clf, out_file="Decision-Tree-Regression-v2", feature_names=feature_names, class_names=target.name, filled=True, rounded=True, special_characters=True)
        graph = graphviz.Source(dot_data)
        # print graph this is done correct as lang as out_file=None
        graph
        
        # save graph version 2 as pdf data file
        graph = pydot.graph_from_dot_file('SVC_Tree_v2')
        graph[0].write_pdf("SVC_Tree_v2.pdf")
        return True


svc_predic = SVC_prediction(filename, names)