from pathlib import Path

DATA_FILE = Path(__file__).parent / "todos_v2.json"

import json

from models import dict_to_task, TodoList

def save_todos(todo_list):
    try:
         data = [task.to_dict() for task in todo_list.tasks]
         with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except OSError:
        print("할 일을 저장하는 데 실패했습니다.")

def load_todos():
    todo_list = TodoList()

    try:    # try 안에서 그 오류가 나면 except 코드를 대신 실행한다
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

            for item in data:
                try:
                    task = dict_to_task(item)
                except KeyError:
                    continue

                todo_list.tasks.append(task)
    except FileNotFoundError:   # except 뒤에는 어떤 오류를 무시할건지 작성하면 돼.
        print("저장된 할 일 파일이 없어 새로 시작합니다.")
    except json.JSONDecodeError:
        print("저장 파일이 손상되어 새로 시작합니다.")
    return todo_list