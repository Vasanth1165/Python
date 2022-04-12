from math import *
def pronic(n):
    return isqrt(n) * (isqrt(n)+1) == n

n = int(input())

print('Pronic') if(pronic(n)) else print('not a pronic')