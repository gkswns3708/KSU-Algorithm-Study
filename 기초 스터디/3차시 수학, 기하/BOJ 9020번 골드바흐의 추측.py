import sys

N = int(sys.stdin.readline())

eratos_sieve = [False] * (10000 + 1)
eratos_sieve[1] = True

for i in range(2, 10000 + 1):
    for j in range(i * 2, 10000 + 1, i):
        eratos_sieve[j] = True


for i in range(N):
    now_input = int(sys.stdin.readline())
    for j in range(now_input//2):
        if (not eratos_sieve[(now_input//2)-j]) and (not eratos_sieve[(now_input//2)+j]):
            print(now_input//2-j,now_input//2+j)
            break

