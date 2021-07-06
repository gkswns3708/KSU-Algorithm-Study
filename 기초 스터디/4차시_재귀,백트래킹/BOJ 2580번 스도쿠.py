arr = [list(map(int, input().split())) for _ in range(9)]
empty_pos, N = [0] * 81, 0
row = [[False] * 10 for _ in range(9)]
col = [[False] * 10 for _ in range(9)]
squ = [[False] * 10 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if arr[i][j] != 0:
            row[i][arr[i][j]] = True
            col[j][arr[i][j]] = True
            squ[(i // 3) * 3 + j // 3][arr[i][j]] = True
        else:
            empty_pos[N] = i * 9 + j
            N += 1  # len 함수의 시간 복잡도가 O(N)이기 때문에 상수로 이렇게 구현해놓는게 편할 듯 하다.


def solve(idx):
    if idx == N:
        for i in range(9):
            print(' '.join(map(str, arr[i])))
        exit(0)

    x, y = empty_pos[idx] // 9, empty_pos[idx] % 9
    for i in range(1, 10):
        if not (row[x][i] or col[y][i] or squ[(x // 3) * 3 + y // 3][i]):
            row[x][i] = col[y][i] = squ[(x // 3) * 3 + y // 3][i] = True
            arr[x][y] = i
            solve(idx + 1)
            arr[x][y] = 0
            row[x][i] = col[y][i] = squ[(x // 3) * 3 + y // 3][i] = False


solve(0)
