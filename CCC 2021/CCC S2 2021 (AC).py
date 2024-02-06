# CCC '21 S2 - Modern Art
import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
K = int(input())

choices = [tuple(input().split()) for _ in range(K)]

rows = [0 for _ in range(M)]
cols = [0 for _ in range(N)]

for RC, RCnum in choices:
    RCnum = int(RCnum)

    if RC == "C":
        cols[RCnum - 1] += 1
    else:
        rows[RCnum - 1] += 1

counter = 0
for i in range(M):
    for j in range(N):
        if (rows[i] + cols[j]) % 2 == 1:
            counter += 1

print(counter)
