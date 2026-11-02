name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")

print("안녕하세요,", name, "님!")
print("나이:", age)

birth_year = 2026 - int(age)

print(f"{name}님은 {birth_year}년생으로 추정됩니다.")
print(f"5년 뒤 나이는 {int(age) + 5}살입니다.")