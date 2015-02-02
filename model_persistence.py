# It is possible to save a model in the scikit by using Pythons built-in persistence model, namely pickle

from sklearn import svm
from sklearn import datasets
clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X, y)  
#SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
 # kernel='rbf', max_iter=-1, probability=False, random_state=None,
  #shrinking=True, tol=0.001, verbose=False)

import pickle
s = pickle.dumps(clf)
clf2 = pickle.loads(s)
clf2.predict(X[0])
y[0]

# use joblibs replacement of pickle (joblib.dump & joblib.load) on big data
# from sklearn.externals import joblib
# joblib.dump(clf, 'filename.pkl') 


# load back the pickled model (possibly in another Python process) with:
# clf = joblib.load('filename.pkl') 
