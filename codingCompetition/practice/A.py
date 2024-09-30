stdin = int(input())

stdout = 0
for i in range(stdin):
    inArr = input().split(' ')
    noOne = 0
    for n in inArr:
        if n == '1':
            noOne += 1
        if noOne == 2:
            stdout += 1
            break
print(stdout)
