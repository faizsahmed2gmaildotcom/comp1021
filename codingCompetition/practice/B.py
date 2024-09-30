stdin = int(input())
wordArr = []
for _ in range(stdin):
    wordArr.append(input())

for w in wordArr:
    if len(w) > 10:
        stdout = f'{w[0]}{len(w) - 2}{w[-1]}'
    else:
        stdout = w
    print(stdout)
