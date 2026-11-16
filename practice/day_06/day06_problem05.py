friends = [
    {"name": "철수", "age": 20},
    {"name": "영희", "age": 22},
    {"name": "민수", "age": 19}
]

for friend in friends:
    if friend["age"] >= 21:
        print(friend["name"], friend["age"])
