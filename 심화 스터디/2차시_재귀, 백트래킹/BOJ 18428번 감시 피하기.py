import sys
import copy

get_line: iter = lambda: sys.stdin.readline().rstrip().split()
get_input: int = lambda: int(sys.stdin.readline().strip())

N = get_input()
arr = [list(get_line()) for _ in range(N)]
teacher = []
Scnt = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def possible(temp_arr, y, x):
    if 0 <= y < N and 0 <= x < N and (
            temp_arr[y][x] == ' ' or temp_arr[y][x] == 'X' or temp_arr[y][x] == 'S' or temp_arr[y][x] == 'T'):
        return True
    else:
        return False


def solution(a, b, c):
    y1, x1 = a // N, a % N
    y2, x2 = b // N, b % N
    y3, x3 = c // N, c % N
    if not (arr[y1][x1] == 'X' and arr[y2][x2] == 'X' and arr[y3][x3] == 'X'):
        return False
    temp_arr = copy.deepcopy(arr)
    temp_arr[y1][x1] = 'O'
    temp_arr[y2][x2] = 'O'
    temp_arr[y3][x3] = 'O'
    for now in teacher:
        fty, ftx = now[0], now[1]
        for i in range(4):
            ty, tx = fty, ftx
            print(ty, tx, fty, ftx)
            while possible(temp_arr, ty, tx):
                print(ty, tx, fty, ftx)
                temp_arr[ty][tx] = ' '
                tx += dx[i]
                ty += dy[i]

    cnt = 0
    for i in range(N):
        for j in range(N):
            if temp_arr[i][j] == 'S':
                cnt += 1
    return 1 if cnt == Scnt else 0


# main 문

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'T':
            teacher.append([i, j])
        elif arr[i][j] == 'S':
            Scnt += 1

for pos1 in range(N * N):
    for pos2 in range(pos1 + 1, N * N):
        for pos3 in range(pos2 + 1, N * N):
            answer = solution(pos1, pos2, pos3)
            if answer:
                print("YES")
                exit(0)

print("NO")

a = 1
b = a
b = 2
print (a, b)