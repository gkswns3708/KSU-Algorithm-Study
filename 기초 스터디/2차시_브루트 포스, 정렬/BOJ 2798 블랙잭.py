import sys

N,M = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

ans = -1

for i in range(len(arr)-2):
    for j in range(i+1,len(arr)-1):
        for k in range(j+1,len(arr)):
            if (arr[i] + arr[j] + arr[k]) > M:
                continue
            # print(arr[i] , arr[j] , arr[k])
            ans = max(ans, arr[i] + arr[j] + arr[k])

print(ans)