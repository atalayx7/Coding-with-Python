myList = [1, 5, 5, -37, 15, 10]
maxNum = myList[0]
indexOfMax = 0
for i in range(1, len(myList)):
    if myList[i] > maxNum:
        maxNum = myList[i]
        indexOfMax = i
print(indexOfMax)
