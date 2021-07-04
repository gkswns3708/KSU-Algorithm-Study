import sys
import math

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
fprime = 0
primesum = 0

eratosthenes_sieve = [False] * (N+1)
eratosthenes_sieve[1] = True

for i in range(2, N + 1):
    for j in range(i * 2, N + 1, i):
        eratosthenes_sieve[j] = True
        # print(f"{j}번째 숫자는 소수가 아닙니다.")


for i in range(M, N+1):
    if eratosthenes_sieve[i] == False:
        # print(f"{i}번째 수는 소수입니다.")
        if fprime == 0:
            fprime = i
        primesum += i

if fprime != 0:
    print(primesum)
    print(fprime, end="")
else:
    print(-1, end="")

