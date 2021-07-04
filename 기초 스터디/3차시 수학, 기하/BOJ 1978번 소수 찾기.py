import sys
import math

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))
ans = 0
for i in arr:
    flag = True if i != 1 else False
    for j in range(2, int(math.sqrt(i) + 1)):
        if (i % j) == 0:
            # print(f"{i}는 소수가 아닙니다.")
            flag = False
            break
    if flag:
        ans += 1

print(ans)
