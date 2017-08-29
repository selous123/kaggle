#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:04:08 2017

@author: lrh
"""
#%%
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

data = pd.read_csv("train.csv")

#print data.head(3)

#print data[0:1]['Cabin']




# print type(data.values)

#print data.describe()
#print "hello:{}".format (data.values.dtype)

#print data[0:3]["Survived"]

#print data.iat[0,3]

import os


#print "{}".format(data.iloc[0:2,:])

d = data.groupby(["Survived","Sex"]).size().reset_index().rename(columns=('Survived':'survived',"Sex":"sex","0":"data"))

print d
sns.boxplot(x="Survived",y="Sex",data=d)

plt.show()

#%%
#coding:utf-8
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
data = pd.read_csv("train.csv")

plt.subplot2grid((2,1),(0,0))
sns.kdeplot(data.Age[data.Pclass == 1])
sns.kdeplot(data.Age[data.Pclass == 2])
sns.kdeplot(data.Age[data.Pclass == 3])
plt.legend((u'1等舱', u'2等舱',u'3等舱'),loc='best')

plt.show()