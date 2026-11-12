student = {
    "name": "민재",
    "age": 20,
    "major": "컴퓨터공학"
}

print(student)
print(student["name"])
print(student["age"])
print(student["major"])

student["age"] = 21
print(student)

student["city"] = "서울"
print(student)

del student["city"]
print(student)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())
print(student.get("phone")) # .get()을 이용하면 NONE 혹은 지정한 기본값을 출력한다.
print(student["phone"]) # []로 조회하면 KEYERROR가 남