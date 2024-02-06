# CCC '09 S4 - Shop and Ship
import sys, heapq

input = sys.stdin.readline

N = int(input().strip())   # Number of cities
T = int(input())    #  Number of trade routes (x, y, C(x, y))

route = [[float('inf')] * (N + 1) for _ in range(N + 1)]
for _ in range(T):
   x, y, C = map(int, input().strip().split())
   route[x][y], route[y][x] = C, C

K = int(input())           # Number of cities with a store (z, Pz)
price = [float('inf')] * (N + 1)
for _ in range(K):
    z, P = map(int, input().strip().split())
    price[z] = P

D = int(input())    # Destination city

def dijkstras(D):   # Shortest Path Algo
    dis = [float("inf")] * (N + 1)
    dis[D] = 0
    queue = [(0, D)]
    while len(queue):
        cost1, city = heapq.heappop(queue)
        if cost1 != dis[city]: continue
        for city2, cost2 in enumerate(route[city]):
            totalCost = cost1 + cost2
            if totalCost < dis[city2]:
                dis[city2] = totalCost
                heapq.heappush(queue, (totalCost, city2))
    return min([dis[i] + price[i] for i in range(1, N + 1)])

print(dijkstras(D))
