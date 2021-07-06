import sys

T = int(sys.stdin.readline().strip())

eratos_temp = [True] * (1000 + 1)
eratos_temp[1] = False
eratos = []
for i in range(2, 1000 + 1):
    if eratos_temp[i] == True:
        eratos.append(i)
    for j in range(i * 2, 1000 + 1, i):
        eratos_temp[j] = False

for TC in range(T):
    K = int(sys.stdin.readline().strip())
    flag = False
    for i in eratos:
        if flag: 
            break
        for j in eratos:
            if flag:
                break
            for k in eratos:
                if i + j + k == K:
                    print(i, j, k)
                    flag = True
                    break
