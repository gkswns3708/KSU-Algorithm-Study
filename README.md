## 기초 입출력

1. 기초 입출력

    ```python
    # 기본적으로는 input을 통해 입력을 받을 수 있다.
    A = int(input())
    A = map(int, input().split())
    ```

2. 조금 더 나아간 입출력 (보편적)

    ```python
    import sys

    A = int(sys.stdin.readline()) # 한 줄에 1개의 숫자가 입력될 경우
    A = list(map(int, sys.stdin.readline().rstrip().split())) # 한 줄에 여러개의 숫자가 입력될 경우
    A = sys.stdin.readline() # 한 줄에 1개의 string이 입력될 경우
    A = list(sys.stdin.readline().rstrip().split()) # 한 줄에 여러개의 string이 입력될 경우
    ```

3. + @ 많은 입출력이 요구되어 타이핑을 줄이는 용도

    ```python
    # + @ 더 알아놓으면 좋은 
    get_line = lambda : map(int, sys.stdin.readline().rstrip().split())
    input = lambda : int(sys.stdin.readline())

    # 원본 함수를 lambda형으로 연결해놔서 원본 객체를 참조하지 않음.
    get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
    get_input: int = lambda: int(sys.stdin.readline())

    # ----
    # 여러 줄을 한번에 받을 때 사용 (입력받고 후처리 혹은 전체가 string 자료형일 때 사용)
    sys.stdin.readlines()
    sys.stdin.read().splitlines() # 이게 조금 더 좋은 역할의 다중 입력을 처리해 주는 듯...?
    ```

    출처 : [지원이 형 깃헙](https://github.com/JiwonDev/BOJ-Algorithm-python)

---

## 나머지 정리

- 길이가 정해진 리스트 만들기

    ```python
    list = [0 for i in range(n)] # 초기값이 0이고 길이가 n인 list 만들기
    matrix = [[0 for col in range(n)] for row in range(n)] # 0으로 초기화된 2차원 배열
    ```

- 내가 원하는 대로 정렬 (custom comparator)

    ```python
    from functools import cmp_to_key
    def compare(x ,y):
    		...
    sorted(arr, key=cmp_to_key(compare)) # 이러한 형식으로 사용 return 1이면 교환해야할 때 그대로 둘 때 0, -1
    # 만약 어떤 key값으로 정렬을 하고 싶다? 예를 들어서 

    [[1, 3], [4, 2], [4, 1], [5, 3]]에서 각 자료형의 합의 순서로 정렬하고 싶다
    def sorting_func(lst):
      return lst[0] + lst[1]

    sorted_lst = sorted(lst, key= sorting_func)
    print(sorted_lst)
    # OUTPUT
    [[1, 3], [4, 1], [4, 2], [5, 3]] # 4, 5, 6, 8 이런게도 사용 가능.
    ```

일반적인 sort 알고리즘의 경우 python의 default sorting algorithm은 **TimSort**이다.

## 출력

- f-string ( f-formatting)

    ```python
    print(f"{연산 혹은 변수에 관한 내용}")
    print("{0} 처럼 소숫점의 자릿수를 정할 수 도 잇음.".format()
    print("{:.3f}%".format(cnt*100/tmp[0]))
    print(f"{cnt/N*100:.3f}")
    ```

    [https://andamiro25.tistory.com/16](https://andamiro25.tistory.com/16) - 포멧팅에 관한 블로그 포스팅

    [https://ming-jee.tistory.com/124](https://ming-jee.tistory.com/124) - 문제를 풀기 위한 formatting 포스팅 (소수점 고정)

- while - else

    ```python
    while 조건문 : 
    		...
    else:
    		# while문이 조건문을 통해 탈출된 경우에 else문이 실행됨.
    		# break문 같은 구문으로 탈출한 경우엔 해당되지 않음.

    ```

- sys.stdin.readline().rstrip() , .strip(), lstrip()

    ```python
    sys.stdin.readline().rstrip() , .strip(), lstrip()
    # rstrip은 오른쪽 공백을 삭제
    # lsrtip은 왼쪽 공백을 삭제
    # strip은 왼쪽 오른쪽 공백 모두 삭제
    # 매개변수는 default는 공백문자, 있으면 해당 char 값들을 전부 제거
    ```
