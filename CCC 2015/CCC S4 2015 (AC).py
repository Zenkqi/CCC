# Funny Dijkstra's
import sys, heapq
input = sys.stdin.readline

K, N, M = map(int, input().split())
# Hull thickness (max), N islands, sea routes
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b, t, h = map(int, input().split())
    graph[a].append((b, h, t))
    graph[b].append((a, h, t))

def dijkstras(A, B):
    pq, marked = [(0, 0, 0, A)], dict()
    dist = [[float('inf')] * (N+1) for _ in range(N+1)]

    while len(pq):
        t1, h1, prev, v1 = heapq.heappop(pq)
        # Quick optimization, once the program sees B, it returns the t1
        # Since the heap data structure is being used, the first t1 will always be minimized
        if v1 == B: return t1

        if (prev, v1) in marked:
            # Checking marked paths to see if the curr path is usable or extraneous
            ti, hi = marked[(prev, v1)]
            if t1 >= ti and h1 >= hi:
                # A path must both have a higher hull and greater time to be discarded
                continue
        # Mark the path in a dict
        marked[(prev, v1)] = (t1, h1)

        for v2, h2, t2 in graph[v1]:
            if v2 == A: continue
            # Ignore the path that leads back to the start
            time, hull = t1 + t2, h1 + h2
            if hull < K:
                # Checks to see if this path is less than the hull
                # then finds the shortest time to it
                if time < dist[v2][v1]:
                    dist[v2][v1] = time
                heapq.heappush(pq, (time, hull, v1, v2))
    t = min(dist[B])
    return t if t != float('inf') else -1

A, B = map(int, input().split())
print(dijkstras(A, B))
