import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())

N = get_input()
arr = sorted(list(get_line()))
ans = SUM = 0
for i in arr:
    ans += SUM + i
    SUM += i

print(ans)