import sys

X = sys.stdin.readline().strip()
cnt = 0

def sum_function(X):
    result = 0
    for i in X:
        result += int(i)
    return result

def mulofthree_function(X):
    # X가 바로 판별이 되는 경우 -> 1자리인 경우 -> return
    # X가 바로 판별이 안되는 경우 -> 2자리 이상인 경우 -> 변환횟수 += 1
    # mulofthree_function(str(sum_function(X)))를 실행하는 것.
    # sum_function(X)
    # str(sum_function(X))
    # mulofthree_function(str(sum_function(X)))
    if len(X) == 1:
        return "YES" if int(X) % 3 == 0 else "NO"
    else:
        global cnt
        cnt += 1
        Y = sum_function(X)
        return mulofthree_function(str(Y))

ans = mulofthree_function(X)
print(cnt)
print(ans)
# 함수 호출 횟수
# 한 자리 수 확인
# 1234567 -> 28 -> 10 -> 1 (NO)
