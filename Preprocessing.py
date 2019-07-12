import numpy as np
import pandas as pd
import sklearn
#import arff2csv
import category_encoders as ce
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer 
from pyspark.ml.feature import OneHotEncoder, StringIndexer
from pyspark.ml import Pipeline
from pyspark import SparkContext
from pyspark.sql import SQLContext
from sklearn import preprocessing
import numpy as np


# Read dataset from file ckd.csv

dataset = pd.read_csv("ckd.csv",header=0, na_values="?")

# Replace null values "?" by numpy.NaN(empty)
dataset.replace("?", " ")


# Fill null values with ffill (with a limit of 1) and then proceed with bfill 
dataset.fillna( method ='ffill', limit = 1, inplace = True) 
dataset.fillna(method='bfill', inplace=True)


#remove the single quotes from the column titles so as to prepare it for further processing
dataset.rename(columns={"'age'": "age", "'bp'": "bp", "'sg'": "sg","'al'": "al","'su'": "su","'rbc'": "rbc","'pc'": "pc","'pcc'": "pcc","'ba'": "ba","'bgr'": "bgr", "'bu'": "bu","'sc'": "sc","'sod'": "sod","'pot'": "pot","'hemo'": "hemo","'pcv'": "pcv","'wbcc'": "wbcc","'rbcc'": "rbcc", "'htn'": "htn","'dm'": "dm","'cad'": "cad","'appet'": "appet","'pe'": "pe","'ane'": "ane","'class'": "class"}, inplace=True)


sc = SparkContext('local','example')  # if using locally
sql_sc = SQLContext(sc)

#pandas_df = pd.read_csv(dataset,header=0,na_values="?")  # assuming the file contains a header

s_df = sql_sc.createDataFrame(dataset)


#select columns with nominal/categorical values
carrier_dff = s_df.select("rbc","pc","pcc","ba","htn","dm","cad","appet","pe","ane")
categoricalColumns = ['rbc', 'pc','pcc','ba','htn','dm','cad','appet','pe','ane']
stages = []
for categoricalCol in categoricalColumns:
    stringIndexer = StringIndexer(inputCol = categoricalCol, outputCol = categoricalCol + '_new')
    stages += [stringIndexer]

pipeline = Pipeline(stages = stages)
pipelineModel = pipeline.fit(carrier_dff)
df = pipelineModel.transform(carrier_dff)
#df.show(5)
df.toPandas().to_csv('nominals.csv')

# making data frame from csv file 
data = pd.read_csv("nominals.csv" ) 
  
# dropping passed columns 
data.drop(["rbc", "pc","pcc","ba","htn","dm","cad","appet","pe","ane"], axis = 1, inplace = True) 
data.drop(["Unnamed: 0"], axis = 1, inplace = True)   


#combine the original dataset with the changed nominal data
merged = dataset.join(data, how='right')
#merged = merged.to_csv("nominalss.csv" ) 
merged.drop(["rbc", "pc","pcc","ba","htn","dm","cad","appet","pe","ane"], axis = 1, inplace = True) 
#merged.drop(merged.columns[0], axis = 1, inplace = True)


cols = list(merged.columns.values) #Make a list of all of the columns in the df
cols.pop(cols.index('class')) #Remove b from list

#merged = merged[cols+['class']] #Create new dataframe with columns in the order you want
merged = merged[cols] # remove the 'class' column to prepare for normalization

#normalize the dataset with z-score
for col in cols:
    col_N = col + '_N'
    merged[col_N] = (merged[col] - merged[col].mean())/merged[col].std(ddof=0)


merged.to_csv("normalized.csv")

#print(merged.info())  # Descriptive info about the DataFrame
print(merged.shape)  # gives a tuple with the shape of DataFrame







