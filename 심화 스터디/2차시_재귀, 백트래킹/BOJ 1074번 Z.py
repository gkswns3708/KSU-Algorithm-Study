import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())

N, R, C = get_line()

cnt = 0


def recursive(n, r, c):
    global cnt
    if n == 1:
        return 1
    else:
        n //= 2
        if R < n + r and C < n + c:
            return recursive(n, r, c)
        elif R < n + r and C >= n + c:
            return n * n + recursive(n, r, c + n)
        elif R >= n + r and C < n + c:
            return n * n * 2 + recursive(n, r + n, c)
        else:
            return n * n * 3 + recursive(n, r + n, c + n)


print(recursive(2 ** N, 0, 0) - 1)
