# CCC '18 S2 - Sunflowers
import copy
N = int(input())        # Num of Plants

record = []
for i in range(N):
    inputs = input().split()
    plant = [int(i) for i in inputs]
    record.append(plant)

def transposeMatrix(arr):
    matrix = copy.deepcopy(arr)
    for i in range(N):
        for j in range(i, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

def matrixRot(arr):
    matrix = transposeMatrix(arr)

    for i in range(N // 2):           # Swap [i][j], [N - i][j] = [N - i][j], [i][j]
        for j in range(N):
            matrix[i][j], matrix[N - i - 1][j] = matrix[N - i - 1][j], matrix[i][j]
    return matrix

def isSmall(matrix):
    matrixT = transposeMatrix(matrix)
    for i in range(N):
        minimaRow = min(matrix[i])
        minimaCol = min(matrixT[i])
        if minimaRow != matrix[i][0] or minimaCol != matrixT[i][0]:
            return False
    return True

for i in range(4):
    if not isSmall(record):
        record = matrixRot(record)
    else:
        break

printArr = []
for i in range(N):
    var = ''
    for j in range(N):
        var += str(record[i][j])
        var += ' '
    printArr.append(var)

for i in printArr:
    print(i)
