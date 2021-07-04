## 재귀

재귀 함수란 호출한 함수에서 다시 그 함수를 호출(recursive call)함으로 반복하는 것을 의미한다.

쉽게 말하자면 `**만든 함수 안에서 다시 그 함수를 호출 하는 것**`을 의미한다. 자칫하면 무한히 자기 자신을 호출하게 되므로 `무한 루프` 에 빠지기 쉬우므로 저는 재귀함수를 아래와 같은 구조를 가진다고 생각합니다.

```python
def 함수 (매개변수) # 함수 선언부
	if (매개변수의 상태에 따른 종결 조건) : # (기저 사례)
		...
		return ???
	else :
		...
		return 함수(현재의 함수가 진행하면서 변한 매개변수) # recursive call
```

- [BOJ 10872번 팩토리얼](https://www.acmicpc.net/problem/10872)
    - source code - 한준

        ```python
        import sys

        N = int(sys.stdin.readline())
        ans = 1

        def recursive_function(i):
            if i == 1 or i == 0: # 매개변수 상태에 따른 종결 조건
                return 1
            else:
                return i * recursive_function(i - 1); # 함수가 진행하면서 변한 매개변수 (i-1)

        print(recursive_function(N))
        ```

- [BOJ 2447번 별 찍기 - 10](http://boj.kr/2447)
    - source code - 한준

        ```python
        import sys

        N = int(sys.stdin.readline())

        def recursive_mapping(n, y, x):
            global b
            if n == 1: # 기저 사례
                arr[y][x] = '*'
            else:
                for i in range(3):
                    for j in range(3):
                        if i != 1 or j != 1:
                            recursive_mapping(n // 3, y + (n // 3) * i, x + (n // 3) * j)
        										# 재귀 호출 부분

        arr = [([' '] * N) for _ in range(N)]
        recursive_mapping(N, 0, 0)
        for i in arr:
            print(*i, sep='') # 출력시에 list간 공백없이 출력하는 방법
        ```

- [BOJ 11729번 하노이 탑 이동 순서](https://www.acmicpc.net/problem/11729)
    - 참고 과정...?

        N번째를 시작 지점에서 목표 지점으로 옮긴다  
        N-1 개를 시작 지점에서 거쳐가는 지점으로 옮기고
        -> N-2 개를 시작 지점에서 거쳐가는 지점으로 옮기고
        ->-> N-3 개를 시작 지점에서 거쳐가는 지점으로 옮기고
        ->->-> N-4 개를 시작 지점에서 거쳐가는 지점으로 옮기고
        ->->-> 1개를 목표지점으로 옮긴 뒤
        ->->-> 거쳐가는 지점에 있는 N-4개를 목표지점으로 옮긴다
        ->-> 1개를 목표지점으로 옮긴 뒤
        ->-> 거쳐가는 지점에 있는 N-3개를 목표지점으로 옮긴다
        -> 1개를 목표지점으로 옮긴 뒤
        -> 거쳐가는 지점에 있는 N-2개를 목표지점으로 옮긴다.
        1개를 목표지점으로 옮긴뒤
        거쳐가는 지점에 있는 N-1개를 목표지점으로 옮긴다.

        옮긴다 ⇒ 호출한다 이런 느낌으로 받아들이면 될 듯...?

    - source code - 최한준

        ```python
        import sys

        N = int(sys.stdin.readline())

        def hanoi(n, st, mid, ed):
            if n == 1:
                print(f"{st} {ed}")
            else:
                hanoi(n - 1, st, ed, mid)
                print(f"{st} {ed}")
                hanoi(n - 1, mid, st, ed)

        print((1 << N) - 1) 
        # 쉬프트 연산은 단순히 생각하면 빠르게 2 ** N한다고 생각하면 편할 듯 합니다.
        # 자세한 내용은 쉬프트 연산자를 구글신에게 검색 해보세요.
        hanoi(N, 1, 2, 3)
        ```

    - source code - 박은지

        ```python
        import sys

        def move_disk(disk_num, start_peg, end_peg):
            print(f'{start_peg} {end_peg}')

        def hanoi(num_disks, start_peg, end_peg):
            # base case: 옮길 원판이 없으면 부분 문제를 나누지 않고 함수 종료
            if num_disks == 0:
                return
            else:
                mid_peg = 6 - start_peg - end_peg

                # 1. 가장 큰 원판을 제외하고 나머지 원판들을 start_peg에서 mid_peg로 이동
                hanoi(num_disks - 1, start_peg, mid_peg)

                # 2. 가장 큰 원판을 start_peg에서 end_peg로 이동
                move_disk(num_disks, start_peg, end_peg)

                # 3. 나머지 원판들을 mid_peg에서 end_peg로 이동
                hanoi(num_disks - 1, mid_peg, end_peg)

        # 테스트
        N = int(sys.stdin.readline())
        print(f'{2 ** N - 1}')
        hanoi(N, 1, 3)

        # 실행 결과
        # 3 -> 입력 값
        # 7
        # 1 3
        # 1 2
        # 3 2
        # 1 3
        # 2 1
        # 2 3
        # 1 3
        ```

- BOJ 9663번 N-Queen
    - 주의사항
        - 무조건 PyPy3로 제출할 것. Python3은 Naive하게 짰을 경우 시간초과가 난다.
    - source code - 한준

        ```python
        def check(n):
            for i in range(n):
                if arr[n] == arr[i] or abs(arr[n] - arr[i]) == n - i:
                    return 0
            return 1

        def N_Queen(n):
            global cnt
            if n == N:
                cnt += 1
            else:
                for i in range(N):
                    arr[n] = i
                    if check(n):
                        N_Queen(n + 1)

        N = int(input())
        arr = [0] * N
        cnt = 0
        N_Queen(0)
        print(cnt)
        ```

---

## 백트래킹

---

## @

- 리스트 출력 형식

    ```python
    print(*lis, sep='') # 출력시에 list 원소간 공백없이 출력하는 방법
    # 원리는 원소간 구분자를 default가 공백이던 것을 아무것도 없게 해 원소간 간격을 없앰.
    print(lis, end='') # 원래 print는 내용을 출력하고 \n이 기본
    # 그러나 end를 이용해 마지막 출력을 \n에서 ''으로 바꿔 같은 줄에 다음 print가 입력됨
    print("~~~~ {0} ~~{1}~".format(연산 내용, 연산 내용)) # 연산된 결과과 순서대로 들어감.
    print(f"~~~~{연산내용} ~~~{연산내용}") # 이렇게 작성 해도 됨.
    ```

    출처 : [https://infinitt.tistory.com/11](https://infinitt.tistory.com/11)

- python 시간 제한에 대한 내용

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e46a5285-a862-4a14-a953-84db1ced2967/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e46a5285-a862-4a14-a953-84db1ced2967/Untitled.png)

    출처 : [https://www.acmicpc.net/help/language](https://www.acmicpc.net/help/language)