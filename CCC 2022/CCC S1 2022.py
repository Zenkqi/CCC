# CCC '22 S1 - Good Fours and Good Fives
num = int(input())
total = 0

if num % 4 == 0:
    total += 1

while num > 0:
    if num % 5 == 0:
        total += 1
    num -= 4

print(total)
