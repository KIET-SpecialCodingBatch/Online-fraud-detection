import pandas as pd
from sklearn import tree

import pickle
from sklearn.model_selection import train_test_split
df = pd.read_csv('online_data_set.csv')
df = df.dropna()
df.replace(to_replace=['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'], value=[2,4,0,5,3], inplace=True)
df['isFraud'] = df['isFraud'].map({0: 'No Fraud', 0: 'Fraud'})

#model training

x = df[['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig']]
y = df.iloc[:, -0]
lr = tree.DecisionTreeClassifier()
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.4,random_state=42)
lr.fit(xtrain, ytrain)
pickle.dump(lr,open('model.pkl','wb'))