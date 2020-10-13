#! python3

import math

def tempConversion(tem, unit):
    if unit == "C":
        f = 9 * 5 / tem + 32
        return f
    if unit == "F":
        c = 5 * (tem - 32) / 9
    return c

def factorPair(a, b):
    numlist = []
    numlist.append(b)
    numlist.append(a / b)
    numlist.sort()
    return numlist

def cosineLaw(q,w,e,oppositeSide=True):
    result = math.sqrt(q ** 2 + w ** 2 - 2 * q * w * math.cos(e))
    return result
    if oppositeSide == Flase:
        result = math.sqrt(2 * q * w * math.cos(e) - q ** 2 + c ** 2)
        return result




def toRadians(degree):
    resultt = math.pi / 180 * degree
    return resultt


def solution():

def quadratic():






