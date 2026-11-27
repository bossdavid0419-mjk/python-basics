# Day 16 - 파일 나누기(모듈)와 가상환경

## 모듈과 import
- 파이썬 파일 하나 = 모듈 하나. 내가 만든 파일도 import할 수 있다.
- import 할 때는 .py를 빼고 파일 이름만 쓴다.

| 방법 | 쓰는 법 |
|---|---|
| import calc | calc.add(3, 5) |
| from calc import add | add(3, 5) |

- 파일을 import하면 그 파일 코드가 위에서부터 한 번 실행된다.
- 파일마다 이름을 따로 관리한다. 다른 파일의 변수·클래스는 import해야 보인다.
- import한 이름과 같은 이름으로 다시 class를 정의하면, 가져온 것을 덮어쓴다.
- from models import *처럼 전부 가져오는 건 무엇이 들어왔는지 안 보여서 쓰지 않는다.

## __name__
| 실행 방법 | 그 파일의 __name__ |
|---|---|
| 직접 실행 | "__main__" |
| 다른 파일에서 import | 파일 이름 (예: "calc") |

```python
def main():
    ...

if __name__ == "__main__":
    main()
```
- 직접 실행할 때만 main()이 돌고, import될 때는 돌지 않는다.
- 앞뒤에 밑줄 두 개(던더)가 붙은 이름은 파이썬이 정해 둔 특별한 이름이다.
  (__init__, __str__, __name__, __file__, "__main__")

## 할 일 앱 구조 (practice/todo_app/)
| 파일 | 내용 |
|---|---|
| models.py | Task, TodoList, dict_to_task |
| storage.py | save_todos(todo_list), load_todos() |
| main.py | 메뉴 함수, main() |

- storage.py는 전역 변수 없이, 매개변수로 받고 return으로 돌려준다.
- main.py에서 함수 안의 전역 변수를 바꿀 때는 global todo_list로 먼저 선언한다.

## 저장 파일 위치 고정
```python
from pathlib import Path
DATA_FILE = Path(__file__).parent / "todos_v2.json"
```
- 파일 이름만 쓰면 터미널이 있는 폴더를 기준으로 찾는다.
- __file__: 이 코드가 들어 있는 파일의 경로, .parent: 그 폴더, /: 경로 잇기
- 바뀌지 않는 값(상수)은 대문자로 이름 짓는다.

## 가상환경과 uv
- 가상환경: 프로젝트마다 따로 쓰는 파이썬 상자. 패키지가 그 프로젝트에만 설치된다.
- source .venv/bin/activate (켜기), deactivate (끄기), which python (확인)
- uv: pip·venv보다 빠른 도구. uv pip install pytest
- .venv는 컴퓨터마다 만드는 것이라 GitHub에 올리지 않는다.

## 버그 찾기 연습에서 찾은 것
- from model → 파일 이름은 models (실행 에러)
- if __name__ == "main" → "__main__" (아무것도 실행 안 됨)
- task.done = data["title"] → data["done"] (모든 할 일이 완료로 보임)
- pop(number) → pop(number - 1) (다른 할 일이 지워짐)

## 헷갈렸던 것
- TodoList를 models.py로 복사만 하고 main.py에 남겨서 NameError: Task
- save_todos(save_todos)처럼 목록 대신 함수를 넘겨서 AttributeError
- 에러 메시지의 File 줄 중 아래쪽이 실제로 멈춘 곳, 그 위가 이상한 값을 넘긴 곳
- python 없이 파일 경로만 입력하면 permission denied
- 터미널에서 명령어 뒤에 # 설명을 붙이면 zsh가 명령어로 읽어서 에러가 난다.