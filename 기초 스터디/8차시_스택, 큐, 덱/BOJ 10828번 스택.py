import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())

N = get_input()
arr = []
length = 0
for _ in range(N):
    command = list(sys.stdin.readline().rstrip().split())
    if command[0] == 'push':
        arr.append(command[1])
        length += 1
    elif command[0] == 'pop':
        if length == 0:
            print(-1)
        else:
            print(arr.pop())
            length -= 1
    elif command[0] == 'size':
        print(length)
    elif command[0] == 'empty':
        print(1 if length == 0 else 0)
    elif command[0] == 'top':
        if length == 0:
            print(-1)
        else:
            print(arr[-1])
