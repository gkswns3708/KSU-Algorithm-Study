import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())
deq = deque()

for i in range(1, N+1):
    deq.append(i)

print('<', end="")

while deq: # 큐가 비어있지 않다면 반복 실행
    for i in range(K-1):
        deq.append(deq.popleft())
    print(deq.popleft(), end="")
    if deq:
        print(", ", end="")

print('>')