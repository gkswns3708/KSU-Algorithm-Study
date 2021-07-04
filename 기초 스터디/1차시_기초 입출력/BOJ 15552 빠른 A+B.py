import sys

TC = int(input())
for i in range(TC):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)