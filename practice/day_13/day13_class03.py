# 클래스 예시

class Dog:
    def __init__(self, name, age):   # 생성자: 객체를 만들 때 자동 실행
        self.name = name              # 속성 저장
        self.age = age

    def bark(self):                   # 메서드
        print(f"{self.name}: 멍멍!")

    def birthday(self):
        self.age += 1                 # 자기 속성을 바꿀 수 있음


dog1 = Dog("초코", 3)    # 객체 만들기 → __init__이 실행됨
dog2 = Dog("콩이", 5)

dog1.bark()             # 초코: 멍멍!
dog2.bark()             # 콩이: 멍멍!

dog1.birthday()
print(dog1.age)         # 4
print(dog2.age)         # 5 → dog2는 영향 없음

# 3번 문제

class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def introduce(self):
        print(f"안녕하세요, {self.major} {self.name}입니다.")

s1 = Student("민재", "소프트웨어학부")
s2 = Student("철수", "기계공학과")

s1.introduce()
s2.introduce()