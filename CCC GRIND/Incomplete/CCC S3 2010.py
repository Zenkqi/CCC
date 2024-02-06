import sys, copy
input = sys.stdin.readline

H = int(input())        # 0 <= H <= 1000
houses = [int(input()) for _ in range(H)] # 0 <= address < 1,000,000
k = int(input())

distance = [[] for _ in range(H)]
for index, i in enumerate(houses):
    for j in houses:
        distance[index].append(min(abs(i - j), (1000000 - i) + j))

order = sorted([(sum(distance[i]), i) for i in range(len(distance))])
print(order)

marked = []
homes = sorted(copy.deepcopy(houses))
for i in range(1, k):
    fired = homes.remove(houses[order[-i][1]])
    marked.append(fired)

print(homes)

l, r = homes[0], homes[-1]
while l <= r:
    mid = (r + l)//2
    if mid > val:
        l = mid + 1
    elif mid < val:
        r = mid - 1
    else:
        return mid

