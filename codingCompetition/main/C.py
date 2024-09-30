fNum = int(input())

fIn = []
for i in range(fNum):
    fIn.append(input().split(' '))

w = 0
h = []
th = []
for g in range(len(fIn)):
    w += int(fIn[g][0])
    h.append(int(fIn[g][1]))
hPos = h.index(max(h))
h = max(h)
for g in range(len(fIn)):
    if g != hPos:
        th.append(int(fIn[g][1]))
    else:
        th.append(0)
thPos = th.index(max(th))
th = max(th)

strOut = ''
for f in range(len(fIn)):
    if f != hPos:
        rh = h
    else:
        rh = th
    if strOut:
        strOut += ' ' + str((w - int(fIn[f][0])) * rh)
    else:
        strOut = f'{(w - int(fIn[f][0])) * rh}'
print(strOut + ' ')
