import sys

N = int(sys.stdin.readline())
ans = 1


def recursive_function(i):
    if i == 1 or i == 0:
        return 1
    else:
        return i * recursive_function(i - 1);


print(recursive_function(N))
