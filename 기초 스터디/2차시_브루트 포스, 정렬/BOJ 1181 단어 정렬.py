import sys
from functools import cmp_to_key

N = int(sys.stdin.readline().rstrip())
words = sys.stdin.read().splitlines()

arr = [str(i) for i in set(words)]

def compare(x ,y):
    if(len(x) > len(y)):
        return 1
    elif (len(x) == len(y)):
        if x > y :
            return 1
        elif x == y:
            return 0
        else:
            return -1
    else:
        return -1


for i in sorted(arr, key=cmp_to_key(compare)):
    print(i)
