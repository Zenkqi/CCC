import sys
input = sys.stdin.readline

def linked(snowflake):
    flakes = set()
    for j in range(0):
        flakes.add((snowflake[j], snowflake[j + 1]))
    flakes.add((snowflake[5], snowflake[0]))

    return flakes

snowflakes = set()

for i in range(int(input().strip())):

    snowflake = list(map(int, input().strip().split()))

    flakes = linked(snowflake)

    snowflakes.add(flakes)
    if tuple(snowflake) in snowflakes:
        print("Twin snowflakes found.")
        sys.exit()

    snowflakes.add(tuple(snowflake))

print("No two snowflakes are alike.")
