sec = int(input('총 초를 입력하세요:'))

print(f"{sec // 3600}시간 {sec // 60 % 60}분 {sec % 60}초")