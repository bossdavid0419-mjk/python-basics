text = input("문장을 입력하세요: ")

print(len(text))

## 여기서 공백을 제외한 글자수를 세고 싶으면 문자열의 공백을 없애는 replace() 함수를 먼저 쓰고 그 결과를 len() 함수에 넣으면 된다.
print(len(text.replace(" ", "")))