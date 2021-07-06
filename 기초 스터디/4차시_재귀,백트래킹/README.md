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

함수 호출시 stack에 데이터가 쌓입니다. stack이 꽉차게 되면 더이상 함수호출을 하지 못하게 되고 프로그램이 강제 종료됩니다. 잘은 없겠지만 함수를 매우 깊게 호출하는건 프로그램을 뻗게 만들수도 있으니 설계를 잘 하는게 중요합니다.
 - 함수 호출에 의해 쌓여있는 스택을 보고 call stack 이라고 부릅니다.
 - OS에서 따로 "최대 call stack depth"를 정하고 있진 않습니다. OS는 "stack의 최대 사이즈는 ~~MB이다" 라고 제한만 합니다. call stack depth는 여러분이 작성하는 코드에 달려 있습니다. 여러분이 `int main() { ~~~ }` 으로 작성할 때 무심코 선언했던 변수들은 모두 stack에 들어가 저장됩니다. `int a = ~~`를 선언한 경우 `int`형 바이트 크기만큼 stack 공간을 소모합니다. 윈도우의 경우, 기본적으로 스택을 1MB로 제한하고 있습니다. 
- stack은 쓰래드당 공간이 부여되며 함수 호출에 따라 계속 쌓이는 구조입니다. 프로그램의 실행 구조가: `main()` → `run()` → `create_table()` → `verification()` 식으로 nested 되어있으면 각각의 함수 정보(스택)가 쓰래드의 스택에 쌓입니다. 각각의 함수에서 `main`: 128K, `run`: 256K, `create_table`: 512K, `verification`: 12K 씩 로컬 스택을 쓴다면 전체에서는 908KB를 사용하겠네요. 이 쓰레드에서 116KB의 스택을 더 쓰면 stack overflow로 터질겁니다.
- `main` 함수에서 크기가 매우 큰 변수를 선언하면 `main`함수에서 다른 함수를 호출하는것 조차 안될 수 있습니다. 
   → C등에서 recursive한 함수를 만들 때 stack의 사이즈를 전혀 고려하지 않고, 각 함수에서 256KB짜리 배열을 만들었다 하면 5번째 깊이에서 프로그램은 터질겁니다.
