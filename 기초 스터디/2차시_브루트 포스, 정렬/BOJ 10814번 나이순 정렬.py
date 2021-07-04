import sys

n = int(sys.stdin.readline())
ans = []
for i in range(n):
    ans.append(list(sys.stdin.readline().split()))
ans.sort(key=lambda x: int(x[0]))
for i in range(n):
    print(ans[i][0], ans[i][1])
