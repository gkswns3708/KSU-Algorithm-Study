import sys

N, X = map(int, sys.stdin.readline().rstrip().split())

buger = [0] * (N + 1)
patty = [0] * (N + 1)
buger[0] = 1
patty[0] = 1


def bupa(cnt):
    if cnt == N:
        return
    buger[cnt] = buger[cnt - 1] * 2 + 3
    patty[cnt] = patty[cnt - 1] * 2 + 1
    bupa(cnt + 1)


def cal(n, X):
    if X == 1:
        return 0
    elif buger[n - 1] + 1 > X:  # 빵 + 어느 정도의 N-1번째 버거
        return cal(n - 1, X - 1)
    elif buger[n - 1] + 1 == X:  # 빵 + N-1번째 버거
        return patty[n - 1]
    elif buger[n - 1] + 2 == X:  # 빵 + N-1번째 버거 + 패티
        return patty[n - 1] + 1
    elif buger[n - 1] * 2 + 2 > X > buger[n - 1] + 2:  # 빵 + N-1번째 버거 + 패티 + 어느정도의 N-1번째 버거
        return 1 + patty[n - 1] + cal(n - 1, X - buger[n - 1] - 2)  # n-1번째 버거의 어느 정도와 N-1번째 버거의 패티 전체를 구함.
    elif buger[n - 1] * 2 + 2 == X:  # 빵 + N-1번째 버거 + 패티 + N-1번째 버거
        return 1 + patty[n - 1] * 2
    else: # 그외 (빵 + N-1번째 버거 + 패티 + N-1번째 버거 + (빵)
        return buger[n]


bupa(1)
print(cal(N, X))
