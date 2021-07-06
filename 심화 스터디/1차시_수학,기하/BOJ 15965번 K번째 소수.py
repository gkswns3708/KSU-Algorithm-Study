import sys

check = [True] * (7500000 + 1)
for i in range(2, int(7500000 ** 0.5) + 1):
    if check[i]:
        for j in range(i * 2, 7500000 + 1, i):
            check[j] = False

prime = [i for i in range(2, 7500000 + 1) if check[i]]
K = int(sys.stdin.readline().rstrip())
print(prime[K - 1])
