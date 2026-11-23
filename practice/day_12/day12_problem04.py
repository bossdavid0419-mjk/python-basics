def search_todos(todos, keyword):
    return [todo for todo in todos if keyword in todo["title"]]