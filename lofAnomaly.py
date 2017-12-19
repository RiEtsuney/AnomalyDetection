#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:03:09 2017

@author: yueningli
"""

from sklearn.neighbors import LocalOutlierFactor
import sys
import os
import csv
import math
import random
import scipy as sp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
from sklearn import svm


os.chdir('/Users/yueningli/Documents/NetworkAnomaly/Anomaly')


data = pd.read_csv('login.csv')
rng = np.random.RandomState(42)
total=len(data)
idCount={}
for id in data['prsId']:
    idCount[id]=idCount.get(id,0.0)+1.0
#sort dictionary
idkey = sorted(idCount.iteritems(), key=lambda d:d[1], reverse = True)
#top n
n=1393
topntemp=np.array(idkey[:n])
topnkey=topntemp[:,0]
#top n contains:
totalnum=sum(topntemp[:,1])-topntemp[0][1]

from sklearn.preprocessing import OneHotEncoder


resulttemp=pd.read_csv('result3.csv')
for num in range(1,n):
    user =data[data['prsId']==topnkey[num]]
    
    length=len(user)
    col=10
    mu,sigma=0,0
    predict=np.zeros((length,col))   
    category=np.zeros((length,col))
    sa=0
    '''def loginStatusCheck(self):'''
    for i in range(0,length):
        if data['STATUS'][i]!='SUCCESS':
            predict['STATUS'][i]=0
        else: predict[i][0]=1 
    category[:,0]=1+sa
    '''def operationSystemCheck(self):'''
    osCount={}
    for os in data['OPERATING_SYSTEM']:
        osCount[os]=osCount.get(os,0.0)+1.0
    for i in range(0,length):
        if pd.isnull(data['OPERATING_SYSTEM'][i]):
            data.fillna(method='bfill')
        predict[i][1]=osCount[data['OPERATING_SYSTEM'][i]]/length
    oslen=len(osCount)
    ostmp=list(osCount)
    for i in range(0,length):
        for j in range(0,oslen):
            if data['OPERATING_SYSTEM'][i]==ostmp[j]:
                sa=np.random.normal(mu,sigma)
                category[i][1]=j+1+sa
    '''def deviceTypeCheck(self):'''
    deviceCount={}
    for dt in data['DEVICE_TYPE']:
        deviceCount[dt]=deviceCount.get(dt,0.0)+1.0
    for i in range(0,length):
        if pd.isnull(data['DEVICE_TYPE'][i]):
            data.fillna(method='bfill')
        predict[i][2]=deviceCount[data['DEVICE_TYPE'][i]]/length
    dtlen=len(deviceCount)
    dttmp=list(deviceCount)
    for i in range(0,length):
        for j in range(0,dtlen):
            if data['DEVICE_TYPE'][i]==dttmp[j]:
                sa=np.random.normal(mu,sigma)
                category[i][2]=j+1+sa
    '''def browserCheck(self):'''
    browserCount={}
    for bc in data['BROWSER']:
        browserCount[bc]=browserCount.get(bc,0.0)+1.0
    for i in range(0,length):
        if pd.isnull(data['BROWSER'][i]):
            data.fillna(method='bfill')
        predict[i][3]=browserCount[data['BROWSER'][i]]/length
    bclen=len(browserCount)
    bctmp=list(browserCount)
    for i in range(0,length):
        for j in range(0,bclen):
            if data['BROWSER'][i]==bctmp[j]:
                sa=np.random.normal(mu,sigma)
                category[i][3]=j+1+sa
    '''def connectionTypeCheck(self):'''
    connectionType={}
    for ct in data['client_connectionType']:
        connectionType[ct]=connectionType.get(ct,0.0)+1.0
    for i in range(0,length):
        if pd.isnull(data['client_connectionType'][i]):
            data.fillna(method='bfill')
        predict[i][4]=connectionType[data['client_connectionType'][i]]/length
    ctlen=len(connectionType)
    cttmp=list(connectionType)
    for i in range(0,length):
        for j in range(0,ctlen):
            if data['client_connectionType'][i]==cttmp[j]:
                sa=np.random.normal(mu,sigma)
                category[i][4]=j+1+sa
    '''def applicationNameCheck(self):'''
    appCount={}
    for an in data['APPLICATION_NAME']:
        appCount[an]=appCount.get(an,0.0)+1.0
    for i in range(0,length):
        if pd.isnull(data['APPLICATION_NAME'][i]):
            data.fillna(method='bfill')
        predict[i][5]=appCount[data['APPLICATION_NAME'][i]]/length
    aclen=len(appCount)
    acnum=np.linspace(1,aclen,aclen)
    actmp=list(appCount)
    for i in range(0,length):
        for j in range(0,aclen):
            if data['APPLICATION_NAME'][i]==actmp[j]:
                sa=np.random.normal(mu,sigma)
                category[i][5]=j+1+sa
    '''def clientCountryCheck(self):'''
    clientCountry={}
    for ccoun in data['client_country']:
        clientCountry[ccoun]=clientCountry.get(ccoun,0.0)+1.0
    for i in range(0,length):
        if pd.isnull(data['client_country'][i]):
            data.fillna(method='bfill')
        predict[i][6]=clientCountry[data['client_country'][i]]/length
    ccounlen=len(clientCountry)
    ccountmp=list(clientCountry)
    for i in range(0,length):
        for j in range(0,ccounlen):
            if data['client_country'][i]==ccountmp[j]:
                sa=np.random.normal(mu,sigma)
                category[i][6]=j+1+sa
    '''def clientCityCheck(self):'''
    clientCity={}
    for ccity in data['client_city']:
        clientCity[ccity]=clientCity.get(ccity,0.0)+1.0
    for i in range(0,length):
        if pd.isnull(data['client_city'][i]):
            data.fillna(method='bfill')
        predict[i][7]=clientCity[data['client_city'][i]]/length
    ccitylen=len(clientCity)
    ccitytmp=list(clientCity)
    for i in range(0,length):
        for j in range(0,ccitylen):
            if data['client_city'][i]==ccitytmp[j]:
                sa=np.random.normal(mu,sigma)
                category[i][7]=j+1+sa
    '''def clientISPCheck(self):'''
    clientISP={}
    for cisp in data['client_isp']:
        clientISP[cisp]=clientISP.get(cisp,0.0)+1.0
    for i in range(0,length):
        if pd.isnull(data['client_isp'][i]):
            data.fillna(method='bfill')
        predict[i][8]=clientISP[data['client_isp'][i]]/length
    cisplen=len(clientISP)
    cisptmp=list(clientISP)
    for i in range(0,length):
        for j in range(0,cisplen):
            if data['client_isp'][i]==cisptmp[j]:
                sa=np.random.normal(mu,sigma)
                category[i][8]=j+1+sa
    clientOrganization={}
    for co in data['client_organization']:
        clientOrganization[co]=clientOrganization.get(co,0.0)+1.0
    for i in range(0,length):
        if pd.isnull(data['client_organization'][i]):
            data.fillna(method='bfill')
        predict[i][9]=clientOrganization[data['client_organization'][i]]/length 
    colen=len(clientOrganization)
    cotmp=list(clientOrganization)
    for i in range(0,length):
        for j in range(0,colen):
            if data['client_organization'][i]==cotmp[j]:
                sa=np.random.normal(mu,sigma)
                category[i][9]=j+1+sa 
    
    
    
    enc = OneHotEncoder()
    enc.fit(category)  
    onehotcategory=enc.transform(category).toarray()
    classifier=LocalOutlierFactor(n_neighbors=length/2,algorithm='kd_tree')
    y_pred = classifier.fit_predict(category)
    y_predvalue=classifier.negative_outlier_factor_
    for i in range(0,length):
        if y_predvalue[i]<-2:
            #print 'Anomaly Detected at:', i
            print user.index[i]
            print user['prsId'][user.index[i]]
            resulttemp=pd.concat([resulttemp,user], axis=0)
resulttemp.to_csv('result3.csv')
