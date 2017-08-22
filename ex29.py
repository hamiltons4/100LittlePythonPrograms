import math


def lVolume(h, r = 10):
    return (4*math.pi*r**3)/3 - (math.pi*h**2*(3*r - h))/3

print(lVolume(2))


#from math import pi
