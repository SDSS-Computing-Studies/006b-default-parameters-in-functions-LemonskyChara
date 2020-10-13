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

def toRadians(degree):
    resultt = math.pi / 180 * degree
    return resultt


def solution(n,p):
    if n > 0 and p < 0:
        res = n
        return res
    elif n < 0 and p > 0:
        res = p
        return res


def quadratic(d,f,g):
    i = (-f + math.sqrt(f ** 2 - 4 * d * g)) / (2 * d)
    n = (-f - math.sqrt(f ** 2 - 4 * d * g)) / (2 * d)
    return i,n


def cosineLaw(q,w,e,oppositeSide=True):
        if oppositeSide == True:
                result = math.sqrt(q ** 2 + w ** 2 - 2 * q * w * math.cos(toRadians(e)))
                return result
        if oppositeSide == False:
                a1 = 1
                b1 = -2 * q * math.cos(toRadians(e))
                c1 = q ** 2 - w ** 2 
                if b1 ** 2 - 4 * a1 * c1 >= 0:
                        x1,x2=quadratic(a1,b1,c1)
                        x = solution(x1,x2)
                        return x
                else:
                        a1 = 1
                        b1 = -2 * w * math.cos(toRadians(e))
                        c1 = w ** 2 - q ** 2
                        x1,x2=quadratic(a1,b1,c1)
                        x = solution(x1,x2)
                        return x



