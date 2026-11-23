# 이제 완료 여부도 함께 출력해 보자.

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
    print(todo["title"], "-", todo["done"])