import sys

TC = int(sys.stdin.readline().rstrip())

eratos_temp = [True] * (100000 + 1)
eratos_temp[1] = False
eratos = []
for i in range(2, 100000 + 1):
    if eratos_temp[i] == True:
        eratos.append(i)
    for j in range(i * 2, 100000 + 1, i):
        eratos_temp[j] = False

for i in range(TC):
    now = int(sys.stdin.readline().rstrip())
    ans = dict()
    while now > 1:
        for j in eratos:
            if now % j == 0:
                now //= j
                ans.setdefault(j,0)
                ans[j] += 1
    for key, value in ans.items():
        print(key, value)


