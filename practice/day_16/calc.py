def add(a, b):
    return a + b

def average(numbers):
    return sum(numbers) / len(numbers)

def main():
    print("calc 테스트:", add(1,1), average([2,4]))

if __name__ == "__main__":
    main()
print(f"calc.py의 __name__: {__name__}")