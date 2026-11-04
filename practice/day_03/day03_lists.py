# colors = ["red", "green", "blue"]
# scores = [95, 82, 76, 91]

# # print(colors[2])  # Output: blue
# # print(colors[0])  # Output: red
# # print(colors(-1))  # Output: blue
# # print(colors[-2])  # Output: green

# # print(len(colors))  # Output: 3
# # colors.append("yellow")  # Add "yellow" to the end of the list
# # print(colors)  # Output: ['red', 'green', 'blue', 'yellow']

# # colors.remove("red")  # Remove "red" from the list
# # print(colors)  # Output: ['green', 'blue', 'yellow']

# # colors[0] = "purple"  # Relplaces "green" with "purple"
# # print(colors)  # Output: ['purple', 'blue', 'yellow']
# # print(colors)  # Output: ['purple', 'blue', 'yellow']



# for score in scores:
#     print(score)  # Output: 95, 82, 76, 91 (each on a new line)

# 리스트 만들기
tasks = ["Python 공부", "운동", "독서"]

# 전체 리스트 출력
print(tasks)  # Output: ['Python 공부', '운동', '독서']

# 첫 번째 항목과 마지막 항목 출력
print(tasks[0])  # Output: Python 공부
print(tasks[-1])  # Output: 독서

# 두번재 항목 수정
tasks[1] = "산책"
print(tasks)  # Output: ['Python 공부', '산책', '독서']

# 마지막에 새 항목 추가
tasks.append("GitHub 기록")
print(tasks)  # Output: ['Python 공부', '산책', '독서', 'GitHub 기록']

# 항목 개수 확인
print(f"할 일 개수: {len(tasks)}")  # Output: 할 일 개수: 4

# 앞의 두 항목 가져오기
print(tasks[0:2])  # Output: ['Python 공부', '산책']
