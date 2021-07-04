import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = []
for i in range(N):
    arr.append(sys.stdin.readline().rstrip())

ans = 64

for y in range(N-8 + 1):
    for x in range(M-8+1):
        cnt1 = 0
        cnt2 = 0
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 1:
                    if arr[y+i][x+j] == 'W':
                        cnt1 +=1
                    else :
                        cnt2+=1
                else :
                    if arr[y+i][x+j] == 'B':
                        cnt1 +=1
                    else :
                        cnt2+=1
        ans = min(cnt1,cnt2,ans)
print(ans)