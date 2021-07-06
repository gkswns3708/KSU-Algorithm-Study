import sys

N = int(sys.stdin.readline().rstrip())
arr = [[' '] * (N * 4 + -3) for _ in range(N * 4 + -3)]


def drawLR(idx):
    if idx == N:
        return
    for i in range(idx * 2, N * 4 + - 3 - idx * 2):
        arr[i][idx * 2] = '*'
        arr[i][N * 4 - 4 - idx * 2] = "*"
    drawLR(idx + 1)


def drawUD(idx):
    if idx == N:
        return
    for i in range(idx * 2, N * 4 + - 3 - (idx * 2)):
        arr[idx * 2][i] = "*"
        arr[N * 4 - 4 - idx * 2][i] = "*"
    drawUD(idx + 1)


drawLR(0)
drawUD(0)
for i in arr:
    print(*i, sep="")
