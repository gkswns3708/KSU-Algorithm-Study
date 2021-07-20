import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())

from queue import PriorityQueue
from collections import deque

TC = get_input()
for i in range(TC):
    N, M = get_line()
    pq = PriorityQueue()
    dq = deque()
    arr = list(get_line())
    for idx, j in enumerate(arr):
        pq.put(-j)
        dq.append((idx, j))
    cnt = 1
    while dq:
        if dq[0][1] == -pq.queue[0]:  # 최대 값과 중요도가 같으면 pop함.
            if dq[0][0] == M:  # 이때 우리가 원하는 index의 값과 같으면 출력함.
                print(cnt)
                break
            dq.popleft()
            pq.get()
            cnt += 1
        else:
            dq.append(dq.popleft())
