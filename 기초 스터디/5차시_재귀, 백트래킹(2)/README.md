## 재귀

- [BOJ 1769번 3의 배수](https://www.acmicpc.net/problem/1769)
    - souce code

        ```python
        import sys

        cnt = 0

        def func1(s):
            global cnt
            if len(s) == 1:
                return 1 if int(s) % 3 == 0 else 0
            cnt += 1
            ret = 0
            for i in s:
                ret += int(i)
            return func1(str(ret))

        N = (sys.stdin.readline().rstrip())

        ans = "YES" if func1(N) == 1 else "NO"
        print(cnt)
        print(ans)
        ```

    - 주의 할 점
        - 1번 문제에서 2번 문제로 변환하는 개수만 세면 된다.
        - 기저사례를 잘 확인할 것.
- [BOJ 16505번 별](https://www.acmicpc.net/problem/16505)
    - source code

        ```python
        import sys

        N = int(sys.stdin.readline().rstrip())

        arr = [[' '] * 2 ** N for _ in range(2 ** N)]

        def reculsive(Y, X, N):
            if N == 0:
                arr[Y][X] = '*'
            else:
                N -= 1
                reculsive(Y + 2 ** N, X, N)
                reculsive(Y, X + 2 ** N, N)
                reculsive(Y, X, N)

        reculsive(0, 0, N)
        for i in arr:
            print(''.join(i).strip(), sep="",)
        ```

    - 주의사항

        문제에도 나와 있듯이 `각 줄 끝에는 필요없는 공백을 출력하지 않는다.`

        이를 만족하기 위해  저는 아래와 같이 작성했습니다

        - 해결법 - 1

            ```python
            for i in arr:
                print(''.join(i).strip(), sep="",)
            ```

            위는 배열에서는 알아서 잘 처리하되 strip을 이용해 만든 string의 시작과 끝에 존재하는 white space를 없애줌.

- [BOJ 18511번 큰 수 구성하기](https://www.acmicpc.net/problem/18511)
    - source code

        ```python
        import sys

        N, K = map(int, sys.stdin.readline().rstrip().split())
        arr = list(map(int, sys.stdin.readline().rstrip().split()))
        ans = 0

        def reculsive(value):
            if value > N:
                return
            global ans
            ans = max(ans,value)

            for i in arr:
                reculsive(value*10 + i)

        reculsive(0)
        print(ans)
        ```

- [BOJ 10994번 별찍기 - 19](https://www.acmicpc.net/problem/10994)
    - source code

        ```python
        import sys

        N = int(sys.stdin.readline().rstrip())
        arr = [[' '] * (N * 4 + -3) for _ in range(N * 4 + -3)]

        def drawLR(idx):
            if idx == N:
                return
            for i in range(idx * 2, N * 4 + - 3 - idx * 2):
                arr[i][idx * 2] = '*'
                arr[i][N * 4 - 4 - idx * 2] = "*"
            drawLR(idx + 1)

        def drawUD(idx):
            if idx == N:
                return
            for i in range(idx * 2, N * 4 + - 3 - (idx * 2)):
                arr[idx * 2][i] = "*"
                arr[N * 4 - 4 - idx * 2][i] = "*"
            drawUD(idx + 1)

        drawLR(0)
        drawUD(0)
        for i in arr:
            print(*i, sep="")
        ```

- [BOJ 16974번 레벨 햄버거](https://www.acmicpc.net/problem/16974)
    - source code

        ```python
        import sys

        N, X = map(int, sys.stdin.readline().rstrip().split())

        buger = [0] * (N + 1)
        patty = [0] * (N + 1)
        buger[0] = 1
        patty[0] = 1

        def bupa(cnt):
            if cnt == N:
                return
            buger[cnt] = buger[cnt - 1] * 2 + 3
            patty[cnt] = patty[cnt - 1] * 2 + 1
            bupa(cnt + 1)

        def cal(n, X):
            if X == 1:
                return 0
            elif buger[n - 1] + 1 > X:
                return cal(n - 1, X - 1)
            elif buger[n - 1] + 1 == X:  # 빵 + N-1번째 버거
                return patty[n - 1]
            elif buger[n - 1] + 2 == X:  # 빵 + N-1번째 버거 + 패티
                return patty[n - 1] + 1
            elif buger[n - 1] * 2 + 2 > X > buger[n - 1] + 2:  # 빵 + N-1번째 버거 + 패티 + 어느정도의 N-1번째 버거
                return 1 + patty[n - 1] + cal(n - 1, X - buger[n - 1] - 2)  # n-1번째 버거의 어느 정도와 N-1번째 버거의 패티 전체를 구함.
            elif buger[n - 1] * 2 + 2 == X:  # 빵 + N-1번째 버거 + 패티 + 어느정도의 N-1번째 버거
                return 1 + patty[n - 1] * 2  # n-1번째 버거의 어느 정도와 N-1번째 버거의 패티 전체를 구함.
            else:
                return buger[n]

        bupa(1)
        print(cal(N, X))
        ```

    - 주의할 점
        - 나처럼 저렇게까지 세분화 안해도 된다.
        - '필자'는 맞추고 싶어서 그냥 저렇게 까지 세분화 했고 합칠 수 있다.
    - source code  - 이석민(개인적으로 가독성 bb)

        ```python
        ### Author: 이석민 (ESukmean). 최대한 재귀호출 느낌을 살리려고 함.
        level, eat = map(int, input().split())

        # 한준님 코드에서는 bupa() 메서드로 되어있는 부분. 코드상에서 직관적으로 뭘 말하려는지 알 수 있도록 dict 구조로 만듦.
        preload = {0: {'all': 1, 'all_petti': 1, 'half': 0, 'half_petti': 0}}
        for i in range(1, level + 1):
        	last = preload[i - 1]
        	preload[i] = { 
        		'all': last['all'] * 2 + 3, 'all_petti': last['all_petti'] * 2 + 1,
        		'half': last['all'] + 1, 'half_petti': last['all_petti']
        	}

        ## 햄버거는 대칭구조를 이루고 있다는게 중요.
        ## 대칭구조이기에 앞쪽에서 탐색해도 되고, 뒤쪽에서 탐색해도 됨. 중간으로 짤라도 반절의 갯수는 항상 동일함을 유의

        # 이 함수는 "몇개의 패티를 먹었는지" 를 리턴함.
        def petti(level, eat):
        	# 먹을수 있는게 없으면 "0개의 패티를 먹은것"임
        	if eat == 0:
        		return 0
        	# 문제 조건에 따라서 레벨-0은 패티 갯수가 1개임. (위에서 eat을 검사한 덕분에, 여기 분기에서는 패티를 (최소한)1개 먹을수 있다는게 확실해짐)
        	if level == 0:
        		return 1

        	# 반보다 많이 남았을때
        	if eat > preload[level]['half']:
        		# 패티 반 + 중간 패티 + (나머지 절반은 다시 재귀로 갯수 계산하라고 보냄)
        		# 어짜피 대칭구조이기에, 반을 자르고 옆에거를 가지고 다시 탐색하면 편함. 굳이 옆에거를 또 계산한다고 삽질할 필요 ㄴㄴ
        		return preload[level]['half_petti'] + 1 + petti(level, eat - preload[level]['half'])

        	# 반보다 적게 남았을때
        	if eat < preload[level]['half']:
        		# 맨 앞에 감싸고 있는 빵을 먹고 다음 레벨로 들어감.
        		# 맨 마지막쪽에 있는 빵 영역은 다음 레벨에서 "반보다 더 남았을때" 케이스로 들어가서 반복됨.
        		# ==> 그러다가 맨 마지막 봉우리에서 level = 0이 되면서 더 탐색할 것 없이 꺼짐. 
        		#     ==> 전체 패티수와 버거수를 구하는게 아니라, 패티수만 구하면 되기 때문에 맨 마지막에 있는 빵만 있는곳은 신경 안써도 됨.
        		return petti(level - 1, eat - 1)

        	# 딱 절반이면 절반 만큼의 패티 갯수 빠르게 제출.
        	# if preload[level]['half'] == eat:
        	# 위에서 eat >, eat < 를 검사했기 때문에, 여기까지 왔단 말은 위의 if문을 만족한 경우밖에 안됨. 그런 상황에서 굳이 cost가 있는 if문을 쓸 필요 전혀없음
        	return preload[level]['half_petti']

        print(petti(level, eat))
        ```

    - 조그마한 커멘트를 달자면, 여러개의 계산이 있고 변수 여러개가 왔다갔다 할 때는 조금 cost가 있더라도 변수명을 바로 알 수 있는것으로 설정하는게 좋음. 알고리즘 연습에서는 꼭 필요없긴 한데, 실제 현업에 가서 죄다 수학식으로 가면 뭐가 뭔 코드인지 알아먹기 힘들어서 문제가 생길 수 있음.. (프로그램의 복잡성 증가) 특히 요즈음 컴파일러들은 "이름 붙이기용 변수" 같은거를 실제 변수로 안빼고 계산식에 바로 inline 시켜줌.
- [BOJ 21735번 눈덩이 굴리기](https://www.acmicpc.net/problem/21735)
    - source code

        ```python
        import sys

        N, M = map(int, sys.stdin.readline().strip().split())
        arr = [0] + list(map(int, sys.stdin.readline().strip().split()))

        dp = [[0] * (N+1) for _ in range(M+1)]
        ans = 0

        def DP(time, pos, value):
            if time > M :
                return
            global ans
            ans = max(ans, value)
            if pos + 1 <= N:
                DP(time + 1, pos + 1, value + arr[pos + 1])
            if pos + 2 <= N:
                DP(time + 1, pos + 2, value // 2 + arr[pos + 2])

        DP(0, 0, 1)
        print(ans)
        ```

    - 주의할 점
        - 기저사례 설정 및 Index 초과를 조심해야함.

---

## 백트래킹

---

## @