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
- [BOJ 2447번 별 찍기 - 10](http://boj.kr/2447)
    - source code - 한준
- [BOJ 11729번 하노이 탑 이동 순서](https://www.acmicpc.net/problem/11729)
    - 참고 과정...?
    - source code - 한준
    - source code - 은지

---

## 백트래킹

- BOJ 9663번 N-Queen
    - 주의사항
    - source code - 한준
- BOJ 2580번 스도쿠
    - 주의사항
    - source code - 한준

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