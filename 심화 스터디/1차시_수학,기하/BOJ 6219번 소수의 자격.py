import sys  

A, B, D = map(int, sys.stdin.readline().strip().split())

eratos = [True] * 4000001
eratos[1] = False
cnt = 0

for i in range(2, B + 1):
    for j in range(i * 2, B + 1, i):
        eratos[j] = False

for i in range(A, B + 1):
    if eratos[i] == True:
        if str(D) in str(i):
            cnt += 1

print(cnt)