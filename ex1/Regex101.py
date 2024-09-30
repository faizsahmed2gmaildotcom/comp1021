f = open('regex_ex.txt', 'r')

flagList = f.read().rsplit('\n')
flagList.pop(-1)
for f in range(len(flagList)):
    listRepl = []
    for c in flagList[f]:
        listRepl.append(c)
    flagList[f] = listRepl
    for _ in range(5):
        flagList[f].pop(0)
    flagList[f].pop(-1)

for ff in flagList:
    if len(ff) == 31:
        sThree = True
        for ch in range(len(ff)):
            if ch == 20:
                sThree = sThree and (ff[ch] == "_")
            else:
                sThree = sThree and (ff[ch].isalpha() or ff[ch].isdigit())
        if sThree:
            if (ff[2] == "p") or (ff[2] == "o") or (ff[2] == "w"):
                if (ff[2] == ff[7]) and (ff[2] == ff[9]) and (ff[18] == ff[6]) and (ff[18] == ff[14]):
                    if not ff[0].isdigit():
                        strOut = ''
                        for char in ff:
                            strOut += char
                        print(strOut)
