# Animal Farm
import sys, heapq
input = sys.stdin.readline
# One animal per pen
# Pens have 3 - 8 edges
# Edges can connect 2 pens or connects to the outside
# Animals assign a weight to the edges of the pens
# Determine the min cost for animals to meet in the same area 

M = int(input()) # Number of Pens

pens = [tuple(map(int, input().split())) for _ in range(M)]
# num of Edges, Edges, Cost

graph = {}

def dijkstra(graph):
    distance = [float('inf')] * N
    queue = []

    while len(queue):
        cur, v = heapq.heappop(queue)

        if cur < distance[v]:
            distance[v] = cur

        for weight, neigh in graph:
            dist = cur + weight
            if dist < graph[neigh]:
                graph[neigh] = dist
                heapq.heappush(queue, (dist, neigh))

