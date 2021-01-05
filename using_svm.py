from sklearn import datasets
from sklearn.model_selection import train_test_split

from sklearn import svm

from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

#data = pd.read_csv("selected_features.csv")
data = pd.read_csv("norm-feature-selected.csv")
#data.drop(["Unnamed: 0"], axis = 1, inplace = True)   
X = data.iloc[:,0:14]  #independent columns
y = data.iloc[:,-1]    #target column i.e price range
print y
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3,random_state=1, stratify=y)

#Create a svm Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel

#Train the model using the training sets
clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

#print X_train
#print y_train
# Model Accuracy: how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test,y_pred))
