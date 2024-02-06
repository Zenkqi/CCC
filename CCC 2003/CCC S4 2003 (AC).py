# CCC '03 S4 - Substrings
import sys
input = sys.stdin.readline
S = int(input())
strings = [str(input().strip()) for i in range(S)]

def substrings(s):
    N = len(s)

    sa = [t[1] for t in sorted((s[i:], i) for i in range(N))]  # Suffix array
    lcp, rank, k = [0] * N, [0] * N, 0 # Array for reverse lookup of the suffix array

    for i in range(N):      # Initialize the lookup array
        rank[sa[i]] = i

    for i in range(N):
        if rank[i] == N - 1:  k = 0; continue
        j = sa[rank[i] + 1]  # Gets the next substring
        while j + k < N and i + k < N and s[i + k] == s[j + k]: k += 1
        lcp[rank[i]] = k
        k = max(0, k - 1)

    # The lcp tells us that there are x similar substrings, we need to subtract those substings
    result = N - sa[0]
    for i in range(1, len(lcp)):
        result += N - sa[i] - lcp[i - 1]
    return result + 1

for i in strings:
    print(substrings(str(i)))





