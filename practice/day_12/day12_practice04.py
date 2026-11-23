# 반복문으로 모든 할 일 제목을 출력

todos = [
    {
        "title": "Python 공부",
        "done": False
    },
    {
        "title": "운동하기",
        "done": True
    }
]

for todo in todos:
    print(todo["title"])