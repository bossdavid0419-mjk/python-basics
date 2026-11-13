tasks = [
    {
        "title": "Python 공부",
        "done": False
    },
    {
        "title": "운동",
        "done": False
    },
    {
        "title": "독서",
        "done": False
    }
]

tasks[1]["done"] = True

for i in range(len(tasks)):
    if tasks[i]["done"]:
        print(f"{i + 1}. {tasks[i]['title']} - 완료")
    else:
        print(f"{i + 1}. {tasks[i]['title']} - 미완료")

done_count = 0

for task in tasks:
    if task["done"]:
        done_count += 1

print(f"완료된 할 일: {done_count}개")