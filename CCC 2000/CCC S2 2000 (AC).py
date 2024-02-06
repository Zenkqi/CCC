import sys
input = sys.stdin.readline


n = int(input())            # Number of initial streams
streamList = [int(input()) for _ in range(n)]

while True:
    streamIn = int(input())

    if streamIn == 99:
        splits = int(input())
        flowPercent = int(input())
        streamList.insert(splits, round(streamList[splits - 1] * (100 - flowPercent) / 100))
        streamList[splits - 1] = round(streamList[splits - 1] * flowPercent / 100)

    if streamIn == 88:
        join = int(input())

        if join < len(streamList):
            streamList[join - 1] += streamList[join]
            streamList.pop(join)

    if streamIn == 77:
        break

strs = ''
for i in streamList:
    strs += str(i) + ' '
print(strs)