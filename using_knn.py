from sklearn import datasets
from sklearn.model_selection import train_test_split

from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.neighbors import KNeighborsClassifier


#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

#data = pd.read_csv("selected_features.csv")
data = pd.read_csv("norm-feature-selected.csv")
#data.drop(["Unnamed: 0"], axis = 1, inplace = True)   
X = data.iloc[:,0:14]  #independent columns
y = data.iloc[:,-1]    #target column i.e price range
print y
#split dataset into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

# Create KNN classifier
knn = KNeighborsClassifier(n_neighbors = 3)
# Fit the classifier to the data
knn.fit(X_train,y_train)

knn.predict(X_test)
#check accuracy of our model on the test data
print knn.score(X_test, y_test)
#print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

