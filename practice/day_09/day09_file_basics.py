with open("memo.txt", "w", encoding="utf-8") as file:
    file.write("오늘 Python 파일 다루기를 배웠다.\n")
    file.write("파일에 내용을 쓰고 읽는 방법을 연습했다.\n")

with open("memo.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)