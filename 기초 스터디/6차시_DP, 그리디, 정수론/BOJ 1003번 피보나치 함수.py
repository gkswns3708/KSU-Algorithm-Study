import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())

T = get_input()
arr = [[1, 0], [0, 1]] + [[0, 0] for _ in range(39)]


def fibonacci(num):
    if num <= 1:
        return arr[num]
    if arr[num] != [0, 0]:
        return arr[num]
    else:
        now = fibonacci(num - 1)
        now2 = fibonacci(num - 2)
        arr[num] = [now[0] + now2[0], now[1] + now2[1]]
        return arr[num]


for _ in range(T):
    print(*fibonacci(get_input()))
