myList = [3, 5, 2, 4, 1]
perms = 0

while True:
    maxNum = max(myList)
    maxIdx = myList.index(maxNum)
    while True:
        if myList[-1] != maxNum:
            myList[maxIdx] = myList[maxIdx + 1]
            myList[maxIdx + 1] = maxNum
            maxIdx += 1
            perms += 1
        else:
            myList.pop(-1)
            break
    if len(myList) == 0:
        break
print(perms)
