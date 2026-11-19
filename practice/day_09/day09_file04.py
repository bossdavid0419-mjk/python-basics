memo = input("오늘의 메모를 입력하세요: ").strip()

if not memo:
    print("메모를 입력해주세요.")
else:
    with open("diary.txt", "w", encoding="utf-8") as file:
        file.write(memo + "\n")

    with open("diary.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)