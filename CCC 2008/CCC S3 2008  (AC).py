# CCC '08 S3 - Maze
import sys
from collections import deque

input = sys.stdin.readline

symbols = {
    "+" : [(1, 0), (-1, 0), (0, 1), (0, -1)],
    "|" : [(1, 0), (-1, 0)],
    "-" : [(0, 1), (0, -1)],
    "*" : []
}

def isAdjacent(x, y, visitedList):
    return 0 <= x < r and 0 <= y < c and not (x, y) in visitedList

def bfs(r, c, M, N, intersection):
    visited = set()
    if len(intersection) == 1 and len(intersection[0]) <= 2: return 1

    queue = deque()
    queue.append((r, c, 1))
    visited.add((r, c))

    while len(queue):
        x, y, depth = queue.popleft()

        for dx, dy in symbols[intersection[x][y]]:
            newX, newY = x + dx, y + dy

            if (newX, newY) == (M - 1, N - 1) and intersection[newX][newY] != "*":
                return depth + 1

            if isAdjacent(newX, newY, visited) and intersection[newX][newY] != "*":
                visited.add((newX, newY))
                queue.append((newX, newY, depth + 1))

    return -1


t = int(input())            # Number of cases

for i in range(t):
    r = int(input())            # Rows
    c = int(input())            # Cols

    intersections = [list(input()) for _ in range(r)]

    print(bfs(0, 0, r, c, intersections))

