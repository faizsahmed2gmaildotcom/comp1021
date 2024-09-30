stdin = int(input())
stuSkill = input().split(' ')
for i in range(len(stuSkill)):
    stuSkill[i] = int(stuSkill[i])
stuSkill.sort()

stdout = 0
for s in range(0, len(stuSkill), 2):
    while stuSkill[s] < stuSkill[s + 1]:
        stuSkill[s] += 1
        stdout += 1
print(stdout)
