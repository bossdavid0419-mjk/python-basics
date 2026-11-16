# Day 7: 함수

# 1. 가장 기본적인 함수

def say_hello():
    print("안녕하세요!")

say_hello()
say_hello()

# 2. 매개변수가 있는 함수

def greet(name):
    print("안녕하세요,", name, "님!")

greet("민재")
greet("철수")

# 3. 두 개의 매개변수

def introduce(name, age):
    print("제 이름은", name, "이고 나이는", age, "살입니다.")

introduce("민재", 21)
introduce("영희", 22)

# 4. 반환값이 있는 함수

def add(a, b):
    return a + b

result = add(3, 5)
print(result)

# 5. 여러 번 사용하기

def multiply(a, b):
    return a * b

print(multiply(2, 3))
print(multiply(4, 5))

# 6. 조건문이 있는 함수

def is_adult(age):
    if age >= 20:
        return True
    else:
        return False

print(is_adult(21))
print(is_adult(18))

# 7. 리스트를 받는 함수

def total(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

print(total([1, 2, 3, 4, 5]))

# 8. 함수 안에서 리스트 만들기

def make_even_numbers(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result

print(make_even_numbers([1, 2, 3, 4, 5, 6]))

# 9. 딕셔너리를 받는 함수

def print_student(student):
    print(student["name"], student["age"])

student = {
    "name": "민재",
    "age": 21
}

print_student(student)

# 10. 함수 안에서 함수 호출하기

def calculate_area(width, height):
    return width * height

def show_area(width, height):
    area = calculate_area(width, height)
    print("넓이는", area, "입니다.")

show_area(3, 4)