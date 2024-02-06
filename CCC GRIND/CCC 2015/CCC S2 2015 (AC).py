J = int(input())
A = int(input())

mappings = {
    'S' : 1,
    'M' : 2,
    'L' : 3
}

jerseys = [mappings[str(input())] for _ in range(J)]
prefer = [tuple(map(str, input().split())) for _ in range(A)]
marked = [0 for i in range(1000005)]
total = 0
for size, number in prefer:
    if mappings[size] <= jerseys[int(number) - 1] and marked[int(number)] == 0:
        marked[int(number)] = int(number)
        total += 1

print(total)