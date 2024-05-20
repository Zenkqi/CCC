# CCC '09 S3 - Degrees Of Separation
from collections import deque

friends ={
    1: [6],
    2: [6],
    3: [4, 5, 6, 15],
    4: [3, 5, 6],
    5: [3, 4, 6],
    6: [1, 2, 3, 4, 5, 7],
    7: [6, 8],
    8: [7, 9],
    9: [8, 10, 12],
    10: [9, 11],
    11: [10, 12],
    12: [9, 11, 13],
    13: [12, 14, 15],
    14: [13],
    15: [3,13],
    16: [17,18],
    17: [16,18],
    18: [16,17],
}

def dictAdd(x, y):
    if x in friends.keys() and y not in friends[x]:
        friends[x].append(y)

    elif x not in friends.keys():
        friends[x] = [y]

def dictRemove(x, y):
    if x in friends.keys() and y in friends[x]:
        friends[x].remove(y)

    if y in friends.keys() and x in friends[y]:
        friends[y].remove(x)


def bfs(x, y):
    visited = set()
    q = deque()
    q.append((x, 0))

    while len(q):
        node, depth = q.popleft()
        if node == y:
            return depth

        if node in friends.keys():
            for nextNode in friends[node]:
                if nextNode not in visited:
                    q.append((nextNode, depth + 1))
                    visited.add(node)
    return "Not connected"

while True:
    myInput = input()

    if myInput == 'i':          # make friends
        x = int(input())
        y = int(input())

        dictAdd(x, y)
        dictAdd(y, x)

    elif myInput == 'd':
        x = int(input())
        y = int(input())

        dictRemove(x, y)

    elif myInput == 'n':
        x = int(input())
        print(len(friends[x]))

    elif myInput == 'f':
        x = int(input())
        total = set()
        for i in friends[x]:
            for j in friends[i]:
                if j not in friends[x] and j != x:
                    total.add(j)

    elif myInput == 's':
        x = int(input())
        y = int(input())

        print(bfs(x, y))

    elif myInput == 'q':
        break

    print(friends)

