import sys

N = int(sys.stdin.readline())

arr = [0] * (N+1)

def fibonacci(i):
    if arr[i] != 0:
        return arr[i]
    else:
        if i == 0 or i == 1:
            arr[i] = i
            return arr[i]
        else:
            arr[i] = fibonacci(i-2) + fibonacci(i-1)
            return arr[i]

print(fibonacci(N))