# 문제 1: JSON 저장하고 읽기
import json

data = [
    {"title": "Python 공부", "done": False},
    {"title": "책|영화 정리", "done": True},     # 제목에 | 가 들어간 할 일
]

# 저장: 파이썬 데이터 → JSON 파일
with open("test.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# 불러오기: JSON 파일 → 파이썬 데이터
with open("test.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

print(loaded)                     # 저장한 리스트가 그대로 돌아왔는지
print(loaded[1]["title"])         # '|'가 들어간 제목이 깨지지 않았는지 → txt 방식에선 사라지던 할 일
print(loaded[1]["done"])          # True → 글자 "True"가 아니라 진짜 bool로 돌아왔는지
print(type(loaded[1]["done"]))    # <class 'bool'> → 직접 변환할 필요가 없다는 확인


# 문제 2~3 테스트용 Task 클래스 (to_dict 포함)
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

# 문제 3: dict_to_task 함수
def dict_to_task(data):
    task = Task(data["title"])
    task.done = data["done"]
    return task


# 문제 2 테스트
task = Task("Python 공부")
print(task.to_dict())             # {'title': 'Python 공부', 'done': False} → 새 할 일은 미완료

task.complete()
print(task.to_dict())             # {'title': 'Python 공부', 'done': True} → 완료 후 상태가 반영되는지

print(json.dumps(task.to_dict(), ensure_ascii=False))
# {"title": "Python 공부", "done": true} → 딕셔너리로 바꾸면 json이 처리할 수 있는지

# 문제 3 테스트
data1 = {"title": "Python 공부", "done": False}
data2 = {"title": "책|영화 정리", "done": True}

task1 = dict_to_task(data1)
task2 = dict_to_task(data2)

print(task1)                      # Python 공부 (미완료) → Task 객체로 바뀌어서 __str__로 출력되는지
print(task2)                      # 책|영화 정리 (완료) → 완료 상태까지 그대로 옮겨졌는지
print(type(task2))                # <class '__main__.Task'> → 딕셔너리가 아니라 Task 객체인지

print(task2.to_dict() == data2)   # True → 딕셔너리 → Task → 딕셔너리로 돌아와도 내용이 같은지