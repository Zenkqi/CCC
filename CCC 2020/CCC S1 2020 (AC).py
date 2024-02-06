import sys, heapq
input = sys.stdin.readline

N = int(input())

rec = [tuple(map(int, input().split())) for _ in range(N)]
heapq.heapify(rec)
prev = heapq.heappop(rec)
maxima = -1000001

while len(rec):
    curr = heapq.heappop(rec)
    time, dis = curr[0]-prev[0], curr[1]-prev[1]

    if abs(dis / time) > maxima: maxima = abs(dis/time)
    prev = curr

print("%.1f" % maxima)