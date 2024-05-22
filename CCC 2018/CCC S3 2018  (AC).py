# CCC '18 S3 - RoboThieves
from collections import deque
N, M = map(int, input().split())

def isAdjacent(x, y):
    return 0 <= x < N and 0 <= y < M

directions = {
    '.': [(1, 0), (-1, 0), (0, 1), (0, -1)],
    'D': [(1, 0)],
    'U': [(-1, 0)],
    'R': [(0, 1)],
    'L': [(0, -1)],
    'C': [(1, 0), (-1, 0), (0, 1), (0, -1)]
}

conveyors = {'D', 'U', 'R', 'L'}

factory = []
for _ in range(N):
    a = list(input())
    factory.append(a)

locations = []
cameraList = []
for i in range(N):
    for j in range(M):
        if factory[i][j] == 'S':
            start = (i, j, 0) # Contains the starting indexes and the depth of the node
        if factory[i][j] == '.':
            locations.append((i, j))
        if factory[i][j] == 'C':
            cameraList.append((i, j))

cameraVision = set()
for x, y in cameraList:
    for dx, dy in directions['.']:
        newX, newY = x + dx, y + dy

        while isAdjacent(newX, newY):
            if factory[newX][newY] == 'W':
                break
            elif factory[newX][newY] not in conveyors:
                cameraVision.add((newX, newY))
            newX, newY = newX + dx, newY + dy

distance = [[-1] * M for _ in range(N)]
visited = set()

def bfs(start):
    queue = deque([start])
    visited.add(start)

    while len(queue):
        x, y, depth = queue.popleft()

        if distance[x][y] == -1:
            distance[x][y] = depth

        for dx, dy in directions['.']:
            newX, newY = x + dx, y + dy

            if isAdjacent(newX, newY):
                newX, newY = conveyorCheck(newX, newY, dx, dy)

                if (newX, newY) not in visited and factory[newX][newY] == '.' and not cameraCheck(newX, newY):
                    visited.add((newX, newY))
                    queue.append((newX, newY, depth + 1))

def conveyorCheck(newX, newY, dx, dy):
    if factory[newX][newY] in conveyors and (newX, newY) not in visited:
        visited.add((newX, newY))

        p, q = directions[factory[newX][newY]][0]
        newX, newY = newX + p, newY + q

        return conveyorCheck(newX, newY, dx, dy)
    return newX, newY


def cameraCheck(x, y): # Check if the camera can see the empty cells
    if factory[x][y] == '.' or factory[x][y] == 'S':
        if (x, y) not in cameraVision: return False
    return True

# Run
bfs(start)

for x, y in locations:
    if cameraCheck(start[0], start[1]):
        print(-1)
    else:
        print(distance[x][y])
