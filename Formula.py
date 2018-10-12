import math

def quer(x):
# Q = Square root of [(2 * C * D)/H]
    C = 50
    H = 30
    result = []
    newList = str(x).split(",")
    print(newList)
    for i in newList:
        result.append(str(int(round(math.sqrt(2*C*float(i)/H)))))
        # num = float(newList[i])
        # n = (2 * C * i)
    print (','.join(result))

quer("100,150,180")
