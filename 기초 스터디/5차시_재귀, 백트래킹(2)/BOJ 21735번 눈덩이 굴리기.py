import sys

N, M = map(int, sys.stdin.readline().strip().split())
arr = [0] + list(map(int, sys.stdin.readline().strip().split()))

dp = [[0] * (N+1) for _ in range(M+1)]
ans = 0


def DP(time, pos, value):
    if time > M :
        return
    global ans
    ans = max(ans, value)
    if pos + 1 <= N:
        DP(time + 1, pos + 1, value + arr[pos + 1])
    if pos + 2 <= N:
        DP(time + 1, pos + 2, value // 2 + arr[pos + 2])

DP(0, 0, 1)
print(ans)
