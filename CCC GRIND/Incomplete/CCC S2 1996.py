import sys
input = sys.stdin.readline
n = int(input())

numbers = [int(input()) for _ in range(n)]

for i in numbers:
    num = i
    print(num)
    while num >= 11:
        if num == 11:
            print(f"The number {i} is divisible by 11.")
            break
        temp = num // 10
        onesDigit = num - (10 * temp)

        num = temp - onesDigit
        print(num)

    else: print(f"The number {i} is not divisible by 11.")

