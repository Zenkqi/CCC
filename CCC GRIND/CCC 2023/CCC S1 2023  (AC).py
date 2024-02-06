# Passed
C = int(input())          # Columns

ROW1 = input().split()
ROW2 = input().split()

fence = []
fence.append(ROW1)
fence.append(ROW2)

neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def isAdjacent(i, j):
    return 0 <= i <= 1 and 0 <= j < C

tape = 0
touching = 0
touched = set()
pairs = dict()

for x in range(2):
    for y in range(C):
        if int(fence[x][y]) == 1:
            tape += 3
            neigh = 0
            for dx, dy in neighbors:
                newX, newY = x + dx, y + dy
                if isAdjacent(newX, newY) and int(fence[newX][newY]) == 1:
                    if ((dx, dy) == (1, 0) or (dx, dy) == (-1, 0)):
                        if (y % 2 != 0):
                            pass
                        else:
                            neigh += 1
                            touching += 1
                    else:
                        neigh += 1
                        touching += 1

print(int(tape - touching))


