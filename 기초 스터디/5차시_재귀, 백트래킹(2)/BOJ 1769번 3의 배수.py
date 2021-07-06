import sys

cnt = 0

def func1(s):
    global cnt
    if len(s) == 1:
        return 1 if int(s) % 3 == 0 else 0
    cnt += 1
    ret = 0
    for i in s:
        ret += int(i)
    return func1(str(ret))


N = (sys.stdin.readline().rstrip())


ans = "YES" if func1(N) == 1 else "NO"
print(cnt)
print(ans)
