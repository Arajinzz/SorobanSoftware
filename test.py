import random
import numpy as np

def calSum(soroban):
    s = 0
    p = 1
    for row in soroban:
        i = 0
        for col in row:
            s += (col * p)
            i+=1

        p *= 10
    
    return s

def addOne(soroban, row):
    for i in range(1, 5):
        if soroban[row, i] == 0:
            soroban[row, i] = 1
            return soroban
    return soroban

def subOne(soroban, row):
    for i in range(1, 5):
        if soroban[row, i] == 1:
            soroban[row, i] = 0
            return soroban
    return soroban

def addFive(soroban, row):
    soroban[row, 0] = 5
    return soroban

def subFive(soroban, row):
    soroban[row, 0] = 0
    return soroban

def addRanOne(soroban, l, r):
   
    sorobanT = np.copy(soroban)
    for i in range(0, l):
        sorobanT = addOne(sorobanT, r)
    
    return sorobanT

def subRanOne(soroban, l, r):
    
    sorobanT = np.copy(soroban)
    for i in range(0, l):
        sorobanT = subOne(sorobanT, r)
    
    return sorobanT

def getRanSo(soroban, rows):

    sorobanT = np.copy(soroban)
    r = random.randint(0, rows-1)
    f = random.randint(0, 4)
    b = True

    if f == 1:
        sorobanT = subFive(sorobanT, r)
    elif f == 0 or f == 2 :
        sorobanT = addFive(sorobanT, r)
        b = False
    
    tempR = r
    l = random.randint(0, 4)
    k = random.randint(3, 10)
    if b :
        newR = random.randint(0, rows-1)
        while(r == newR):
            newR = random.randint(0, rows-1)

        r = newR

        for _ in range(0, k):
            if tempR < r:
                sorobanT = subRanOne(sorobanT, l, r)
            else:
                sorobanT = subRanOne(sorobanT, l, tempR)
            
    else:
        for _ in range(0, k):
            sorobanT = addRanOne(sorobanT, l, r)

    
    return sorobanT

def genNonComp(soroban, howmany):
    sorobanT = np.copy(soroban)
    rows, cols = sorobanT.shape
    
    x = []
    lastsum = 0

    for i in range(0, howmany):
        sorobanT = getRanSo(sorobanT, rows)
        temp = np.copy(sorobanT)

        if len(x) == 0:
            lastsum = calSum(sorobanT)
            x.append(lastsum) 
        else:
            su = calSum(sorobanT)
            nb = su - lastsum

            k = random.randint(15, 30)
            while( nbfrequency(x, nb) > 3 and k > 0):
                sorobanT = getRanSo(temp, rows)
                su = calSum(sorobanT)
                nb = su - lastsum
                k -= 1

            lastsum = su
            x.append(nb)
    
    return x


def nbfrequency(X, nb):
    i = 0
    for x in X:
        if(nb == x):
            i+=1
    
    return i

#soroban first column 5 , others 1 each line is a column
sorobanO = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
sorobanO = sorobanO.reshape(2, 5)

x = genNonComp(sorobanO, 100)

print(x, np.sum(np.array(x)))