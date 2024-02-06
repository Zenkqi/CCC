import sys; from collections import deque
input = sys.stdin.readline

excel = [input().split() for _ in range(10)]
#print(excel)

def conv(string):
    if string.isdigit() or string == '*': return False
    neighbors, cell = string.split('+'), []
    for k in neighbors:
        index = list(k)
        print('oo', ord(index[0].lower()) - 97)
        i, j = ord(index[0].lower()) - 97, int(index[1]) - 1
        cell.append((int(i), j))
    return cell

visited = set()
def dfs(x, y, marked):
    global excel, visited
    print((x, y))
    print(excel)
    neighbors, temp = conv(excel[x][y]), 0
    print('neigh', neighbors)
    if tuple(marked) in visited:
        excel[x][y] = '*'
        return excel[x][y]
    visited.add(tuple(marked))

    if not neighbors:
        return int(excel[x][y])

    for newX, newY in neighbors:
        if (newX, newY) not in marked:
            t = dfs(newX, newY, marked.union({(newX, newY)}))
            print((newX, newY),t)
            if t == "*": temp = t; break
            temp = int(temp) + t
    excel[x][y] = str(temp)

M, N = len(excel), len(excel[0])

for i in range(M):
    for j in range(N):
        if not excel[i][j].isdigit():
            dfs(i, j, set())
#print(excel)

for i in range(M):
    print(" ".join(excel[i]))
