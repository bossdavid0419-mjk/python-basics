# 내가 작성한 코드
minute = input("분을 입력하세요: ")  # min은 파이썬에서 예약어이므로 변수명으로 사용하지 않는 것이 좋습니다. 그냥 minute로 바꾸는 것이 좋습니다.
second = input("초를 입력하세요: ")  # sec는 파이썬에서 예약어는 아니지만 변수명으로 사용하지 않는 것이 좋습니다. 그냥 second로 바꾸는 것이 좋습니다.

print("총 " + str(int(minute) * 60 + int(second)) + " 초입니다.")

# 선생님이 작성한 코드
# min = input("분을 입력하세요: ")
# sec = input("초를 입력하세요: ")

# total = int(min) * 60 + int(sec)

# print("총 " + str(total) + "초입니다.")

# 선생님이 작성한 코드 (f-string 사용)
# min = input("분을 입력하세요: ")
# sec = input("초를 입력하세요: ")

# total = int(min) * 60 + int(sec)

# print(f"총 {total}초입니다.")