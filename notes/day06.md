# Day 6: 딕셔너리 심화

## 학습 목표

- 딕셔너리 안에 리스트 넣기
- 리스트 안에 딕셔너리 넣기
- 중첩된 자료 구조에서 값 꺼내기
- for문과 if문을 함께 사용하기
- 딕셔너리 값 수정 및 추가하기
- .get()으로 안전하게 값 꺼내기

## 핵심 개념

### 딕셔너리 안에 리스트

```python
student = {
    "name": "민재",
    "age": 21,
    "subjects": ["Python", "Math", "English"]
}
```

- 딕셔너리 값으로 리스트를 넣을 수 있음
- `student["subjects"]`로 리스트 전체를 꺼냄
- `student["subjects"][1]`로 두 번째 과목을 꺼냄

### 리스트에 값 추가

```python
student["subjects"].append("History")
```

- `.append()`는 리스트 끝에 새 값을 추가함

### 리스트 안에 딕셔너리

```python
friends = [
    {"name": "철수", "age": 20},
    {"name": "영희", "age": 22},
    {"name": "민수", "age": 19}
]
```

- 리스트 안에 여러 딕셔너리를 넣을 수 있음
- `friends[1]["name"]`처럼 접근함

### for문으로 반복하기

```python
for friend in friends:
    print(friend["name"], friend["age"])
```

- 리스트 안의 딕셔너리를 하나씩 꺼내서 처리함

### 조건문과 함께 사용

```python
for friend in friends:
    if friend["age"] >= 21:
        print(friend["name"], friend["age"])
```

- 조건에 맞는 데이터만 골라낼 수 있음

### 딕셔너리 값 수정과 추가

```python
student["age"] = 22
student["school"] = "대학교"
```

- 기존 키에 값을 넣으면 수정
- 새 키에 값을 넣으면 추가

### get() 사용법

```python
phone = student.get("phone", "전화번호 없음")
```

- 키가 없어도 오류 대신 기본값을 반환함

## 오늘 푼 문제

1. 딕셔너리에서 이름, 과목 리스트, 두 번째 과목 출력
2. 딕셔너리 안의 리스트에 새 과목 추가
3. 리스트 안의 딕셔너리에서 특정 값 출력
4. for문으로 모든 친구 정보 출력
5. 조건문으로 나이 21세 이상인 친구만 출력

## 느낀 점

- 딕셔너리와 리스트를 조합하면 더 현실적인 데이터 구조를 만들 수 있음
- `리스트[번호]["키"]` 패턴이 중요함
- for문과 if문을 함께 쓰면 원하는 데이터만 쉽게 골라낼 수 있음
- get()은 키가 없을 때 오류를 피하는 데 유용함