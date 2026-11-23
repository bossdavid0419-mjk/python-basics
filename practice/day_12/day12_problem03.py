def get_not_done_todos(todos):
    return [todo for todo in todos if not todo["done"]]