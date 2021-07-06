import sys

N = int(sys.stdin.readline().rstrip())

arr = [[' '] * 2 ** N for _ in range(2 ** N)]


def reculsive(Y, X, N):
    if N == 0:
        arr[Y][X] = '*'
    else:
        N -= 1
        reculsive(Y + 2 ** N, X, N)
        reculsive(Y, X + 2 ** N, N)
        reculsive(Y, X, N)


reculsive(0, 0, N)
for i in arr:
    print(''.join(i).strip(), sep="")
