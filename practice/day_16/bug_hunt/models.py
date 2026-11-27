class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def complete(self):
        if self.done:
            return False
        self.done = True
        return True

    def __str__(self):
        status = "(완료)" if self.done else "(미완료)"
        return f"{self.title} {status}"

    def to_dict(self):
        return {"title": self.title, "done": self.done}


def dict_to_task(data):
    task = Task(data["title"])
    task.done = data["done"]
    return task


class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, title):
        self.tasks.append(Task(title))

    def complete(self, number):
        return self.tasks[number - 1].complete()

    def delete(self, number):
        removed = self.tasks.pop(number - 1)
        return removed