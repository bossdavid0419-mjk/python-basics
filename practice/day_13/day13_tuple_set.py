# 튜플
point = (3,5)
print(point[0])     # 3 ➡️ 꺼내는 건 리스트와 같음

point[0] = 10       # TypeError ➡️ 바꿀 수 없음

x,y = point     # 하나씩 나눠 담기 (언패킹)
print(x,y)      # 3  5

# 세트
tags = {"공부", "운동", "공부"}
print(tags)         #{'공부', '운동'} ➡️ 중복이 자동으로 사라짐 (순서는 바뀔 수 없음)

tags.add("독서")        # 추가
print("운동" in tags)   # True

names = ["민재", "영희", "민재", "철수"]
unique = set(names)     # 리스트 ➡️ 세트로 바꾸면 중복 제거
print(len(unique))      # 3