# CCC '23 S2 - Symmetric Mountains
import sys
input = sys.stdin.readline

N = int(input())
mou = list(map(int, input().strip().split()))

dp = [float('inf')] * N

for i in range(N):          # Odds
    r, l, curr = i, i, 0
    while l >= 0 and r < N:
        curr += abs(mou[l] - mou[r])
        dp[r-l] = min(curr, dp[r-l])
        r, l = r + 1, l - 1

    r, l, curr = i + 1, i, 0         # Evens
    while l >= 0 and r < N:
        curr += abs(mou[l] - mou[r])
        dp[r-l] = min(curr, dp[r-l])
        r, l = r + 1, l - 1

print(" ".join(map(str, dp)))
