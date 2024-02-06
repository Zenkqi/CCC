import sys
from collections import deque

input = sys.stdin.readline

squareM = int(input())
r = int(input())
c = int(input())

grid = [list(str(input().strip())) for i in range(r)]
empty = set((i, j) for j in range(c) for i in range(r) if grid[i][j] == '.')


directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def inRoom(x, y):
    return 0 <= x < r and 0 <= y < c and grid[x][y] != 'I'

def bfs(A, B):
    visited = set()
    queue = deque()
    queue.append((A, B))

    visited.add((A, B))

    while len(queue):
        x, y = queue.popleft()

        for dx, dy in directions:
            newX, newY = x + dx, y + dy

            if inRoom(newX, newY) and (newX, newY) not in visited:
                visited.add((newX, newY))
                queue.append((newX, newY))

    return visited

marked = set()
rooms = []

for x, y in empty:
    if (x, y) not in marked:
        room = bfs(x, y)
        rooms.append(len(room))
        marked.update(room)


rooms.sort(reverse=True)
squareMIterator = squareM

if sum(rooms) < squareM:
    print(f"{len(rooms)} rooms, {squareM - sum(rooms)} square metre(s) left over")

else:
    for i in range(len(rooms)):
        squareMIterator -= rooms[i]

        if squareMIterator < 0:
            if i != 1:
                print(f"{i} rooms, {squareMIterator + rooms[i]} square metre(s) left over")
            else:
                print(f"{i} room, {squareMIterator + rooms[i]} square metre(s) left over")
            break

        elif squareMIterator == 0:
            print(f"{i + 1} rooms, {0} square metre(s) left over")
            break

