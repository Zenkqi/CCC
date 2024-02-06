import sys
from collections import deque
input = sys.stdin.readline

mapping = {
    'L' : 3,
    'M' : 2,
    'S' : 1
}

def arrange():
    arr = [mapping[i] for i in list(input().strip())]
    L, M, S = [], [], []
    for index, i in enumerate(arr):
        if i == 3:
            L.append(index)
        elif i == 2:
            M.append(index)
        elif i == 1:
            S.append(index)
    arrS = [3] * len(L) + [2] * len(M) + [1] * len(S)

    count = 0
    if arr == arrS:
        return 0

    q1, q2, q3 = [], [], []

    for i in range(len(arr)):
        if arr[i] != arrS[i] and arr[i] == 3:
            q1.append(i)

        if arr[i] != arrS[i] and arr[i] == 2:
            q2.append(i)

        if arr[i] != arrS[i] and arr[i] == 1:
            q3.append(i)
    print(arrS)
    print(arr)
    q = deque(q3 + q2 + q1)
    print(q)
    marked = [False for _ in range(len(arr))]
    print(S)
    for i in S:
        if arr[i] != arrS[i] and arr[i] == 1 and not marked[i]:
            j = q.pop()
            print((i, j))
            if arr[i] == arrS[j]:
                marked[j] = True
                marked[i] = True
            print(marked)
            #print(marked[i])
            #else:
            arr[i], arr[j] = arr[j], arr[i]
            count += 1
    print('----------------------------------------------------------------------------------------')
    print(arr)
    print(q)

    for i in range(len(arr)):
        if arr[i] != arrS[i] and arr[i] == 2 and not marked[i]:
            j = q.pop()
            if arr[i] == arrS[j]:
                marked[j] = True
            #else:
            arr[i], arr[j] = arr[j], arr[i]
            count += 1

    print(deque)
    print(arr)

    return count

print(arrange())
