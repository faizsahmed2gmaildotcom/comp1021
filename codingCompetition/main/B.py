nChoco = int(input())
nTypes = input().split(' ')
nOut = 0

for i in range(len(nTypes)):
    nTypes[i] = int(nTypes[i])

lastN = []
while True:
    lastLen = len(nTypes)
    for i in range(len(nTypes)):
        if nTypes[i] < (i + 1):
            nTypes.pop(0)
            break
    if lastLen == len(nTypes):
        break
nTypes.reverse()

sumOut = []
for n in range(len(nTypes) - 1):
    if nTypes[n + 1] < nTypes[n]:
        sumOut.append(nTypes[n])
    else:
        sumOut.append(min(nTypes[n + 1], nTypes[n]) - 1)
        nTypes[n + 1] = sumOut[-1]

print(sum(nTypes))
