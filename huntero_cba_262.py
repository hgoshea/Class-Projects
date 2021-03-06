# -*- coding: utf-8 -*-
"""HunterO_CBA_262.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RGmXXcysMHBXIWv5-SkAGZd1zD9yTIWT
"""

from google.colab import drive
drive.mount('/content/drive')


import pandas as pd
import math
#reading data into a panda's dataframe

dataT=pd.read_csv('/content/drive/MyDrive/262-CBA.csv')
print(dataT)

discountRate=0.05
discountFactor=[0,0,0,0]
for year in dataT['years']:
  discountFactor[year]=1/math.pow((1+discountRate),year)

dataT['discountFactor']=[round(num, 2) for num in discountFactor]
print (dataT)

#calculate Net benefit/cost for each year
NetBC=[0,0,0,0]
for year in dataT['years']:
  NetBC[year]=dataT['developmentCost'][year]+dataT['operationalCost'][year]+dataT['valueOfBenefits'][year]

dataT['NetBC']=NetBC
print (dataT)


#calculate net present value

NPV=[0,0,0,0]

for year in dataT['years']:
  NPV[year]=dataT['NetBC'][year]*dataT['discountFactor'][year]

dataT['NPV']=[round(num, 2) for num in NPV]
print(dataT)
