import sys

N, K = map(int, sys.stdin.readline().strip().split())

eratos = [True] * (N + 1)
cnt = 0
for i in range(2, N + 1):
    if eratos[i] == True:
        for j in range(i, N + 1, i):
            if eratos[j] == False:
                continue
            eratos[j] = False;
            cnt += 1
            if cnt == K:
                print(j)
                sys.exit(0)
