# Day 14 - 할 일 관리 프로그램을 클래스로 바꾸기

## 바뀐 구조
- Task: 할 일 하나 (title, done, complete(), __str__)
- TodoList: 할 일 목록 전체 (self.tasks와 목록을 다루는 메서드)
- 메뉴 함수: input()으로 입력받고 print()로 출력하는 일만 맡는다.
- 원칙: 클래스는 데이터와 계산만, 메뉴 함수는 사용자와 대화만

## 함수 → 메서드
| v1 (Day 8~12) | v2 (Day 14) |
|---|---|
| todos.append(make_todo(title)) | todo_list.add(title) |
| count_done_todos(todos) | todo_list.count_done() |
| get_done_todos(todos) | todo_list.get_done() |
| search_todos(todos, keyword) | todo_list.search(keyword) |
| is_valid_number(number) | todo_list.is_valid_number(number) |
| todos.pop(number - 1) | todo_list.delete(number) |
| todo["done"], todo["title"] | task.done, task.title |

## 배운 것
- 메서드 안에서는 바깥 변수(todo_list)가 아니라 self를 쓴다.
- 메서드 안에서 같은 객체의 다른 메서드를 부를 때도 self.count_all()처럼 쓴다.
- 메서드를 실행하려면 괄호가 필요하다. self.count_all은 메서드 자체, self.count_all()은 결과다.
- 값 없는 return은 None을 돌려준다.
- 중간 메서드가 결과를 return하지 않으면 결과가 거기서 끊긴다. (메뉴 → TodoList → Task)
- 출력하는 대신 True/False를 return하면, 부르는 쪽이 메시지를 고를 수 있다.
- 사용자 번호(1부터)와 리스트 위치(0부터) 계산은 클래스 안에서 한 번만 한다.
- 범위에 끝값을 포함하려면 >=, <=를 쓴다.
- 출력 함수는 받은 매개변수를 써야 어떤 리스트든 출력할 수 있다.
- 반복문 안에서 반복문이 있는 함수를 부르면 출력이 여러 번 반복된다.

## 헷갈렸던 것
- complete()에 리스트 컴프리헨션을 쓴 것 → 할 일 하나를 다룰 때는 필요 없다.
- self.tasks[number]처럼 꺼내기만 하고 메서드를 안 부른 것
- print_task_list 안에서 task_list 대신 todo_list.tasks를 쓴 것
- todo를 task로 한꺼번에 바꾸면 todo_list 같은 다른 이름까지 바뀐다 → VS Code F2로 변수만 바꾸기