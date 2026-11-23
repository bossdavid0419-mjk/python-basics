# for 반복문과 if를 사용해서 완료된 할 일 제목만 출력해 봐.

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
    if todo["done"]:
        print(todo["title"])