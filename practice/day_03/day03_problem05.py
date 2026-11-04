first_task = input("첫 번째 할 일: ")
second_task = input("두 번째 할 일: ")
third_task = input("세 번째 할 일: ")
tasks = [first_task, second_task, third_task]

print("[오늘의 할 일]")
print(tasks)
print(f"첫 번째: {tasks[0]}")
print(f"마지막: {tasks[-1]}")
print(f"총 {len(tasks)}개")
