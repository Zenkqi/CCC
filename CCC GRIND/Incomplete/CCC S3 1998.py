import sys
imput = sys.stdin.readline

facingDir = 0
# 'north': 0, 'east': 1, 'south': 2,'west': 3

coord = [0, 0]

def inDir(step, direction):
    x, y = coord[0], coord[1]

    if direction == 0:
        x += step

    elif direction == 1:
        y += step

    elif direction == 2:
        x -= step

    elif direction == 3:
        y -= step

    return [x, y]


while True:
    command = int(input())
    print('--------------------------------------------')
    print(coord)
    print('------------ttttttttttttttttt---------------')
    print(facingDir)
    print('--------------------------------------------')

    if command == 0:
        print(abs(coord[0]) + abs(coord[1]))

    if command == 1:        # Forward
        dx = int(input())
        coord = inDir(dx, facingDir)

    if command == 2:        # Right
        facingDir = (facingDir + 1) % 4

    if command == 3:        # Left
        facingDir = (facingDir - 1) % 4

print(coord)