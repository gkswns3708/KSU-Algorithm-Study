## DP

- DP 알고리즘 관련 블로그
    - [https://blog.naver.com/ndb796/221233570962](https://blog.naver.com/ndb796/221233570962)
- DP에 관한 짧은 설명
    - 큰 문제를 해결할 때 작은 문제로 쪼갠뒤에 풀어야 하며, 이때 이 작은 문제들의 답은 정해져 (고정, "불변" 과는 좀 멀다) 있습니다.이때 작은 문제들을 푸는 방식과 큰 문제들을 푸는 방식이 동일해야합니다. 즉 작은 문제들을 잘 해결한뒤 동일한 방법으로 큰 문제를 해결할 수 있을 때 사용하는 알고리즘입니다. 이 과정에서 메모이제이션([memoization](https://ko.wikipedia.org/wiki/%EB%A9%94%EB%AA%A8%EC%9D%B4%EC%A0%9C%EC%9D%B4%EC%85%98)) 기법이 활용됩니다.
- BOJ 1003번 피보나치 함수
    - source Code

        ```python
        import sys

        get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
        get_input: int = lambda: int(sys.stdin.readline())

        T = get_input()
        arr = [[0, 0] for _ in range(50)]

        arr[0] = [1, 0]
        arr[1] = [0, 1]

        def fibonacci(num):
            if num <= 1:
                return arr[num]
            if arr[num] != [0, 0]:
                return arr[num]
            else:
                now = fibonacci(num - 1)
                now2 = fibonacci(num - 2)
                arr[num] = [now[0] + now2[0], now[1] + now2[1]]
                return arr[num]

        for _ in range(T):
            print(*fibonacci(get_input()))
        ```

- BOJ 1904번 01 타일
    - source Code

        ```python
        import sys

        MOD = 15746
        get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
        get_input: int = lambda: int(sys.stdin.readline())

        N = get_input()

        arr = [0, 1, 2] + [0] * (N + 1)

        for i in range(3, N + 1):
            arr[i] = (arr[i - 1] + arr[i - 2]) % MOD
        print(arr[N])
        ```

---

## Greedy

- 그리디 알고리즘에 대한 짧은 설명
    - 그리디 알고리즘이란 말 그대로 탐욕적으로 문제를 해결한다는 뜻입니다. 이때 탐욕적이라는 말은 미래를 생각하지 않고 오직 "현재 상태"에서 가장 최선의 선택을 한다는 뜻입니다. 어떻게 보면 문제를 해결할 때 가장 먼저 떠오르는 기본적인 알고리즘일 수도 있습니다.
    - 그리디 알고리즘은 그리디 알고리즘이라고 판별하는 것이 어렵습니다. 왜냐하면 "현재 상태"에서 가장 최선의 선택을 한 것이 모든 경우의 수에 대해서 가장 최선의 선택인지 아닌지를 판별을 해야하기 때문입니다.
- BOJ 11047번 동전 0
    - source Code

        ```python
        import sys

        N, K = map(int, sys.stdin.readline().strip().split())

        A = []
        money = K
        cnt = 0
        for i in range(N):
            A.append(int(sys.stdin.readline()))

        for i in range(N - 1, -1, -1):
            cnt += money // A[i]
            money = money % A[i]

        print(cnt)
        ```

- BOJ 1931번 회의실 배정
    - source Code

        ```python
        import sys
        from functools import cmp_to_key

        INF = 987654321

        get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
        get_input: int = lambda: int(sys.stdin.readline())

        time = -1
        ans = 0

        def compare(X, Y):
            if X[1] == Y[1]:
                return X[0] - Y[0]
            else:
                return X[1] - Y[1]

        N = get_input()

        arr = [list(get_line()) for _ in range(N)]

        arr = sorted(arr,key=cmp_to_key(compare))
        for i in arr:
            # print(*i)
            if time <= i[0]:
                time = i[1]
                ans += 1
            else:
                continue

        print(ans)
        ```

        - c++언어의 정렬과 비슷하게 구현할 수 있는 cmp_to_key함수를 사용해 정렬 했습니다. 본 과정은 key로써 정렬하게 되는 방법보다는 느리지만 확실하게 정렬하는 기준을 설정할 수 있기 때문에 알고리즘을 공부하신다면 무조건적으로 공부를 하시는 것을 추천합니다.
        - 위는 들어온 인수의 1번째 배열 값이 같으면 0번째를 비교해 X의 0번째가 Y의 0번째보다 크면 $X[0] > Y[0]$이라면 $X[0] - Y[0] > 0$ 이 되믈로 return 값이 양수가 나오게 되어 swap을 하는 형태입니다.
        - 위와 관련한 내용은 [여기](https://stackoverflow.com/questions/32752739/python-how-does-the-functools-cmp-to-key-function-works)(Stack Over Flow), [여기](https://velog.io/@sparkbosing/python-%EB%82%B4-%EB%A7%88%EC%9D%8C%EB%8C%80%EB%A1%9C-%EC%A0%95%EB%A0%ACsort) (Blog) 등등을 참고하면 좋을 듯 합니다.

---

## Number Theory

- 정수론
    - GCD, LCM, 빠른 거듭제곱, 모듈러 외에는 솔직히 코테 이상의 선수지식이 필요하기에 깊게 다루지 않아도 될 듯...?(더 잇을 수도 있음)
    - [http://theyearlyprophet.com/programming-contest-math.html#_10](http://theyearlyprophet.com/programming-contest-math.html#_10) - 프로그래밍 대회를 위한 수학 커리큘럼.
    - [https://data-make.tistory.com/408](https://data-make.tistory.com/408) - 이게 스터디 목적상 더 맞는 블로그라고 생각 됨.
- BOJ 1934번 최소공배수
    - source code

        ```python
        import sys
        import math

        T = int(sys.stdin.readline())
        arr = []
        for i in range(T):
            A, B = map(int, sys.stdin.readline().strip().split())
            print(math.lcm(A, B))
        ```

        - math.lcm은 python 3.9이상부터 사용가능[https://wikidocs.net/106253](https://wikidocs.net/106253) - 관련자료
- BOJ 11051번 이항계수 2
    - source code

        ```python
        import math

        n1, n2 = map(int, input().split())
        ans = math.factorial(n1) // math.factorial(n1 - n2) // math.factorial(n2)
        print(ans % 10007)
        ```

        - math.factorial도 구현되어 있음.

---

## @