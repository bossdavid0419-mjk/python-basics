# Day 6: 딕셔너리 심화

# 1. 딕셔너리 안에 리스트 넣기

student = {
    "name": "민재",
    "age": 20,
    "hobbies": ["게임", "운동", "코딩"]
}

print(student["name"])
print(student["hobbies"])

# 리스트 안의 값 하나만 꺼내기
print(student["hobbies"][0])
print(student["hobbies"][2])

# 2. 리스트에 새 취미 추가하기

student["hobbies"].append("영화 보기")

print(student["hobbies"])

# 3. 딕셔너리 안에 딕셔너리 넣기

user = {
    "name": "민재",
    "login": {
        "id": "minjae",
        "password": "1234"
    }
}

print(user["name"])
print(user["login"])
print(user["login"]["id"])

# 4. 리스트 안에 딕셔너리 넣기

friends = [
    {"name": "철수", "age": 21},
    {"name": "영희", "age": 22},
    {"name": "민수", "age": 23}
]

print(friends[0])
print(friends[1]["name"])
print(friends[2]["age"])

# 5. for문으로 리스트 안의 딕셔너리 꺼내기

for friend in friends:
    print(friend["name"], friend["age"])

# 6. 조건문과 함께 사용하기

for friend in friends:
    if friend["age"] >= 22:
        print(friend["name"], "은 22세 이상입니다")

# 7. 딕셔너리 값 수정하기

student["age"] = 21

print(student)

# 8. 딕셔너리에 새 키 추가하기

student["school"] = "대학교"

print(student)

# 9. 딕셔너리에서 값 꺼내기

age = student.get("age")
print(age)

# 10. 없는 키를 꺼낼 때 기본값 사용하기

phone = student.get("phone", "전화번호 없음") #.get을 사용하면 없는 값을 조회해도 에러가 뜨지 않고 기본값으로 none을 출력하고, 따로 출력할 문구가 있으면 이처럼 "전화번호 없음"로 설정도 할 수 있음
print(phone)
