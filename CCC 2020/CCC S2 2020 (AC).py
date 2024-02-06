# CCC '20 S2 - Escape Room
import sys
from collections import deque
input = sys.stdin.readline

M = int(input())  # ROWS
N = int(input())  # COLS

room = [[int(i) for i in input().split(" ")] for j in range(M)]

adjMatrix = [[] for i in range(1000005)]

for i in range(1, M + 1):
    for j in range(1, N + 1):
        adjMatrix[i * j].append(room[i - 1][j - 1])

visited = [False for _ in range(1000005)]

def bfs(cells):
    queue = deque()
    queue.append(cells)

    while len(queue):
        cell = queue.popleft()

        if cell == M * N: return True

        for newCell in adjMatrix[cell]:
            if not visited[newCell]:
                queue.append(newCell)
                visited[newCell] = True
    return False


if (M == 1 and N == 1) or bfs(room[0][0]):
    print('yes')
else:
    print('no')
