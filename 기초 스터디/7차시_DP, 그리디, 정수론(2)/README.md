## DP

- [2579번 계단오르기](https://www.acmicpc.net/problem/2579)
    - source code

        ```python
        import sys

        get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
        get_input: int = lambda: int(sys.stdin.readline())

        N = get_input()
        arr = {
            0: {'selected': 0, 'non_selected': 0, 'input': 0},
            1: {'selected': 0, 'non_selected': 0, 'input': 0},
            2: {'selected': 0, 'non_selected': 0, 'input': 0},
        }
        for i in range(3, N + 3):
            now = get_input()
            arr[i] = {
                'selected': max(
                    arr[i - 1]['input'] + arr[i - 3]['selected'], 
                    arr[i - 2]['non_selected'],
                    arr[i - 2]['selected']
                ) + now,
                'non_selected': max(
                    arr[i - 1]['selected'], 
                    arr[i - 1]['non_selected']
                ),
                'input': now
            }

        print(arr[N + 2]['selected'])
        ```

    - 이 문제의 핵심은 DP의 table을 어떻게 설정할 것이며 어떻게 활용할 것인가이다(당연한가...?)
    - arr[i]['select'] ⇒ i번째의 계단을 select했을 때의 최대 값
    - arr[i]['non_selected'] ⇒ i번째 계단을 select하지 않았을 때의 최대 값
    - arr[i]['input] ⇒ i번째 계단의 가중치
    - 이후 규칙을 잘 세우면 된다.
        - 규칙
            1. i번째를 선택하고 싶다.
                1. i번째를 선택하므로 i-1번째와 i-3을 선택하면서의 최대 값.
            2. i번째를 선택하고 싶지 않다.
                1. i-2번째를 선택한다.
            3. 다른 경우는 없다.( xxx 이런 경우 x 이유는 계단을 1칸 혹은 2칸밖에 오르지 못함)
- [1463번 1로 만들기](https://www.acmicpc.net/problem/1463)
    - source code

        ```python
        import sys

        get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
        get_input: int = lambda: int(sys.stdin.readline())

        N = get_input()
        arr = [0] * (N + 1)

        for i in range(2, N + 1):
            arr[i] = arr[i - 1] + 1
            if i % 2 == 0:
                arr[i] = min(arr[i // 2] + 1, arr[i])
            if i % 3 == 0:
                arr[i] = min(arr[i // 3] + 1, arr[i])

        print(arr[N])
        ```

    - 이 문제는 추후에 배울 그래프와 간선의 이미지로 생각하면 훨씬 더 쉽게 이해될 수 있습니다.

---

## Greedy

- [11399번 ATM](https://www.acmicpc.net/problem/11399)
    - source code

        ```python
        import sys

        get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
        get_input: int = lambda: int(sys.stdin.readline())

        N = get_input()
        arr = sorted(list(get_line()))
        ans = SUM = 0
        for i in arr:
            ans += SUM + i
            SUM += i

        print(ans)
        ```

    - 쉽게 생각해서 합을 계속 들고 다닌다고 생각하면 쉬울 듯. 이 문제는 description(문제) 이해가 90%라고 생각합니다
- [1541번 잃어버린 괄호](https://www.acmicpc.net/problem/1541)
    - source code

        ```python
        import sys
        import re

        get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
        get_input: int = lambda: int(sys.stdin.readline())

        input = sys.stdin.readline().rstrip()
        arr = list(map(int, re.split('[+-]', input)))
        pos = -1
        cnt = 0
        flag = True
        for i in input:
            if i == '-' or i == '+':
                cnt += 1
                if i == '-':
                    flag = False
                    break

        if cnt == 0:
            ans = arr[0]
        elif flag:
            ans = sum(arr[:cnt + 1])
        else:
            ans = sum(arr[:cnt]) - sum(arr[cnt:])

        print(ans)
        ```

    - regex를 이용해 '-' 위치 이후 모든 숫자는 전부 음수가 됨 이것이 이 문제의 해결 방식.

---

## Number Theory

- [2004번 조합 0의 개수](https://www.acmicpc.net/problem/2004)
    - source code

        ```python
        import sys

        get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
        get_input: int = lambda: int(sys.stdin.readline())

        N, M = get_line()
        K = N - M

        def div5(num):
            cnt = 0
            now = 5
            while now <= num:
                cnt += num // now
                now *= 5
            return cnt

        def div2(num):
            cnt = 0
            now = 2
            while now <= num:
                cnt += num // now
                now *= 2
            return cnt

        print(max(0, min(div5(N) - div5(K) - div5(M), div2(N) - div2(M) - div2(K))))
        ```

        - 지금은 함수를 2개로 작성했지만 1개로 줄일 수도 있으니 생각해보세요!
- [2168번 타일위의 대각선](https://www.acmicpc.net/problem/2168)
    - source code

        ```python
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
        ```

        - 직접 그려보며 x축 혹은 y축 1개의 값에 2개의 칸이 들어와야 하는 경우가 있는데 이 경우가 몇 가지인지 그리고 어떤 경우인지 생각하며 풀어보는 것도 좋을 듯 합니다.

---

## @