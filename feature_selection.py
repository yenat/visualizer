import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.ensemble import ExtraTreesClassifier

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso

data = pd.read_csv("not_normalized.csv")
data.drop(["Unnamed: 0"], axis = 1, inplace = True)   
X = data.iloc[:,0:14]  #independent columns
y = data.iloc[:,-1]    #target column i.e price range
#print y
#apply SelectKBest class to extract top 10 best features

bestfeatures = SelectKBest(score_func=chi2, k=14)
fit = bestfeatures.fit(X,y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(X.columns)

#concat two dataframes for better visualization 
featureScores = pd.concat([dfcolumns,dfscores],axis=1)

featureScores.columns = ['Specs','Score']  #naming the dataframe columns
print(featureScores.nlargest(14,'Score'))  #print 10 best features

featureScores.nlargest(14,'Score').to_csv("hello.csv")
data2 = pd.read_csv("hello.csv")
Z = data2.iloc[1:14,0]

#sd = data.select(data2.iloc[1:18,0])
print Z
#data.select(featureScores.nlargest(18,'Score'))
#carrier_dff = s_df.select("rbc","pc","pcc","ba","htn","dm","cad","appet","pe","ane")
