#!/bin/python
import math
import sys
from typing import List

import matplotlib.pyplot as plt
import numpy as np
posit_x = []
posit_y = []
ut_data = [[[] for _ in range(2)] for _ in range(4)]
sys.stdin = open("./UT.txt", "r")
ut_degree0 = 75  
ut_degree1 = 30  
ut_degree2 = -30  
ut_degree3 = -75  
limit = 50


def trans_coordinate(ob_x, ob_y, theta, pos_x, pos_y):
    r_x = ob_x*math.cos(theta)-ob_y*math.sin(theta)+pos_x
    r_y = ob_x*math.sin(theta)+ob_y*math.cos(theta)+pos_y
    return r_x, r_y


def trans_posit(distance, degree, theta, pos_x, pos_y):
    distance_to_center = 26
    x = 1.0*math.cos(math.radians(degree)) * \
        (distance+distance_to_center)/100
    y = 1.0*math.sin(math.radians(degree)) * \
        (distance+distance_to_center)/100
    return trans_coordinate(x, y, theta, pos_x, pos_y)


def addData(dis, degree, q, x, y, data: List[List[float]]):
    if dis <= limit:
        ux, uy = trans_posit(dis, degree, q, x, y)
        data[0].append(ux), data[1].append(uy)

while True:
    try:
        ut_dis, posit = input().split(',')
    except EOFError:
        break
    x, y, q = map(float, posit.split(' '))
    ut_dis = list(map(int, ut_dis.split(' ')))
    posit_x.append(x), posit_y.append(y)
    addData(ut_dis[0], ut_degree0, q, x, y, ut_data[0])
    addData(ut_dis[1], ut_degree1, q, x, y, ut_data[1])
    addData(ut_dis[2], ut_degree2, q, x, y, ut_data[2])
    addData(ut_dis[3], ut_degree3, q, x, y, ut_data[3])

#sys.stdin = open("/home/antraume/UT/UT.txt", "r")
sys.stdin = open("./pose.txt", "r")
# foot_x = []
# foot_y = []
# while True:
# try:
# num,x,y,yaw = map(float,input().split())
# foot_x.append(x),foot_y.append(y)
# except EOFError:
# break
plt.scatter(posit_x,posit_y,s=6)
a = np.array(posit_x)
b = np.array(posit_y)
plt.scatter(ut_data[0][1], ut_data[0][0], label="ut0", s=3)  # ut0
plt.scatter(ut_data[1][1], ut_data[1][0], label="ut1", s=3)  # ut1
plt.scatter(ut_data[2][1], ut_data[2][0], label="ut2", s=3)  # ut2
plt.scatter(ut_data[3][1], ut_data[3][0], label="ut3", s=3)  # ut3
plt.legend()
plt.show()
