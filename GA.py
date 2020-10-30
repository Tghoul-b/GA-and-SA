import math
import numpy as np
import random
from matplotlib import pyplot as plt 
cities_point=[]
iterations=1000
n=100#种群规模
mutation_probability=0.3
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
    return sum#由于是要求距离的最小值,但是评价函数是针对某个函数的最大值,因此加了一个负号

def GA():
    min_dis=1<<31
    x_min=-1
    y_min=-1
    process_min=[]
    max_range=read_date()#先读入数据,数据范围是在0~100之间的,所以生成的随机数设置在0~100之间。
    chromosome=np.random.rand(n,2)*max_range
    for i in range(iterations):
        dist=[calculate_dist(chromosome[i][0],chromosome[i][1]) for i in range (n)]
        process_min.append(min(dist))
        for j in range(n):
            if(dist[j]<min_dis):
                min_dis=dist[j]
                x_min=chromosome[j][0]
                y_min=chromosome[j][1]
            dist[j]/=sum(dist)
        temp=[]
        for j in range(n):
            random_num=random.random()
            k=0
            while dist[k]<random_num:
                random_num-=dist[k]
                k=k+1
            temp.append(chromosome[k])
        chromosome=temp
        for j in range(0,n,2):
            t=chromosome[j][1]
            chromosome[j][1]=chromosome[j+1][1]
            chromosome[j+1][1]=t
        for j in range(n):
            if(random.random()<0.3):
                chromosome[j][0]=random.random()*max_range
                chromosome[j][1]=random.random()*max_range
    plt.plot(range(iterations),process_min)
    plt.show()
    return min_dis,x_min,y_min


min_d,x,y=GA()
print(min_d,x,y)

    
    