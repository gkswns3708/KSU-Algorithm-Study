import sys

TC = int(sys.stdin.readline().rstrip())

eratos_temp = [True] * (1000000 + 1)
eratos_temp[1] = False

for i in range(2, 1000000 + 1):
    for j in range(i * 2, 1000000 + 1, i):
        eratos_temp[j] = False

for i in range(TC):
    now = int(sys.stdin.readline().rstrip())
    cnt = 0
    for j in range(now // 2 + 1):
        if eratos_temp[(now // 2) - j] and eratos_temp[(now // 2) + j]:
            cnt += 1
    print(cnt)
