import sys
import re

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())

input = sys.stdin.readline().rstrip()
arr = list(map(int, re.split('[+-]', input)))
pos = -1
cnt = 0
flag = True
for i in input:
    if i == '-' or i == '+':
        cnt += 1
        if i == '-':
            flag = False
            break

if cnt == 0:
    ans = arr[0]
elif flag:
    ans = sum(arr[:cnt + 1])
else:
    ans = sum(arr[:cnt]) - sum(arr[cnt:])

print(ans)
