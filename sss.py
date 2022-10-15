import random
import numpy as np

def calcSum(T):
    s = 0
    for x in T:
        s += x

    return s

def genNumb(s):
    while True:
        x = random.randint(0, 9)

        if s < 5 and x < 4:
            return x


T = []
x = random.randint(0, 9)

T.append(x)


