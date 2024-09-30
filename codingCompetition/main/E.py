import math

intIn = input()
arrLen = int(intIn.split(' ')[0])
p = int(intIn.split(' ')[1])
a = input()
a = a.split(' ')
for n in range(len(a)):
    a[n] = int(a[n])

t = p ** sum(a)
s = 0
for i in range(len(a)):
    s += int(t / (p ** a[i]))

# s %= 1000000007
# t %= 1000000007
print(s, t)
gcd = 0
minVal = min(s, t)

for g in range(0, minVal + 1):
    c = minVal - g
    if ((s % c) == 0) and ((t % c) == 0):
        gcd = c
        break

print(gcd)
