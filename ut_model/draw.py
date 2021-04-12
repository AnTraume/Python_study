#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import math
import sys
from typing import List

max_angle = 15
max_dis = 0.8
resolution = 0.05
posit_x = []
posit_y = []
ut_data = [[[] for _ in range(2)] for _ in range(4)]
probability = {}
sys.stdin = open(
    "/home/antraume/py_project/visual_map/visualization/UT.txt", "r")
ut_degree = [75, 30, -30, -75]
limit = 0.8
distance_to_center = 0.26


def gamma(theta: float) -> float:
    if abs(theta) > max_angle:
        return 0.0
    else:
        return 1 - (theta/max_angle)**2


def delta(phi: float) -> float:
    return 1 - (1 + math.tanh(2 * (phi - max_dis))) / 2


def sensor_model(r, phi, theta):
    lbda = delta(phi)*gamma(theta)
    resolution_delta = resolution
    if (phi >= 0.0 and phi < r - 2 * resolution_delta * r):
        return (1 - lbda) * (0.5)
    elif(phi < r - resolution_delta * r):
        return lbda * 0.5 * pow((phi - (r - 2 * resolution_delta * r)) / (resolution_delta * r), 2) + (1 - lbda) * .5
    elif(phi < r + resolution_delta * r):
        J = (r - phi) / (resolution_delta * r)
        return lbda * ((1 - (0.5) * pow(J, 2)) - 0.5) + 0.5
    else:
        return 0.5


def trans_coordinate(source_x, source_y, theta, o_x, o_y):
    destination_x = source_x*math.cos(theta)-source_y*math.sin(theta)+o_x
    destination_y = source_x*math.sin(theta)+source_y*math.cos(theta)+o_y
    return destination_x, destination_y


def getSensorPosInRobot(degree, r):
    return r * math.cos(math.radians(degree)), r * math.sin(math.radians(degree))


def getObstaclesPosInSensor(degree, r):
    return r * math.cos(math.radians(degree)), r * math.sin(math.radians(degree))


def getPosInWord(distance, degree, theta, pos_x, pos_y):
    sensor_pos_x, sensor_pos_y = getSensorPosInRobot(
        degree, distance_to_center)
    x, y = getObstaclesPosInSensor(degree, distance)
    x, y = trans_coordinate(x, y, 0, sensor_pos_x, sensor_pos_y)
    return trans_coordinate(x, y, theta, pos_x, pos_y)


def addData(dis, degree, q, x, y, data: List[List[float]]):
    dis *= 0.01
    if dis <= limit:
        ux, uy = getPosInWord(dis, degree, q, x, y)
        data[0].append(ux), data[1].append(uy)


while True:
    try:
        ut_dis, posit = input().split(',')
    except EOFError:
        break
    x, y, q = map(float, posit.split(' '))
    ut_dis = list(map(int, ut_dis.split(' ')))
    posit_x.append(x), posit_y.append(y)
    for i in range(4):
        addData(ut_dis[i], ut_degree[i], q, x, y, ut_data[i])
plt.scatter(posit_x, posit_y, s=6)
a = np.array(posit_x)
b = np.array(posit_y)
plt.scatter(ut_data[0][1], ut_data[0][0], label="ut0", s=5)  # ut0
# plt.scatter(ut_data[1][1], ut_data[1][0], label="ut1", s=5)  # ut1
# plt.scatter(ut_data[2][1], ut_data[2][0], label="ut2", s=5)  # ut2
# plt.scatter(ut_data[3][1], ut_data[3][0], label="ut3", s=5)  # ut3
plt.legend()
plt.show()
