#! python3

import math

def tempConversion(tem,by="C"):
    if by == "C":
        answer = (tem * 9/5) + 32
    if by == "F":
        answer = 5 * (tem - 32) / 9
    answer = round(answer,1)
    return answer

def factorPair(a, b):
    numlist = []
    numlist.append(b)
    numlist.append(a / b)
    numlist.sort()
    return numlist

def toRadians(degree):
    resultt = math.pi / 180 * degree
    return resultt


def solution(n):
        n.sort()
        result = n[1]
        return result
    

def quadratic(d,f,g):
    i = (-f + math.sqrt(f ** 2 - 4 * d * g)) / (2 * d)
    n = (-f - math.sqrt(f ** 2 - 4 * d * g)) / (2 * d)
    result1 = [i,n]
    result1.sort()
    return result1


def cosineLaw(q,w,e,oppositeSide=True):
        if oppositeSide == True:
                result = math.sqrt(q ** 2 + w ** 2 - 2 * q * w * math.cos(toRadians(e)))
                return result
        if oppositeSide == False:
                a1 = 1
                b1 = -2 * q * math.cos(toRadians(e))
                c1 = q ** 2 - w ** 2 
                if b1 ** 2 - 4 * a1 * c1 >= 0:
                        Y=quadratic(a1,b1,c1)
                        x = solution(Y)
                        return x
                else:
                        a1 = 1
                        b1 = -2 * w * math.cos(toRadians(e))
                        c1 = w ** 2 - q ** 2
                        Y=quadratic(a1,b1,c1)
                        x = solution(Y)
                        return x

