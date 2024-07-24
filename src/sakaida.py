# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:23:45 2020

@author: toki6
"""

import numpy as np
import matplotlib.pyplot as plt


def sakaida():

    fp=open('../data/avhrr-only-v2.19881109.bin','rb')
    rsst=np.fromfile(fp,np.int16).reshape([720,1440])
    fp.close()

    fp=open('../data/N88110903_H_lon.ex','rb')
    lon=np.fromfile(fp,np.int16).reshape([4483,2048])
    fp.close()

    fp=open('../data/N88110903_H_lat.ex','rb')
    lat=np.fromfile(fp,np.int16).reshape([4483,2048])
    fp.close()

    z=np.zeros([4483,2048])
    for i in range(4483):
        if i%500==1:
            print(i)
        for j in range(2048):
            la=lat[i,j]*0.01
            lo=lon[i,j]*0.01
            x=int((lo-0.125)/0.25+0.5)
            y=int((89.875-la)/0.25+0.5)
            z[i,j]=rsst[719-y,x]*0.1-5.0

    # out_f="N88110903_H_RY.npy"
    # print(out_f)
    # np.save(out_f,z)

    tmin=5.0; tmax=30.0
    dy = 4483/256

    z2=np.zeros([4483,2048]) 
    for i in range(4483):
        for j in range(2048):
            v=z[i,j]
            if v>tmax:
                v=tmax
            if v<tmin:
                v=tmin
            z2[i,j]=v

    return z2

    cmap = plt.cm.jet
    norm = plt.Normalize(tmin,tmax)
    rgba = cmap(norm(z2))
    for i in range(4483):
        for j in range(2048):
            v=z[i,j]
            if v>35.0:
                rgba[i,j,:3] = 0, 0, 0
            if v<-1.5:
                rgba[i,j,:3] = 1, 1, 1

    return rgba


