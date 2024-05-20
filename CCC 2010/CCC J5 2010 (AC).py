# CCC '10 J5 - Knight Hop
from collections import deque
A, B = map(int, input().split())

r, c = map(int, input().split())

jumps = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

def withinGraph(x, y):
    return 1 <= x <= 8 and 1 <= y <= 8

visited = set()

def bfs(a, b):
    if (a, b) == (c, r): return 0

    queue = deque()
    queue.append((a, b, 0))

    while len(queue):
        x, y, depth = queue.popleft()

        for dx, dy in jumps:
            newX, newY = x + dx, y + dy

            if withinGraph(newX, newY) and not (newX, newY) in visited:
                if (newX, newY) == (c, r): return depth + 1

                visited.add((newX, newY))
                queue.append((newX, newY, depth + 1))


print(bfs(B, A))
