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
        task = Task(title)
        self.tasks.append(task)

    def count_all(self):
        return len(self.tasks)

    def count_done(self):
        return len([task for task in self.tasks if task.done])

    def count_not_done(self):
        return len([task for task in self.tasks if not task.done])

    def get_done(self):
        return [task for task in self.tasks if task.done]
    
    def get_not_done(self):
        return [task for task in self.tasks if not task.done]
    
    def search(self, keyword):
        return [task for task in self.tasks if keyword in task.title]

    def is_valid_number(self, number):
        if number >= 1 and number <= self.count_all():
            return True
        return False
    
    def complete(self, number):
        return self.tasks[number-1].complete()

    def delete(self, number):
        removed = self.tasks.pop(number-1)
        return removed