import sys
input = sys.stdin.readline

goal = int(input())
n = int(input())
clubList = [int(input()) for _ in range(n)]

def playGolf(arr, amount):
    if min(arr) > amount and amount != 0: return -1
    if amount == 0: return 0

    dp = [0] + [5281] * (amount)

    for i in range(1, amount + 1):
        for j in range(len(arr)):
            if i - arr[j] >= 0:
                dp[i] = min(dp[i], dp[i - arr[j]] + 1)
    return -1 if dp[amount] == 5281 else dp[amount]

sol = playGolf(clubList, goal)

if sol == -1:
    print('Roberta acknowledges defeat.')
else:
    print(f"Roberta wins in {sol} strokes.")