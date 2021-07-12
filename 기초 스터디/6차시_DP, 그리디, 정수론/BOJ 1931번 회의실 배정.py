import sys
from functools import cmp_to_key

INF = 987654321

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())

time = -1
ans = 0


def compare(X, Y):
    if X[1] == Y[1]:
        return X[0] - Y[0]
    else:
        return X[1] - Y[1]


N = get_input()

arr = [list(get_line()) for _ in range(N)]

arr = sorted(arr,key=cmp_to_key(compare))
for i in arr:
    # print(*i)
    if time <= i[0]:
        time = i[1]
        ans += 1
    else:
        continue

print(ans)