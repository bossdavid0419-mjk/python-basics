# Day 9: 파일 다루기

## 학습 목표

- `open()`으로 텍스트 파일을 열고 닫는다.
- `"r"`, `"w"`, `"a"` 모드의 차이를 이해한다.
- `with` 문으로 파일을 안전하게 사용한다.
- `write()`로 파일에 내용을 저장한다.
- `read()`로 파일 전체 내용을 읽는다.
- `for line in file:`로 파일을 한 줄씩 읽는다.
- `strip()`으로 문자열 앞뒤 공백과 줄바꿈을 제거한다.

## 파일을 왜 사용하나

변수와 리스트는 프로그램이 종료되면 사라진다.  
하지만 파일에 저장한 데이터는 프로그램을 다시 실행해도 남아 있다.

예를 들어 할 일 관리 프로그램에서 `todos` 리스트에 할 일을 저장하면, 프로그램을 끄면 목록이 사라진다.  
파일에 저장하면 다음에 프로그램을 실행할 때도 이전 할 일을 불러올 수 있다.

## `open()` 기본 형태

```python
open("파일이름", "모드", encoding="utf-8")
```

| 순서 | 입력값 | 의미 | 예시 |
|---|---|---|---|
| 1 | 파일 이름 | 열거나 만들 파일 | `"goals.txt"` |
| 2 | 모드 | 파일을 어떻게 다룰지 | `"r"`, `"w"`, `"a"` |
| 3 | 인코딩 | 텍스트 저장 방식 | `encoding="utf-8"` |

## 파일 모드

| 모드 | 뜻 | 기존 파일이 있을 때 |
|---|---|---|
| `"r"` | read, 읽기 | 내용을 읽기만 함 |
| `"w"` | write, 쓰기 | 기존 내용을 지우고 새로 저장 |
| `"a"` | append, 추가 | 기존 내용을 유지하고 맨 뒤에 추가 |

`"w"`는 파일을 여는 순간 기존 내용을 지운다.  
그래서 기존 내용을 수정해서 다시 저장할 때는 먼저 내용을 읽고, 수정한 뒤 `"w"`로 저장해야 한다.

`"a"`는 기존 내용을 지우지 않고 파일 맨 뒤에 새 내용을 추가한다.

## `with` 사용하기

```python
with open("goals.txt", "w", encoding="utf-8") as file:
    file.write("Python 공부하기\n")
```

`with` 블록이 끝나면 파일이 자동으로 닫힌다.  
그래서 파일을 직접 `close()`하지 않아도 된다.

## 파일에 쓰기

```python
with open("goals.txt", "w", encoding="utf-8") as file:
    file.write("Python을 꾸준히 공부하기\n")
    file.write("운동 습관 만들기\n")
    file.write("영어 공부하기\n")
```

- `"w"` 모드는 기존 내용을 지우고 새로 저장한다.
- `\n`은 줄바꿈이다.
- `write()`는 자동으로 줄을 바꾸지 않는다.

## 파일 전체 읽기

```python
with open("goals.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```

`read()`는 파일 전체를 하나의 문자열로 읽는다.

## 파일을 한 줄씩 읽기

```python
with open("goals.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(f"목표: {line.strip()}")
```

- `for line in file:`은 파일을 한 줄씩 읽는다.
- `line.strip()`은 줄 끝의 `\n`과 앞뒤 공백을 제거한다.
- f-string으로 각 줄 앞에 원하는 문구를 붙일 수 있다.

## 파일에 추가하기

```python
with open("goals.txt", "a", encoding="utf-8") as file:
    file.write("하루 30분 운동하기\n")
```

`"a"` 모드는 기존 내용을 유지하고 새 내용을 맨 뒤에 추가한다.

## 사용자 입력 저장하기

```python
memo = input("오늘의 메모를 입력하세요: ").strip()

if not memo:
    print("메모를 입력해 주세요.")
else:
    with open("diary.txt", "w", encoding="utf-8") as file:
        file.write(memo + "\n")

    with open("diary.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
```

- `input()`은 사용자 입력을 문자열로 받는다.
- `.strip()`은 입력값 앞뒤 공백을 제거한다.
- `if not memo:`는 빈 문자열을 검사한다.
- 빈 입력이면 파일을 열지 않고 안내만 출력한다.
- 정상 입력이면 파일에 저장하고 다시 읽어 출력한다.

## 문자열 바꾸기

```python
content = content.replace("공부했다.", "Python을 공부했다.")
```

- `replace(a, b)`는 문자열에서 `a`를 찾아 `b`로 바꾼 새 문자열을 만든다.
- 원래 문자열을 직접 바꾸지 않으므로 결과를 변수에 저장해야 한다.
- 파일의 중간 내용을 바꾸려면 파일을 읽고, 문자열을 수정한 뒤, `"w"` 모드로 다시 저장한다.

## 배운 점

- 파일은 프로그램이 종료된 뒤에도 데이터를 남긴다.
- `"w"`는 덮어쓰기, `"a"`는 뒤에 추가, `"r"`은 읽기다.
- `with`를 쓰면 파일을 자동으로 닫을 수 있다.
- `write()`에는 줄바꿈 `\n`을 직접 넣어야 한다.
- `strip()`은 문자열 앞뒤 공백과 줄바꿈을 제거한다.
- 파일을 다룰 때는 열기 → 사용 → 닫기 순서를 지켜야 한다.