- 1학년때 프로그래밍 강의 때 “*크기가 매우큰 배열을 만들때는 `malloc`을 써야한다.”* 라고 하는 이유가 여기에 있습니다. 배열의 크기든 뭐든 총 합이 stack의 크기보다 커지면 프로그램이 죽거든요. 다르게 보면... stack의 크기보다 커지지만 않게 한다면 어느 크기든 상관없이 배열을 만들어도 됩니다.
- Python은 인터프리터 언어입니다. 그렇기에 유저들이 호출한 함수들이 직접적으로 스택에 쓰이지는 않습니다. 유저들이 호출한 함수들은 인터프리터 내부상에 `frame`으로 표현됩니다. ( [https://towardsdatascience.com/python-stack-frames-and-tail-call-optimization-4d0ea55b0542](https://towardsdatascience.com/python-stack-frames-and-tail-call-optimization-4d0ea55b0542) )
  → 실제로는 CPython내에 스택이 있습니다. 그러나 사용자 눈에서는 (`traceback`을 찍을때는) 해당 스택이 직접적으로 보이진 않습니다. 실제 스택을 찍어보고 싶으시면 `gdb`를 붙이시면 잘 보일겁니다. (예전엔 잘 보였습니다)
      ⇒ CPython은 C++언어로 Python 구현체를 만든것입니다. 그렇기에 내부 구현은 C의 함수 호출을 사용합니다. ( [https://nikhilism.com/post/2018/python-call-stack](https://nikhilism.com/post/2018/python-call-stack) ) 그 점 때문에 Python 코드상에선 함수를 몇개 호출을 하지도 않았는데 stack이 꽉차서(CPython의 내부 구현때문에) 프로그램이 터지기도 했습니다
      → 한때 이 문제로 stackless python이 흥행했습니다. pypy가 stackless를 계승하여 들고왔으며, 현재는 pypy가 주로 쓰입니다.
- Python은 안전을 위해(?) 기본적으로 1000회 이상의 recursive 호출을 막고 있습니다. 만약 1000개 이상의 recursive 함수 호출을 해야한다면 별도의 설정이 필요합니다. ( [https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=luiz4our&logNo=220642911892](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=luiz4our&logNo=220642911892) )
- recursive한 호출은 일반 loop 작업에 비해 cost가 더 먹는것은 사실입니다. 혹시나 미래에 극한의 최적화를 해야할 경우가 온다면 recursive 함수를 loop 구조로 바꾸셔야 할 수도 있습니다
  ⇒ 2학년 "계산이론" 과목에서 `tail recursion`에 대해 들어봤을 겁니다. 재귀형 함수더라도 tail recursion 형태로 코드를 작성하시면 똑똑한 컴파일러들이 알아서 최적화를 해 줄것입니다 (Tail call optimization - [https://medium.com/pocs/tail-call-recursion-79176631fc1](https://medium.com/pocs/tail-call-recursion-79176631fc1) , [https://eklitzke.org/how-tail-call-optimization-works](https://eklitzke.org/how-tail-call-optimization-works) )
 - 한편 Haskell 언어의 경우 함수 호출이 thunk 형태로 heap에 저장됩니다. 그렇기에 recursion에 의한 stack 문제뿐 아니라, function call recursion 구조에 의한 성능저하에서 거의 자유롭습니다. (아예 스택이 없는것은 아닙니다)
- 여기 적힌 내용이 [https://homoefficio.github.io/2015/07/27/%EC%9E%AC%EA%B7%80-%EB%B0%98%EB%B3%B5-Tail-Recursion](https://homoefficio.github.io/2015/07/27/%EC%9E%AC%EA%B7%80-%EB%B0%98%EB%B3%B5-Tail-Recursion) 에 잘 설명되어 있는것 같습니다.

- 세줄요약:
    - 재귀적 구조는 이해하기 쉽고 간결한 구조를 만들지만, 고려없이 너무 깊은 재귀구조를 만들면 스택공간 때문에 프로그램이 터진다
    - 재귀구조는 어쨋든 loop 문에 비해 cost가 더 발생하는것이 사실이다. 그러나 코드를 깨끗하게 (컴파일러가 알아먹을 수준으로 - tail recursion 형식으로) 만들면 어느정도 최적화를 해 준다
    - python은 기본적으로 함수 call을 1000회로 제한한다. recursion 하다가 프로그램이 터질수도 있으니 유의해서 설계 해야한다. 
- 이석민 좋은 글 (감사합니다)

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

    - source code - 한준

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

    - source code - 은지

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

---

## 백트래킹

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

- BOJ 2580번 스도쿠
    - 주의사항
        - 무조건 PyPy3로 제출할 것. Python3은 Naive하게 짰을 경우 시간초과가 날 거 같다.
    - source code - 한준

        ```python
        arr = [list(map(int, input().split())) for _ in range(9)]
        empty_pos, N = [0] * 81, 0
        row = [[False] * 10 for _ in range(9)]
        col = [[False] * 10 for _ in range(9)]
        squ = [[False] * 10 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if arr[i][j] != 0:
                    row[i][arr[i][j]] = True
                    col[j][arr[i][j]] = True
                    squ[(i // 3) * 3 + j // 3][arr[i][j]] = True
                else:
                    empty_pos[N] = i * 9 + j
                    N += 1  # len 함수의 시간 복잡도가 O(N)이기 때문에 상수로 이렇게 구현해놓는게 편할 듯 하다.

        def solve(idx):
            if idx == N:
                for i in range(9):
                    print(' '.join(map(str, arr[i])))
                exit(0)

            x, y = empty_pos[idx] // 9, empty_pos[idx] % 9
            for i in range(1, 10):
                if not (row[x][i] or col[y][i] or squ[(x // 3) * 3 + y // 3][i]):
                    row[x][i] = col[y][i] = squ[(x // 3) * 3 + y // 3][i] = True
                    arr[x][y] = i
                    solve(idx + 1)
                    arr[x][y] = 0
                    row[x][i] = col[y][i] = squ[(x // 3) * 3 + y // 3][i] = False

        solve(0)
        ```

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

    [Python 시간 제한에 대한 내용](https://user-images.githubusercontent.com/62585503/124578102-decfa200-de88-11eb-9a6a-a2fae83c238d.png)


    출처 : [https://www.acmicpc.net/help/language](https://www.acmicpc.net/help/language)
