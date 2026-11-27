import calc
from calc import average

print(calc.add(3, 5))            # 8 → 'import 모듈' 방식: 모듈이름.함수()로 부름
print(average([10, 20, 30]))     # 20.0 → 'from 모듈 import 함수' 방식: 함수 이름만으로 부름
print(calc.average([1, 2]))      # 1.5 → 두 방식을 같이 써도 되는지
print(f"app.py의 __name__: {__name__}")