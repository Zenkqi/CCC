import sys; from collections import deque
input = sys.stdin.readline

N = int(input())

friends = {}
for _ in range(N):
    x, y = map(int, input().split())
    if x not in friends:
        friends[x] = [y]
    else:
        friends[x].append(y)

check = []
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0: break
    check.append((x, y))

def bfs(r, c):
    visited = set(); visited.add(r)
    queue = deque(); queue.append((r, -1))

    while len(queue):
        x, depth = queue.popleft()

        for y in friends[x]:
            if y == c: return (True, depth + 1)
            if y not in visited:
                queue.append((y, depth + 1))
                visited.add(y)
    return False

for x, y in check:
    t = bfs(x, y)
    if t == False: print('No')

    else: print(f"Yes {t[1]}")


