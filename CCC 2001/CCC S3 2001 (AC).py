# CCC '01 S3 - Strategic Bombing
from collections import deque
roadLinks = {}
connectingRoads = set()
roads = []

while True:
    links = input()
    if links == '**': break
        
    connectingRoads.add(links)
    point1, point2 = map(str, list(links))

    if "A" not in links or 'B' not in links or point1 not in roads or point2 not in roads:
        roads.append((point1, point2))

    if point1 not in roadLinks:
        roadLinks[point1] = []

    if links[1] not in roadLinks:
        roadLinks[point2] = []

    roadLinks[point1].append(point2)
    roadLinks[point2].append(point1)


def bfs(start, eKey, eRoad):
    visited = set()
    q = deque()
    q.append(start)

    while len(q):
        point = q.popleft()
        visited.add(point)

        if not point in roadLinks: continue 
            
        for road in roadLinks[point]:
            if (point, road) != (eKey, eRoad) and (road, point) != (eKey, eRoad):
                if road not in visited:
                    q.append(road)

                if road == 'B':
                    return True

    return False


bombed = []
for point1, point2 in roads:
    if point1 + point2 not in bombed and not bfs('A', point1, point2):                        # points --> linked eg A --> C
        bombed.append(point1 + point2)

for i in bombed:
    print(i)

print('There are', len(bombed), 'disconnecting roads.')
