- [BOJ 10828번 스택](https://www.acmicpc.net/problem/10828)
    - source code

        ```python
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
        ```

    - 이 문제는 C++이 deque을 이용해 stack을 구현했듯이 python에서도 deque을 이용해서 해결하시면 됩니다.
    - Python에서는 list가 vector와 비슷하지만 deque의 popleft와 같은 제일 앞의 원소를 pop하는게 아닌 이상 list를 사용해도 무방합니다.
    - 저는 그래서 list를 이용해 push, pop, size, empty, top을 구현했습니다.
- [BOJ 10773번 제로](https://www.acmicpc.net/problem/10773)
    - source code

        ```python
        import sys

        get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
        get_input: int = lambda: int(sys.stdin.readline())

        K = get_input()
        arr = []
        for _ in range(K):
            now = get_input()
            if now == 0:
                arr.pop()
            else:
                arr.append(now)

        print(sum(arr))
        ```

    - 마지막 수를 없애는 과정이 stack 자료구조와 유사하게 행동합니다.
    - 1번 문제와 마찬가지로 stack의 기능을 deque할 수 있고 python에서는 popleft가 없는 deque를 list로 구현할 수 있기 때문에 list를 사용했습니다.
- [BOJ 9012번 괄호](https://www.acmicpc.net/problem/9012)
    - source code

        ```python
        import sys

        get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
        get_input: int = lambda: int(sys.stdin.readline())

        TC = get_input()
        for _ in range(TC):
            cnt = 0
            flag = True
            arr = sys.stdin.readline().rstrip()
            for i in arr:
                if i == '(':
                    cnt += 1
                else:
                    if cnt != 0:
                        cnt -= 1
                    else:
                        flag = False
                        break;
            print("YES" if flag and cnt == 0 else "NO")
        ```

    - 이 문제 또한 스택을 이용해서 해결할  수 있습니다.
    - 하지만 굳이 스택을 이용해서 풀 것 없이 `현재까지 쌍을 이루지 않은 '('의 갯수가 0미만이 되는 순간이 있거나 모든 문자열을 탐색 완료 했을 때 쌍을 이루지 않은 '('가 존재한다면 그것은 올바른 괄호 문자열이 아닙니다.`
- [BOJ 18258번 큐 2](https://www.acmicpc.net/problem/18258)
    - source code

        ```python
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
        ```

    - 이 문제는 queue가 아닌 deque를 활용해서 해결할 수 있습니다.
    - 하지만 저는 굳이 그럴 필요 없이 앞을 가리키는 cursor 라는 개념을 두어 그것을 이용해 front 및 size 계산을 진행했습니다.
    - 당연하게도 popleft를 실질적으로 구현하지 않은 코드이기에 그것과 관련된 내용은 구글을 참고하길 바랍니다
- [BOJ 11866번 오세푸스 문제 0](https://www.acmicpc.net/problem/11866)
    - source code

        ```python
        import sys
        from collections import deque

        N, K = map(int, sys.stdin.readline().strip().split())
        deq = deque()

        for i in range(1, N+1):
            deq.append(i)

        print('<', end="")

        while deq: # 큐가 비어있지 않다면 반복 실행
            for i in range(K-1):
                deq.append(deq.popleft())

            print(deq.popleft(), end="")

            if deq:
                print(", ", end="")

        print('>')
        ```

    - 코드는 popleft 함수는 return 값이 popleft 한 인자이므로 pop과 동시에 append가 일어납니다. 이를 활용해 K-1개를 지나가고 K번째는 가장 앞에 존재하게 하여 popleft를 진행하며 없앱니다.
- [BOJ 1966번 프린터 큐](https://www.acmicpc.net/problem/1966)
    - source code

        ```python
        import sys

        get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
        get_input: int = lambda: int(sys.stdin.readline())

        from queue import PriorityQueue
        from collections import deque

        TC = get_input()
        for i in range(TC):
            N, M = get_line()
            pq = PriorityQueue()
            dq = deque()
            arr = list(get_line())
            for idx, j in enumerate(arr):
                pq.put(-j)
                dq.append((idx, j))
            cnt = 1
            while dq:
                if dq[0][1] == -pq.queue[0]:  # 최대 값과 중요도가 같으면 pop함.
                    if dq[0][0] == M:  # 이때 우리가 원하는 index의 값과 같으면 출력함.
                        print(cnt)
                        break
                    dq.popleft()
                    pq.get()
                    cnt += 1
                else:
                    dq.append(dq.popleft())
        ```

    - Python Priority Queue 사용법
        - C++의 pq.top() ⇒ pq.queue[0]
        - 모듈 import 방법

            ```python
            from queue import PriorityQueue
            ```

    - Python의 마지막 요소가 아닌 임의의 요소 pop의 Time complexity
        - link :[https://stackoverflow.com/questions/195625/what-is-the-time-complexity-of-popping-elements-from-list-in-python/46136638](https://stackoverflow.com/questions/195625/what-is-the-time-complexity-of-popping-elements-from-list-in-python/46136638)
        - 마지막 요소는 $O(N)$ 임의의 경우는 해당 위치까지 iterator가 이동해야 하므로 $O(N)$입니다
        - 여러가지의 Time complexity를 알려주는 link: [https://wiki.python.org/moin/TimeComplexity](https://wiki.python.org/moin/TimeComplexity)

---

# @