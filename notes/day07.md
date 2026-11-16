# Day 7: 함수

## 학습 목표

- 함수 정의와 호출 방법 이해
- 매개변수와 반환값 사용
- 조건문과 반복문을 함수 안에서 사용
- 리스트와 딕셔너리를 함수로 처리
- 함수 안에서 다른 함수 호출하기
- 실전형 문제 풀이

## 핵심 개념

### 함수란?

함수는 자주 쓰는 코드를 이름을 붙여 저장하고, 필요할 때마다 다시 실행하는 도구입니다.

```python
def say_hello():
    print("안녕하세요!")

say_hello()
```

- `def`는 함수를 정의
- `say_hello`는 함수 이름
- `()`는 함수 호출
- 함수 안의 코드는 호출될 때 실행됨

### 매개변수

```python
def greet(name):
    print("안녕하세요,", name, "님!")

greet("민재")
```

- `name`은 매개변수
- 함수 호출 시 값을 넣어줌
- 함수 안에서 그 값을 사용함

### return

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```

- `return`은 함수의 결과를 돌려줌
- `print()`는 화면에 보여주는 것
- `return`은 값을 돌려주는 것
- 함수 밖에서 결과를 저장하거나 출력할 수 있음

### 조건문이 있는 함수

```python
def is_adult(age):
    if age >= 20:
        return True
    else:
        return False
```

- 조건에 따라 다른 값을 반환
- `True`와 `False`를 활용

### 리스트를 받는 함수

```python
def total(numbers):
    result = 0
    for number in numbers:
        result += number
    return result
```

- 리스트를 매개변수로 받음
- 반복문으로 합계 계산
- 결과 반환

### 짝수만 골라내기

```python
def make_even_numbers(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result
```

- 빈 리스트 생성
- 조건에 맞는 값만 추가
- 새 리스트 반환

### 딕셔너리를 받는 함수

```python
def print_student(student):
    print(student["name"], student["age"])
```

- 딕셔너리를 매개변수로 받음
- 키로 값 접근
- 출력 가능

### 함수 안에서 함수 호출

```python
def calculate_area(width, height):
    return width * height

def show_area(width, height):
    area = calculate_area(width, height)
    print("넓이는", area, "입니다.")
```

- 함수 안에서 다른 함수 호출 가능
- 코드 재사용성 향상

## 오늘 푼 문제

1. 두 수를 받아 합을 반환하는 함수
2. 이름을 받아 인사 문장을 반환하는 함수
3. 숫자 리스트 평균 계산 함수
4. 짝수만 골라 새 리스트로 반환하는 함수
5. 상품 가격과 할인율로 최종 가격 계산 함수

## 느낀 점

- 함수는 코드 재사용에 매우 유용함
- `return`과 `print()`의 차이를 이해함
- 함수 안의 코드는 호출될 때 실행됨
- 리스트와 딕셔너리를 함수로 처리하는 방법을 익힘
- 실전형 문제에서 조건문과 반복문을 함께 사용하는 감각을 익힘