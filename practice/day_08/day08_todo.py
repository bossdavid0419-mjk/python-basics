# Day 8: 작은 할 일 관리 프로그램

todos = []

def show_menu():
    print("1. 할 일 목록보기")
    print("2. 할 일 추가")
    print("3. 할 일 완료 표시")
    print("4. 할 일 삭제")
    print("5. 종료")

def add_todo():
    title = input("할 일을 입력하세요: ").strip()

    if title == "":
        print("할 일 내용을 입력해 주세요.")
        return

    todo = {
        "title": title,
        "done": False
    }

    todos.append(todo)
    print("할 일이 추가되었습니다.")

    save_todos()

def show_todos():
    if len(todos) == 0:
        print("할 일이 없습니다.")
        return
    else:
        print(f"전체 할 일: {len(todos)}개")

    print("할 일 목록:")
    for i, todo in enumerate(todos):
        status = "완료" if todo["done"] else "미완료"
        print(f"{i + 1}. {todo['title']} ({status})")

def complete_todo():
    show_todos()

    if len(todos) == 0:
        return

    try:
        number = int(input("완료할 할 일 번호를 입력하세요: "))
    except ValueError:
        print("숫자를 입력해 주세요.")
        return

    if number < 1 or number > len(todos):
        print("잘못된 번호입니다.")
        return

    if todos[number - 1]["done"]:
        print("이미 완료된 할 일입니다.")
    else:
        todos[number - 1]["done"] = True
        print("할 일이 완료 처리되었습니다.")
        save_todos()

def delete_todo():
    show_todos()

    if len(todos) == 0:
        return
    try:
        number = int(input("삭제할 할 일 번호를 입력하세요: "))
    except ValueError:
        print("숫자를 입력해 주세요.")
        return
    if number < 1 or number > len(todos):
        print("잘못된 번호입니다.")
        return

    removed = todos.pop(number - 1)
    print(f"'{removed['title']}' 할 일이 삭제되었습니다.")

    save_todos()

def save_todos():
    try:
        with open("todos.txt", "w", encoding="utf-8") as file:
            for todo in todos:
                file.write(f"{todo['title']}|{todo['done']}\n")
    except OSError:
        print("할 일을 저장하는 데 실패했습니다.")


def load_todos():
    try:    # 이렇게 try와 except를 사용해서 해당 루프에는 오류가 있을 수도 있으니 생략하고 코드를 돌린다는 의미야.
        with open("todos.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                try:
                    title, done = line.split("|")
                    done = done == "True"

                    todo = {
                        "title": title,
                        "done": done
                    }
                except ValueError:
                    continue
                todos.append(todo)
    except FileNotFoundError:   # except 뒤에는 어떤 오류를 무시할건지 작성하면 돼.
        print("저장된 할 일 파일이 없어 새로 시작합니다.")

load_todos()

while True:
    show_menu()
    choice = input("번호를 선택하세요: ")

    if choice == "1":
        show_todos()
    elif choice == "2":
        add_todo()
    elif choice == "3":
        complete_todo()
    elif choice == "4":
        delete_todo()
    elif choice == "5":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 메뉴 번호입니다.")