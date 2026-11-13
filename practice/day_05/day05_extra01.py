scores = {
    "python": 95,
    "math": 82,
    "english": 76,
    "science": 91
}

total = 0

for score in scores.values(): 
    total += score # 점수 합산 방법

average = total / len(scores)

print(f"총점: {total}")
print(f"평균: {average}")