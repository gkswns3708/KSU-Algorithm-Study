import sys
import math

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())

X, Y = get_line()
if X < Y:
    X, Y = Y, X
GCD_XY = math.gcd(X, Y)
x, y = X // GCD_XY, Y // GCD_XY
print((x + y - 1) * GCD_XY)
