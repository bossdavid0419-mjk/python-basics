def print_todo_list(todo_list):
    if len(todo_list) == 0:
        print("해당하는 할 일이 없습니다.")
        return

    for i, todo in enumerate(todo_list):
        status = "완료" if todo["done"] else "미완료"
        print(f"{i + 1}. {todo['title']} ({status})")
    
    