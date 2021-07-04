import sys
import math

M, N = map(int, sys.stdin.readline().rstrip().split())

eratos_sieve = [False] * (N + 1)
eratos_sieve[1] = True

for i in range(2, int(math.sqrt(N) + 1)):
    for j in range(2 * i, N + 1, i):
        eratos_sieve[j] = True

for i in range(M, N + 1):
    if eratos_sieve[i] == False:
        print(i)
