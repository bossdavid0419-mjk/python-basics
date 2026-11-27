# Day 15 - 저장 형식을 JSON으로 바꾸기

## JSON이란
- 데이터를 텍스트로 저장하거나 주고받을 때 쓰는 표준 형식
- 생김새는 파이썬 리스트·딕셔너리와 거의 같다.
- 차이: true/false/null(소문자), 문자열은 큰따옴표만
- 웹 API(FastAPI), 설정 파일 등에서 계속 쓰인다.

## txt 대신 JSON을 쓰는 이유
- 제목에 `|`가 들어가도 할 일이 사라지지 않는다. (Day 11에 남겨 둔 버그 해결)
- "True" 같은 글자를 직접 bool로 바꿀 필요가 없다.
- 키 이름으로 저장해서, 항목이 늘어나도 순서를 외울 필요가 없다.

## json 모듈
| 함수 | 하는 일 |
|---|---|
| json.dump(data, file) | 파이썬 데이터 → JSON 파일 |
| json.load(file) | JSON 파일 → 파이썬 데이터 |
| json.dumps(data) | 파이썬 데이터 → JSON 문자열 (파일 X) |
| json.loads(text) | JSON 문자열 → 파이썬 데이터 |
- s는 string(문자열)의 s
- ensure_ascii=False: 한글을 그대로 저장
- indent=4: 사람이 읽기 좋게 줄바꿈·들여쓰기

## Task ↔ 딕셔너리
- json은 Task 객체를 직접 저장하지 못한다. → 딕셔너리로 바꿔서 저장
- Task.to_dict(): Task → {"title": ..., "done": ...}
- dict_to_task(data): 딕셔너리 → Task
- 왕복 테스트: task.to_dict() == data 가 True면 두 변환이 맞게 짝지어진 것

```text
저장:  Task들 → (to_dict) → 딕셔너리 리스트 → (json.dump) → todos_v2.json
읽기:  todos_v2.json → (json.load) → 딕셔너리 리스트 → (dict_to_task) → Task들
```

## 예외 처리
| 예외 | 언제 | 처리 |
|---|---|---|
| FileNotFoundError | 저장 파일이 없을 때 | 새로 시작 |
| json.JSONDecodeError | 파일 내용이 JSON 형식이 아닐 때 | 안내하고 새로 시작 |
| KeyError | 할 일 하나에 키가 없을 때 | 그 할 일만 continue로 건너뛰기 |
- 파일 전체 문제는 바깥 try, 할 일 하나의 문제는 반복문 안쪽 try

## 헷갈렸던 것
- 메서드에는 대괄호를 쓸 수 없고, 실행하려면 괄호가 필요하다. (task.to_dict())
- json.dump에는 클래스(Task)가 아니라 만든 데이터(data)를 넘긴다.
- except OSError는 파일 에러만 잡는다. NameError 같은 다른 에러는 못 잡는다.
- 저장할 데이터는 파일을 열기 전에 만들어 두면, 중간에 문제가 생겨도 기존 파일이 비지 않는다.
- JSON은 마지막 항목 뒤에 쉼표가 있으면 형식 오류다.
- .gitignore에는 *.json 대신 todos_v2.json처럼 파일 이름을 적는다.