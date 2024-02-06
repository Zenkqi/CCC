import sys, heapq
input = sys.stdin.readline

c, r, d = map(int, input().split())
connections, destinations = {}, set()

for _ in range(r):
    x, y, w = map(int, input().split())
    if x not in connections: connections[x] = [(y, w)]
    else: connections[x].append((y, w))

    if y not in connections: connections[y] = [(x, w)]
    else: connections[y].append((x, w))

for _ in range(d):
    destinations.add(int(input()))

def prims(start):
    weights = [0] * 100002; weights[1] = float('inf')
    queue, visited = [], set()
    queue.append((-float('inf'), start))

    while len(queue):
        w1, v1 = heapq.heappop(queue); w1 *= -1
        if v1 in visited: continue
        visited.add(v1)
        for v2, w2 in connections[v1]:
            if min(weights[v1], w2) > weights[v2]:
                weights[v2] = min(weights[v1], w2)
                heapq.heappush(queue, (-1 * weights[v2], v2))
    return weights

mini, weights = float('inf'), prims(1)
for i in destinations:
    mini = min(mini, weights[i])
print(mini)