import sys
import math

T = int(sys.stdin.readline())
arr = []
for i in range(T):
    A, B = map(int, sys.stdin.readline().strip().split())
    print(math.lcm(A, B))
