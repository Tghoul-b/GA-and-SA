import math
import numpy as np
import random
from matplotlib import pyplot as plt 
cities_point=[]
t=0.9
eps=1e-7
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def read_date():
    max_range=-1
    with open('./data/data4.txt','r') as f:
        lines=f.readlines()
        for line in lines:
            line=line.split(' ')
            temp=[int(line[0]),int(line[1])]
            max_range=max([max_range,int(line[0]),int(line[1])])
            cities_point.append(temp)
    return max_range
def calculate_dist(x,y):  #评估函数
    sum=0
    for city_point in cities_point:
        sum=sum+math.sqrt((x-city_point[0])**2+(y-city_point[1])**2)
    return sum
def three_split_helper(x):
    l=0
    r=100
    min_dis=1<<31
    while(r-l>eps):
        lmid=(l+r)/2
        rmid=(lmid+r)/2
        l_min=calculate_dist(x,lmid)
        r_min=calculate_dist(x,rmid)
        if(l_min<r_min):
            r=rmid
            min_dis=l_min
        else:
            l=lmid
            min_dis=r_min
    return lmid,min_dis
def three_split():
    read_date()
    l=0
    r=100
    min_dis=1<<31
    y=-1
    while(r-l>eps):
        lmid=(l+r)/2
        rmid=(lmid+r)/2
        l_y,l_min=three_split_helper(lmid)
        r_y,r_min=three_split_helper(rmid)
        if(l_min<r_min):
            r=rmid
            min_dis=l_min
            y=l_y
        else:
            l=lmid
            min_dis=r_min
            y=r_y
    return min_dis,l,y
min_dis,x,y=three_split()
print(min_dis,x,y)