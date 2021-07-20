import sys

N = int(sys.stdin.readline())
queue = [0]
st, ed = 0, 0
for i in range(N):
    command = sys.stdin.readline().strip().split()
    if command[0] == 'push':
        queue.append(command[1])
        ed += 1
    elif command[0] == 'pop':
        if st == ed:
            print(-1)
        else:
            st += 1
            print(queue[st])
    elif command[0] == 'size':
        print(ed - st)
    elif command[0] == 'empty':
        if st == ed:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if st == ed:
            print(-1)
        else:
            print(queue[st + 1])
    elif command[0] == 'back':
        if st == ed:
            print(-1)
        else:
            print(queue[-1])
