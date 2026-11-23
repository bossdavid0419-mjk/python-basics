# 세트로 중복 제거

tags = ["공부", "운동", "공부", "독서", "운동", "공부"]
unique = set(tags)
print(f"태그종류: {len(unique)}개")
print(f"독서 태그 있음: {"독서" in unique}")
print(f"청소 태그 있음: {"청소" in unique}")

