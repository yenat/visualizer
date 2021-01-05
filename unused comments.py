data_types = defaultdict(list)
strings_used = [var for var in data_types["StringType"] if var not in ignore]


# drop multiple columns from tables
# Import pandas package  
#import pandas as pd 
  
# create a dictionary with five fields each 
#data = { 
#    'A':['A1', 'A2', 'A3', 'A4', 'A5'],  
#    'B':['B1', 'B2', 'B3', 'B4', 'B5'],  
#    'C':['C1', 'C2', 'C3', 'C4', 'C5'],  
#    'D':['D1', 'D2', 'D3', 'D4', 'D5'],  
#    'E':['E1', 'E2', 'E3', 'E4', 'E5'] } 
  
# Convert the dictionary into DataFrame  
#df = pd.DataFrame(data) 
  
# Remove two columns name is 'C' and 'D' 
#df.drop(['C', 'D'], axis = 1) 
  
# df.drop(columns =['C', 'D']) 



# Convert nominal values to binary values
#cleanup = {"Rbc":     {"normal": 1, "abnormal": 0},
#           "Pc": {"normal": 1, "abnormal": 0},
#           "Pcc": {"present": 1, "notpresent": 0},
#           "Ba": {"present": 1, "notpresent": 0},
 #          "Htn": {"yes": 1, "no": 0},
#           "Dm": {"yes": 1, "no": 0},
#           "Cad": {"yes": 1, "no": 0},
#           "Appet": {"good": 1, "poor": 0},
#           "pe": {"yes": 1, "no": 0},
 #          "Ane": {"yes": 1, "no": 0}}

#age	'bp'	'sg'	'al'	'su'	rbc	'pc'	'pcc'	'ba'	'bgr'	'bu'	'sc'	'sod'	'pot'	'hemo'	'pcv'	'wbcc'	'rbcc'	'htn'	'dm'	'cad'	'appet'	'pe'	'ane'	'class'







#dataset.to_csv("Edited.csv", index=None)


#dataset_cp = pd.read_csv("limit.csv",header=0, na_values="?")


#encoder = ce.BinaryEncoder(cols=['rbc'])
#df_binary = encoder.fit_transform(dataset_cp)

#df_binary.to_csv("nomi.csv", sep=',',index=False)




#carrier_df = s_df.select("rbc")

#dataset_cpp = StringIndexer(inputCol="rbc",outputCol="rbc_new")
#carr_indexed = dataset_cpp.fit(carrier_df).transform(carrier_df)
#carr_indexed.show(17)
#carr_indexed.write.csv('mycsv.csv')


#dataset["rbc","pc","pcc","ba","htn","dm","cad","appet","pe","ane"]= data["rbc_new", "pc_new","pcc_new","ba_new","htn_new","dm_new","cad_new","appet_new","pe_new","ane_new"].values




#dff.toPandas().to_csv('newone.csv')

# Replace binary values into dataset
#dataset.replace(cleanup, inplace=True)



# Save this dataset file 
#dataset.to_csv("missing_filled.csv", sep=',', index=False)

from collections import defaultdict






