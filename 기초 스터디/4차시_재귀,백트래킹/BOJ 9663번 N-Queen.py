def check(n):
    for i in range(n):
        if arr[n] == arr[i] or abs(arr[n] - arr[i]) == n - i:
            return 0
    return 1


def a(n):
    global cnt
    if n == N:
        cnt += 1
    else:
        for i in range(N):
            arr[n] = i
            if check(n):
                a(n + 1)


N = int(input())
arr = [0] * N
cnt = 0
a(0)
print(cnt)
