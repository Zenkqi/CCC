# Good Samples
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
# N - num of notes,  M - max pitch, K - num of good samples

piece = [1]
samples = [1] + [0] * (N-1)
prev = 0

def calc(p):
    i, backTracked = 0, False
    memo, total, prev, storedIndex = dict(), 0, 0, 0
    while i <= len(p) - 1:
        if backTracked:
            prev = i - 1
            backTracked = not backTracked

        print(i, p[i], memo)
        if not backTracked and [i] in memo:
            n = i - prev
            total += n * (n + 1) // 2
            storedIndex = i
            i = memo[p[i]] + 1
        memo[p[i]] = i
        i += 1
    return total

def sol():
    if N * (N+1) // 2 < K:
        return -1

    prevSamples = 1
    for i in range(1, N-1):
        currSamples = calc(piece[:i-1])
        nextSamples = calc(piece[:i - 1] + [i])
        length = N - (i+1)

        if calc(piece[:i - 1] + [i]) > length: pass

        if currSamples == prev:
            pass
            diff = K - nextSamples
            if diff == 0 or diff >= i:
                piece[i] = i
            if diff == i: pass


        samples.append(calc(piece[:i]))
        prevSamples = nextSamples


print(calc([1, 2, 1]))






