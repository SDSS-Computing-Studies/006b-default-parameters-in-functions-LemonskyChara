#!python3
import math
def cosineLaw(q,w,e,oppositeSide=True):
    result = math.sqrt(q ** 2 + w ** 2 - 2 * q * w * math.cos(e))
    return result
    if oppositeSide == Flase:
        result = math.sqrt(2 * q * w * math.cos(e) - q ** 2 + c ** 2)
        return result
x = cosineLaw(10,3,50,oppositeSide=False)
print(x)