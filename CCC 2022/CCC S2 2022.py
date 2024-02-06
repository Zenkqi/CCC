violate = 0
studentMapping = {}

X = int(input())
must  = [input().split() for i in range(X)]

Y = int(input())
cant = [input().split() for i in range(Y)]

G = int(input())
group = [input().split() for i in range(G)]

for groups in group:
    for students in groups:
        studentMapping[students] = groups

for studentA, studentB in must:
    if studentMapping[studentA] != studentMapping[studentB]:
            violate += 1

for studentA, studentB in cant:
    if studentMapping[studentA] == studentMapping[studentB]:
            violate += 1

print(violate)