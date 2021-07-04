import math
import sys

# 테스트 케이스 T를 입력받습니다.
T = int(sys.stdin.readline())

# 0~T-1, 즉 T만큼 순회합니다.
for i in range(T):
    # x1, y1, r1, x2, y2, r2 값을 입력받습니다.
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    # math.sqrt()는 제곱근 함수
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # 두 원의 거리 d를 계산합니다.

    # abs는 절댓값 함수
    if d == 0 and r1 == r2:  # 두 원이 동심원이고 반지름이 같을 경우
        print(-1)
    elif abs(r1 - r2) == d or r1 + r2 == d:  # 내접이거나 외접일 경우
        print(1)
    elif abs(r1 - r2) < d < (r1 + r2):  # 두 원이 서로 다른 두 점에서 만날 경우
        print(2)
    else:  # 그 외의 경우
        print(0)
