# CCC '01 S2 - Spirals
from math import ceil, floor, sqrt

x = int(input())
y = int(input('\n'))

characters = y - x + 1
rows = ceil(sqrt(characters))
cols = floor(sqrt(characters))
remainder = (characters - (cols ** 2))

if remainder > cols:
    cols += 1


spiralList = [[' '] * cols for _ in range(rows)]

def middle(X):              # Returns the middle number
    if X % 2 == 0:
        return X // 2 - 1
    else:
        return X // 2

i, j = middle(rows), middle(cols)
placeCounter, turnCounter, isRow = 1, 0, True
# placeCounter - How many numbers I can place in a row
# turnCounter - How many numbers I have placed

decX, decY = False, False           # Add or decrease list indices

for num in range(x, y + 1):
    spiralList[i][j] = num
    if isRow and turnCounter < placeCounter:
        if not decX:
            i += 1
        else:
            i -= 1
        turnCounter += 1
        if turnCounter >= placeCounter:
            isRow, turnCounter, decX = False, 0, not decX

    elif not isRow and turnCounter < placeCounter:
        if not decY:
            j += 1
        else:
            j -= 1
        turnCounter += 1
        if turnCounter >= placeCounter:
            isRow, turnCounter, decY = True, 0, not decY
            placeCounter += 1


for k in range(len(spiralList)):
    line = ''
    for l in range(len(spiralList[0])):
        line += str(spiralList[k][l]) + ' '
    print(line)








