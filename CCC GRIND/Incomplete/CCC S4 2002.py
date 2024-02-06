# M - max people, Slowest person is the time it takes to cross
import sys
input = sys.stdin.readline
M = int(input())        # Limit
Q = int(input())        # Length of the queue

q = []
time = []
for i in range(Q):
    q.append(str(input()))
    time.append(int(input()))

dp = [[0] * Q for _ in range(Q)]

for i in range(Q, -1, -1):
    for j in range(i, Q):
        if i - j + 1 < M: dp[i][j] = max(q[i:j]); continue

        dp[i][j] = min([dp[i][k] + dp[k+1][j] for k in range(i+1, j-1, M)])




"""for l in range(1, M+1):
    for i in range(Q-l+1):
        j = i+l-1
        print(l, i, j)
        for k in range(i, j):
            if l < M:
                print('hey')
                dp[i][j] = max(time[i:j+1])
            else:
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])"""

print(dp)
print(dp[0][-1])