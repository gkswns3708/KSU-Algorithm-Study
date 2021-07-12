import sys

N, K = map(int, sys.stdin.readline().strip().split())

A = []
money = K
cnt = 0
for i in range(N):
    A.append(int(sys.stdin.readline()))

for i in range(N - 1, -1, -1):
    cnt += money // A[i]
    money = money % A[i]

print(cnt)