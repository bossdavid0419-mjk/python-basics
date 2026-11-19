with open("goals.txt", "w", encoding="utf-8") as file:
    file.write("Python을 꾸준히 공부하기\n")
    file.write("운동 습관 만들기\n")
    file.write("영어 공부하기\n")

with open("goals.txt", "a", encoding="utf-8") as file:
    file.write("하루 30분 운동하기\n")

with open("goals.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(f"목표: {line.strip()}")