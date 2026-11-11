# 1부터 입력한 숫자까지 출력하기
num = int(input("마지막 숫자를 입력하세요: "))

while num <= 0:
    print("양의 정수를 입력하세요.")
    num = int(input("다시 입력하세요: "))

i = 1

while i <= num:
    print(i)
    i+=1