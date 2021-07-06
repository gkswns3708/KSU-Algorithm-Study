import sys

N = int(sys.stdin.readline().rstrip())

eratos_temp = [True] * (1000000 + 1)
eratos_temp[1] = False
eratos = []
for i in range(2, 1000000 + 1):
    if eratos_temp[i] == True:
        eratos.append(i)
    for j in range(i * 2, 1000000 + 1, i):
        eratos_temp[j] = False

eratos.sort()
arr = list(map(int, sys.stdin.readline().strip().split()))
ans = set()

for i in arr:
    for j in eratos:
        if i == j and j <= i:
            ans.add(i)
            break

if len(ans) == 0:
    print(-1)
else:
    answer = 1
    for i in ans:
        answer*=i
    print(answer)


