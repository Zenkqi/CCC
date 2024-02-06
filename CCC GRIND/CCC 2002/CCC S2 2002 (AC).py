import sys
input = sys.stdin.readline

num = int(input())
denom = int(input())

def euclidAlgo(a, b):
    while b:
        a, b = b, a % b
    return a

if num == 0:
    print('0')

else:
    whole = 0
    fraction = str(num) + '/' + str(denom)
    if num > denom:
        remainder = num % denom
        whole = (num - remainder) // denom
        num = remainder

    gcd = euclidAlgo(num, denom)
    fraction = str(num // gcd) + '/' + str(denom // gcd)

    if whole == 0:
        print(fraction)
    elif num == 0:
        print(whole)
    else:
        print(whole, fraction)