import sys

N = int(sys.stdin.readline())

cnt = 0
now = 666
while 1:
    if '666' in str(now):
        cnt += 1
    if cnt == N:
        print(now)
        break
    now += 1
