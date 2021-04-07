import matplotlib as plt
import math

max_angle = 15
max_dis = 0.8
resolution = 0.05


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
    t = pow((phi-r)/resolution_delta, 2)
    if phi >= 0 and phi <= r - 2 * resolution_delta:
        return 0.5 * (1 - lbda)
    elif phi <= r - resolution_delta:
        return 0.5 * lbda * (2+t)
    elif phi < r + resolution_delta:
        return 0.5 * lbda * (1 - t)
    else:
        return 0.5

