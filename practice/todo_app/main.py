from models import TodoList
from storage import save_todos, load_todos

todo_list = TodoList()

def show_menu():
    print("1. 할 일 목록보기")
    print("2. 할 일 추가")
    print("3. 할 일 완료 표시")
    print("4. 할 일 삭제")
    print("5. 완료된 할 일 보기")
    print("6. 미완료 할 일 보기")
    print("7. 할 일 검색")        
    print("0. 종료")

def get_number(message):
    try:
        number = int(input(message))
        return number
    except ValueError:
        return None

def print_task_list(task_list):
    if len(task_list) == 0:
        print("해당하는 할 일이 없습니다.")
        return

    for i, task in enumerate(task_list):
        print(f"{i + 1}. {task}")

def show_todos():
    if todo_list.count_all() == 0:
        print("할 일이 없습니다.")
        return
    
    print(f"전체 할 일: {todo_list.count_all()}개")
    print(f"완료된 할 일: {todo_list.count_done()}개")

    print("할 일 목록:")
    print_task_list(todo_list.tasks)

def select_todo_number(message):
    show_todos()

    if todo_list.count_all() == 0:
        return None
    number = get_number(message)

    if number is None:
        print("숫자를 입력해 주세요.")
        return None

    if not todo_list.is_valid_number(number):
        print("잘못된 번호입니다.")
        return None

    return number

def add_todo():
    title = input("할 일을 입력하세요: ").strip()

    if title == "":
        print("할 일 내용을 입력해 주세요.")
        return

    todo_list.add(title)

    print("할 일이 추가되었습니다.")
    save_todos(todo_list)

def complete_todo():
    number = select_todo_number("완료할 할 일 번호를 입력하세요: ")

    if number is None:
        return

    if todo_list.complete(number):
        print("할 일이 완료 처리되었습니다.")
        save_todos(todo_list)
    else:
        print("이미 완료된 할 일입니다.")

def delete_todo():
    number = select_todo_number("삭제할 할 일 번호를 입력하세요: ")

    if number is None:
        return
    
    removed = todo_list.delete(number)
    print(f"'{removed.title}' 할 일이 삭제되었습니다.")
    save_todos(todo_list)


def search_menu():
    keyword = input("검색할 단어를 입력하세요: ").strip()

    if keyword == "":
        print("검색어를 입력해 주세요.")
        return

    results = todo_list.search(keyword)
    print_task_list(results)

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

    if choice =="5":
        print_task_list(todo_list.get_done())
        return False

    if choice =="6":
        print_task_list(todo_list.get_not_done())
        return False

    if choice =="7":
        search_menu()
        return False

    if choice == "0":
        print("프로그램을 종료합니다.")
        return True

    print("잘못된 메뉴 번호입니다.")
    return False

def main():
    global todo_list
    todo_list = load_todos()

    while True:
        show_menu()
        choice = input("번호를 선택하세요: ")
        if run_menu(choice):
            break

if __name__ == "__main__":
    main()