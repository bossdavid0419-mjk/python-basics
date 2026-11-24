class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def complete(self):
        if self.done:
            print("이미 완료된 할 일입니다.")
            return

        self.done = True
        print("할 일이 완료 처리되었습니다.")

    def __str__(self):
        status = "(완료)" if self.done else "(미완료)"
        return f"{self.title} {status}"

tasks = [Task("Python 공부"), Task("운동하기"), Task("C++ 공부")]

tasks[1].complete()
tasks[1].complete()

for i, task in enumerate(tasks):
    print(f"{i + 1}. {task}")