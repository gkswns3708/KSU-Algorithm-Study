import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

ans = list(sorted(set(arr)))
ans = {ans[i]:i for i in range(len(ans))}
print(*[ans[i] for i in arr])