from sklearn import datasets
from sklearn.model_selection import train_test_split

from sklearn import svm

from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix


#data = pd.read_csv("selected_features.csv")
data = pd.read_csv("norm-feature-selected.csv")
#data.drop(["Unnamed: 0"], axis = 1, inplace = True)   
X = data.iloc[:,0:14]  #independent columns
y = data.iloc[:,-1]    #target column i.e price range
print y
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3,random_state=1,stratify=y)


scaler = StandardScaler()

# Fit only to the training data
scaler.fit(X_train)
scaler.fit(X_test)

# Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

mlp = MLPClassifier(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
       beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(24,24,24), learning_rate='constant',
       learning_rate_init=0.001, max_iter=500)

mlp.fit(X_train,y_train)
predictions = mlp.predict(X_test)

print(confusion_matrix(y_test,predictions))

print(classification_report(y_test,predictions))
print("Accuracy:",metrics.accuracy_score(y_test, predictions))

