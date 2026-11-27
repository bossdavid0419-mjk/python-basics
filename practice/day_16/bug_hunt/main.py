from models import TodoList, dict_to_task


def main():
    # 1. 할 일 2개를 만들고 2번만 완료
    todo_list = TodoList()
    todo_list.add("Python 공부")
    todo_list.add("운동하기")
    todo_list.complete(2)

    # 2. 저장했다가 다시 불러온 것처럼 딕셔너리로 바꿨다가 되돌리기
    saved = [task.to_dict() for task in todo_list.tasks]
    loaded = TodoList()
    for item in saved:
        loaded.tasks.append(dict_to_task(item))

    # 3. 불러온 목록 출력
    for task in loaded.tasks:
        print(task)

    # 4. 1번 삭제
    removed = loaded.delete(1)
    print(f"삭제: {removed.title}")


if __name__ == "__main__":
    main()