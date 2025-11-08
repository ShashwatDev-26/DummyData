# This module is to create dummy Data

import numpy as np 
import pandas as pd
import os

class Dummydata:
    def __init__(self,sample_size:int=40,features:int=1,N_classes:int=1):
        self.sample_size = sample_size
        self.features    = features
        self.N_classes   = N_classes
        self.independent = np.full(fill_value=False,shape=(sample_size,features))
        self.dependent   = np.full(fill_value=False,shape=(sample_size,1))
        self.data_false  = True
    
    def check_false(self):
        if np.any(self.independent != type(bool)) and np.any(self.dependent != type(bool)):
            self.data_false = False
    
    def independent_data(self):
        mu = 0.1
        sg = 0.9
        self.independent = np.random.normal(mu,sg,(self.sample_size,1))
        for i in range(2,self.features+1):
            temp = np.random.normal(mu,(sg/i),(self.sample_size,1))
            self.independent = np.hstack((self.independent,temp))
        self.check_false()

    def OneHotEncoding(self):
        maxcol = np.max(self.dependent)+1
        mask   = np.zeros((self.sample_size,maxcol))
        for i in range(self.sample_size):
            mask[i,self.dependent[i]] = 1
        self.dependent = mask.copy()
        self.check_false()
    def regression_data(self):
        self.dependent = np.random.normal(0.1,0.86,(self.sample_size,1))
        self.check_false()
    def categorical_data(self):
        if self.N_classes==0:
            self.N_classes=1
        if self.N_classes>2:
            self.dependent = np.random.randint(0,self.N_classes,(self.sample_size,1))
            self.OneHotEncoding()
        else:
            self.dependent = np.random.randint(0,self.N_classes,(self.sample_size,1))
            self.check_false()
    def DataframeExport(self):
        if not self.data_false:
            indCol = [f"Feature_{i+1}" for i in range(self.independent.shape[1])]
            depCol = [f"Target_{i+1}" for i in range(self.dependent.shape[1])]
            data   = np.hstack((self.independent,self.dependent))
            df     = pd.DataFrame(data,columns=indCol+depCol)
            try:
                df.to_csv("Data/sample.csv",index=False)
            except Exception :
                os.makedirs("Data",exist_ok=True)
                df.to_csv("Data/sample.csv",index=False)
        else:
            print("[*] unable to Export invalid DataSets")

if __name__ == "__main__":
    test = Dummydata(features=2,N_classes=0)
    test.check_false()
    test.independent_data()
    test.categorical_data()
    # test.regression_data()
    print(test.independent.shape)
    print(test.dependent.shape)
    print(test.data_false)
    test.DataframeExport()