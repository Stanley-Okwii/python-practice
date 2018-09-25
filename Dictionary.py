def createDictionary(x):
    intDictionary = dict()
    for i in range(1, x + 1):
        # intDictionary.
        # position = i + 1
        intDictionary[i] = i * i
    return intDictionary

print(createDictionary(8))
