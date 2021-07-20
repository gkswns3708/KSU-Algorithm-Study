import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())

TC = get_input()
for _ in range(TC):
    cnt = 0
    flag = True
    arr = sys.stdin.readline().rstrip()
    for i in arr:
        if i == '(':
            cnt += 1
        else:
            if cnt != 0:
                cnt -= 1
            else:
                flag = False
                break;
    print("YES" if flag and cnt == 0 else "NO")
