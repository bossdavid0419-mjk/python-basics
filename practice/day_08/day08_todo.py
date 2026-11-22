# Day 8: 작은 할 일 관리 프로그램

todos = []

def show_menu():
    print("1. 할 일 목록보기")
    print("2. 할 일 추가")
    print("3. 할 일 완료 표시")
    print("4. 할 일 삭제")
    print("5. 종료")

def make_todo(title):
    todo = {
        "title": title,
        "done": False
    }

    return todo

def add_todo():
    title = input("할 일을 입력하세요: ").strip()

    if title == "":
        print("할 일 내용을 입력해 주세요.")
        return

    todo = make_todo(title)

    todos.append(todo)
    print("할 일이 추가되었습니다.")

    save_todos()

def count_done_todos():
    done_count = 0
    for todo in todos:
        if todo["done"]:
            done_count += 1
    return done_count

def show_todos():
    if len(todos) == 0:
        print("할 일이 없습니다.")
        return
    
    print(f"전체 할 일: {len(todos)}개")
    print(f"완료된 할 일: {count_done_todos()}개")

    print("할 일 목록:")
    for i, todo in enumerate(todos):
        status = "완료" if todo["done"] else "미완료"
        print(f"{i + 1}. {todo['title']} ({status})")

def get_number(message):
    try:
        number = int(input(message))
        return number
    except ValueError:
        return None

def is_valid_number(number):
    if number < 1 or number > len(todos):
        return False
    return True

def select_todo_number(message):
    show_todos()

    if len(todos) == 0:
        return None
    number = get_number(message)

    if number is None:
        print("숫자를 입력해 주세요.")
        return None

    if not is_valid_number(number):
        print("잘못된 번호입니다.")
        return None

    return number


def complete_todo():
    number = select_todo_number("완료할 할 일 번호를 입력하세요: ")

    if number is None:
        return
    
    if todos[number - 1]["done"]:
        print("이미 완료된 할 일입니다.")
    else:
        todos[number - 1]["done"] = True
        print("할 일이 완료 처리되었습니다.")
        save_todos()

def delete_todo():
    number = select_todo_number("삭제할 할 일 번호를 입력하세요: ")

    if number is None:
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
    try:    # try 안에서 그 오류가 나면 except 코드를 대신 실행한다
        with open("todos.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                try:
                    title, done = line.split("|")
                    if done != "True" and done != "False":
                        continue 
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

def run_menu(choice):
    if choice == "1":
        show_todos()
        return False

    if choice =="2":
        add_todo()
        return False

    if choice =="3":
        complete_todo()
        return False

    if choice =="4":
        delete_todo()
        return False

    if choice == "5":
        print("프로그램을 종료합니다.")
        return True

    print("잘못된 메뉴 번호입니다.")
    return False

while True:
    show_menu()
    choice = input("번호를 선택하세요: ")

    if run_menu(choice):
        break