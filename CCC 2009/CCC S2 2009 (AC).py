# Lights Going On and Off
import sys
input = sys.stdin.readline

R = int(input())
L = int(input())

grid = [list(map(int, input().split())) for _ in range(R)]
memo = [[] for _ in range(R)]; memo[-2].append(grid[-1])

count = 0
for k in range(R-1):
    # If you skip an XOR operation, nothing before that matters
    gridXOR = [[] for _ in range(k)] + [[i for i in grid[k]]]
    # the list to store the XOR chain
    for i in range(k, R - 1):
        temp = []
        for j in range(L):
            # Performs an XOR operation on the entire row
            temp.append(gridXOR[i][j] ^ grid[i+1][j])
        if temp in memo[i]:
            # Checks to see if the row has already been seen
            count += 1
            break
        memo[i].append(temp); gridXOR.append(temp)
print(R - count)