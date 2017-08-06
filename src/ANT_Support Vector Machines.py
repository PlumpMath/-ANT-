# -*- coding: utf-8 -*-
""" 
Python Script
Created on  Sunday August 2017 10:17:41 
@author:  Mahmoud AbdelRahman

[desc]
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

    - Effective in high dimensional spaces. 
    - Still effective in cases where number of dimensions is greater than the number of samples. 
    - Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient. 
    - Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels. 

The disadvantages of support vector machines include:

    - If the number of features is much greater than the number of samples, the method is likely to give poor performances. 
    - SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation. 
    
The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.

[\desc]

ARGUMENTS:  
    _data = data
    _target = target
    _features = features
    _predict = predict
    _algorithm = Support Vector Machines Algorithm\nint value, default(1) \nOptions: \n1->Support Vector Classifier SVC\n2->Linear Support Vector Classifier LinSVC\n3->Nu Support Vector Classifier NuSVC\n4->Support Vector Regression SVR\n5->Linear Support Vector Regression LinSVR\n6->Nu Support Vector Regression NuSVR\n7->One Class Support Vector Machines\n


RETURN: 
    log_ = output log
    output_ = predict Data
    score_ score value
"""


import numpy as np


_data = np.array(_data)
_target = np.array(_target)

if(_algorithm == None):
    _algorithm =1 

if _algorithm == 1:
    from sklearn.svm import SVC
    
    model = SVC()
    model.fit(_data,_target)
    log_ = "Support Vector Classification SVC"
    
elif _algorithm ==2:
    from sklearn.svm import LinearSVC
    
    model = LinearSVC()
    model.fit(_data,_target)
    log_ = "Linear Support Vector Classification LinearSVC"
    
elif _algorithm == 3:
    from sklearn.svm import NuSVC
    model = NuSVC()
    model.fit(_data,_target)
    log_ = "Nu Support Vector Classification NuSVC"
elif _algorithm == 4:
    from sklearn.svm import SVR
    
    model = SVR()
    model.fit(_data,_target)
    log_ = "Support Vector Regression SVR"
    
elif _algorithm ==5:
    from sklearn.svm import LinearSVR
    
    model = LinearSVR()
    model.fit(_data,_target)
    log_ = "Linear Support Vector Regression LinearSVR"
   
elif _algorithm == 6:
    from sklearn.svm import NuSVR
    model = NuSVR()
    model.fit(_data,_target)
    log_ = "Nu Support Vector Regression NuSVR"

elif _algorithm == 7:
    from sklearn.svm import OneClassSVM
    
    model = OneClassSVM()
    model.fit(_data,_target)
    log_ = "One Class Support Vector Machines"


if(_features != None):
    output_ = _features[model.predict(_predict)]
else:
    output_ = model.predict(_predict)


score_ = model.score(_data, _target)