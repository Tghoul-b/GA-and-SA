import math
import numpy as np
import random
from matplotlib import pyplot as plt 
cities_point=[]
t=0.9
dx=[1,-1,0,0]
dy=[0,0,1,-1]
eps=1e-7
def read_date():
    max_range=-1
    with open('./data/data3.txt','r') as f:
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
def SA():
    read_date()
    step=100.0
    min_dis=1<<31
    x_min=100.0
    y_min=100.0
    process_min=[]
    while(step>eps):
        dist_list=[]
        for i in range(4):
            x_=x_min+step*dx[i]
            y_=y_min+step*dy[i]
            dist=calculate_dist(x_,y_)
            dist_list.append(dist)
            if dist<min_dis:
                min_dis=dist
                x_min=x_
                y_min=y_
        step*=t
        process_min.append(min(dist_list))
    plt.plot(process_min)
    plt.show()
    return min_dis,x_min,y_min
min_d,x,y=SA()
print(min_d,x,y)