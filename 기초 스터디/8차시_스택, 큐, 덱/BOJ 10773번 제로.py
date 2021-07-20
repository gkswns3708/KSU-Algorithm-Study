import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())

K = get_input()
arr = []
for _ in range(K):
    now = get_input()
    if now == 0:
        arr.pop()
    else:
        arr.append(now)

print(sum(arr))
