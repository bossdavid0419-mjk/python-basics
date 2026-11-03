# 내가 작성한 코드
# sec = int(input('총 초를 입력하세요:'))

# print(f"{sec // 3600}시간 {sec // 60 % 60}분 {sec % 60}초")

# 선생님이 작성한 코드

total = int(input("총 초를 입력하세요: "))

hours = total // 3600
minutes = (total % 3600) // 60
seconds = total % 60

print(f"{hours}시간 {minutes}분 {seconds}초입니다.")