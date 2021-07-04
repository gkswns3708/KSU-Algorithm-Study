import sys
import math

eratos_sieve = [False] * (123456 * 2 + 1)
eratos_sieve[1] = True

for i in range(2, 123456 + 1):
    for j in range(i * 2, 123456 * 2 + 1, i):
        eratos_sieve[j] = True

while 1:
    now_input = y = int(sys.stdin.readline())
    if now_input == 0:
        break
    else:
        cnt = 0
        for i in range(now_input + 1, now_input * 2 + 1):
            if not eratos_sieve[i]:
                cnt += 1
        print(cnt)
