import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
ans = 0


def reculsive(value):
    if value > N:
        return
    global ans
    ans = max(ans,value)

    for i in arr:
        reculsive(value*10 + i)


reculsive(0)
print(ans)
