def quer(x):
# Q = Square root of [(2 * C * D)/H]
    C = 50
    H = 30
    result = []
    newList = str(x).split("x")
    for i in newList:
        # result.append((2 * C * i)/H)
        num = float(newList[i])
        n = (2 * C * i)
        print(num)

quer("2,34,4")
