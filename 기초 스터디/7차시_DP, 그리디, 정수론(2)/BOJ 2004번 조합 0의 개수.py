import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())

N, M = get_line()
K = N - M


def div5(num):
    cnt = 0
    now = 5
    while now <= num:
        cnt += num // now
        now *= 5
    return cnt


def div2(num):
    cnt = 0
    now = 2
    while now <= num:
        cnt += num // now
        now *= 2
    return cnt


print(max(0, min(div5(N) - div5(K) - div5(M), div2(N) - div2(M) - div2(K))))
