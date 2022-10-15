import random
import numpy as np
from math import pow

Set = []

def inverse(X):
    x1 = []

    for s in reversed(X):
        x1.append(s)
    
    return x1


def decompose(n):
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    while(n / 10 != 0 and i < len(x)):
        x[i] = (n % 10)
        n = int(n/10)
        i += 1
    
    x1 = inverse(x)

    return x1

def trans(X):
    p = 1
    s = 0
    for x in reversed(X):
        s += x * p
        p *= 10
    
    return s


'''*************************************** Simple Numbers *************************'''


def getValidNegNumber(n1):

    if n1 == 5:
        X = [5, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 6:
        X = [1, 5, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 7:
        X = [1, 2, 5, 6, 7, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 8:
        X = [1, 2, 3, 5, 6, 7, 8, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 9:
        X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]
    
    if n1 == 4:
        X = [1, 2, 3, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 3:
        X = [1, 2, 3, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 2:
        X = [1, 2]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 1:
        X = [1, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    return 0

def getValidPosNumber(n1):

    if n1 == 5:
        X = [1, 2, 3, 4, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 6:
        X = [1, 2, 3, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 7:
        X = [1, 2, 0]
        k = random.randint(0, len(X)-1)
        return X[k] 

    if n1 == 8:
        X = [1, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 9:
        return 0
    
    if n1 == 4:
        X = [5, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 3:
        X = [1, 5, 6, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 2:
        X = [1, 2, 5, 6, 7, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 1:
        X = [1, 2, 3, 5, 6, 7, 8, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 0:
        X = [1, 2, 3, 5, 6, 7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    return 0


def getSimpleNumber(last, l):
    ds = decompose(last)
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    t = random.randint(0, 1)
    signe = 1

    if t == 1 and last > 0:
        signe=-1

    for n in reversed(ds):

        k = 0

        if(signe == 1):
            k = getValidPosNumber(n)
        else:
            k = getValidNegNumber(n)
        
        x[i] = abs(k)
        i+=1

        if(i >= l):
            break

    x1 = inverse(x)

    return signe*trans(x1)
        

def sumList(X):
    s = 0
    for x in X:
        s+=x
    return s


'''***********************************Complexe 5 Positive***************************************'''


def initcomp5pos(n1):

    if n1 == 4:
        X = [1, 2, 3, 4, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 3:
        X = [1, 2, 3, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 2:
        X = [1, 2, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 1:
        X = [1, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 5:
        X = [5, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 6:
        X = [5, 6, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 7:
        X = [5, 6, 7, 0]
        k = random.randint(0, len(X)-1)
        return X[k] 

    if n1 == 8:
        X = [5, 6, 7, 8, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 9:
        X = [5, 6, 7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    return 0


def complex5Pos(n1):

    if n1 == 5:
        X = [1, 2, 3, 4, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 6:
        X = [2, 3, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 7:
        X = [1, 2, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 8:
        X = [1, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 0:
        X = [1, 2, 3, 5, 6, 7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 4:
        X = [1, 2, 3, 4, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 3:
        X = [2, 3, 4, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 2:
        X = [3, 4, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 1:
        X = [4, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 0:
        X = [1, 2, 3, 4, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    return 0
    


def genComplex5(last, l):
    ds = decompose(last)
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    signe = 1
    k = 0
    operation = 0

    for n in reversed(ds):

        if(n < 5):
            k += 1

        i+=1

        if(i >= l):
            break


    if(l == k):
        signe = 1
        operation = 1
    elif(k == 0):
        operation = 2
        signe = -1
    elif(l != 0):
        operation = random.randint(1, 2)
        if operation == 2:
            signe = -1

    i = 0

    for n in reversed(ds):

        z = 0

        if(operation == 2):
            z = initcomp5pos(n)
        elif operation == 1:
            z = complex5Pos(n)

        x[i] = abs(z)
        i+=1

        if(i >= l):
            break

    x1 = inverse(x)

    return signe*trans(x1)



def complex5NegInit(n1):
    if n1 == 0 :
        X = [6, 7, 8, 0]
        k = random.randint(0, len(X)-1)
        return X[k]
    
    if n1 == 1 :
        X = [5, 6, 7, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 2 :
        X = [5, 6, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 3 :
        X = [5, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 7:
        X = [1, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 6:
        X = [2, 1, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 5:
        X = [1, 2, 3, 0]
        k = random.randint(0, len(X)-1)
        return X[k]
    
    if n1 == 4:
        X = [5, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    return 0 



'''*****************************************Complexe 5 Negative***********************************************************'''



def complex5Neg(n1):

    if n1 == 9 :
        X = [1, 2, 3, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 8:
        X = [4, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 7:
        X = [3, 4, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 6:
        X = [2, 3, 4, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 5:
        X = [1, 2, 3, 4, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 4:
        X = [1, 2, 3, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 3:
        X = [1, 2, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 2:
        X = [1, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    return 0



def genComplex5Neg(last, l):
    ds = decompose(last)
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0

    signe = 1
    fivesg = 0
    operation = 0

    for n in reversed(ds):

        if n >= 5:
            fivesg += 1

        i+=1

        if(i >= l):
            break
    
    if(fivesg == l):
        signe = -1
        operation = 1
    elif(fivesg == 0):
        operation = 2
    elif(fivesg != 0):
        operation = random.randint(1, 2)
        if operation == 1:
            signe = -1

        

    i = 0

    for n in reversed(ds):

        z = 0

        if operation == 1:
            z = complex5Neg(n)
        if operation == 2:
            z = complex5NegInit(n)
        
        x[i] = abs(z)
        i+=1

        if(i >= l):
            break

    x1 = inverse(x)

    return signe*trans(x1)


'''********************************Complex 10 Positive***********************************************'''


def complex10PosInit(n1):

    if n1 == 9 :
        X = [1, 2, 3, 4, 6, 7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 8:
        X = [1, 2, 3, 5, 6, 7, 8, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 7:
        X = [1, 2, 5, 6, 7, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 6:
        X = [1, 5, 6, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 5:
        X = [5, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 4:
        X = [1, 2, 3, 4, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 3:
        X = [1, 2, 3, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 2:
        X = [1, 2, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 1:
        X = [1, 0]
        k = random.randint(0, len(X)-1)
        return X[k]
    
    return 0


def complex10Pos(n1):

    if n1 == 9 :
        X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 8:
        X = [2, 3, 4, 5, 6, 7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 7:
        X = [3, 4, 5, 6, 7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 6:
        X = [4, 5, 6, 7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 5:
        X = [5, 6, 7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 4:
        X = [6, 7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 3:
        X = [7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 2:
        X = [8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 1:
        X = [9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]
    
    if(n1 == 0):
        X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]


def genComplex10Pos(last, l):
    ds = decompose(last)
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0

    signe = 1
    fours = 0
    operation = 0

    for n in reversed(ds):

        if n == 4 or n == 9:
            fours += 1

        i+=1

        if(i >= l):
            break
    
    if(fours == l):
        signe = -1
        operation = 1
    elif(fours == 0):
        operation = 2
    elif(fours != 0):
        operation = random.randint(1, 2)
        if operation == 1:
            signe = -1

        

    i = 0

    for n in reversed(ds):

        z = 0

        if operation == 1:
            z = complex10PosInit(n)
        if operation == 2:
            z = complex10Pos(n)
        
        x[i] = abs(z)
        i+=1

        if(i >= l):
            break

    x1 = inverse(x)

    return signe*trans(x1)




'''********************************Complex 10 Negative***********************************************'''


def complex10NegInit(n1):

    if n1 == 8:
        X = [1, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 7:
        X = [1, 2, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 6:
        X = [1, 2, 3, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 5:
        X = [1, 2, 3, 4, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 4:
        X = [5, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 3:
        X = [1, 5, 6, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 2:
        X = [1, 2, 5, 6, 7, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 1:
        X = [1, 2, 3, 5, 6, 7, 8, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if(n1 == 0):
        X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]
    
    return 0


def complex10Neg(n1):

    if n1 == 9 :
        X = [9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 8:
        X = [9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 7:
        X = [8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 6:
        X = [7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 5:
        X = [6, 7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 4:
        X = [5, 6, 7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 3:
        X = [4, 5, 6, 7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 2:
        X = [3, 4, 5, 6, 7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]

    if n1 == 1:
        X = [2, 3, 4, 5, 6, 7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]
    
    if(n1 == 0):
        X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        k = random.randint(0, len(X)-1)
        return X[k]


def genComplex10Neg(last, l):
    ds = decompose(last)
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0

    signe = 1
    ones = 0
    operation = 0

    for n in reversed(ds):

        if n >= 1 and n != 5:
            ones += 1

        i+=1

        if(i >= l):
            break
    
    if(ones == l):
        signe = -1
        operation = 1
    elif(ones == 0):
        operation = 2
    elif(ones != 0):
        operation = random.randint(1, 2)
        if operation == 1:
            signe = -1

    
    if operation == 1:
        l -= 1

    i = 0
        
    for n in reversed(ds):

        z = 0

        if operation == 1:
            z = complex10Neg(n)
        if operation == 2:
            z = complex10NegInit(n)
        
        x[i] = abs(z)
        i+=1

        if(i >= l):
            break

    x1 = inverse(x)

    return signe*trans(x1)



def genManySimple(howmany, digits):
    X = []
    multiplier = int(9.9999999999 * pow(10, digits-1))
    X.append(random.randint(0, multiplier))
    i = 1

    while (i < howmany):
        s = sumList(X)
        gen = genComplex5(s, digits)
        X.append(gen)
        i+=1

    return X
