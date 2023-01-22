import numpy as np
import pandas as pd
import math
from operator import add
import random
import matplotlib.pyplot as plt

class ship:
    def __init__(self, loc, spd):
        self.spd = spd
        self.loc = loc



locT = [0, 0, 500]
locM = [0, 0, 0]

vM = [20, 0, 0]
vT = [15, 0, 0]

sM = 70
sT = 65

def distance(l1, l2):
    dx = l1[0] - l2[0]
    dy = l1[1] - l2[1]
    dz = l1[2] - l2[2]
    distance = math.sqrt(((dx) ** 2) + ((dy) ** 2) + ((dz) ** 2))
    return [abs(dx), abs(dy), abs(dz), distance]

def velocity(dist, spd):
    velx = dist[0] / dist[3]
    vely = dist[1] / dist[3]
    velz = dist[2] / dist[3]

    direction = [velx, vely, velz]

    velocity = [x * spd for x in direction]

    return velocity

def mag(v):
    return sum(pow(x, 2) for x in v)


M = ship(locM, sM)
T = ship(locT, sT)

targetD = [10000, 0, 100]
destroyed = False

dist = [500]

while destroyed == False:

    vT = 0
    vM = 0

    if distance(T.loc, M.loc)[3] <= 300:
        newT = [T.loc[0] + random.randint(0, 60), T.loc[1] + random.randint(0, 60), T.loc[2] + random.randint(0, 60)]

        tempDt = distance(T.loc, newT)
        tempVt = velocity(tempDt, T.spd)
        vT = tempVt

        T.loc = list(map(add, T.loc, tempVt))

        print('pursuiter sighted')
    
    else:
        tempDt = distance(T.loc, targetD)
        tempVt = velocity(tempDt, T.spd)
        vT = tempVt

        T.loc = list(map(add, T.loc, tempVt))

    tempDm = distance(T.loc, M.loc)
    tempVm = velocity(tempDm, M.spd)
    vM = tempVm

    M.loc = list(map(add, M.loc, tempVm))

    print('new distance: ', distance(T.loc, M.loc)[3])

    dist.append(distance(T.loc, M.loc)[3])

    if distance(T.loc, M.loc)[3] <= 150:
        alpha = math.degrees(np.arccos((np.dot(vT, vM) / math.sqrt(mag(vT) * mag(vM) ) )))

        print(alpha)

        if alpha < 20:
            print('target destroyed')
            destroyed = True
            break
        else:
            print('not in vision\n\n')



plt.plot(dist)
plt.title('Pursuit of Two Space Ships')
plt.xlabel('Time (ticks)')
plt.ylabel('Distance')
plt.show()