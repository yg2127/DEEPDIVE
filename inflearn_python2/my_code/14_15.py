#매직메소드, 스페셜 메소드
# 파이썬의 핵심 -> Sequence(반복 가능한 변수), iterator(반복), Function(함수), Class
# 클래스 안에 정의할 수 있는 특별한 (Built-in) 메소드

# 기본형
print(int) # 뭐야. int를 출력하면 클래스가 나오내?
print(float) # 이것도 클래스고?

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10

print(type(n)) # 위와같이 선언한 변수도 클래스네?? 이제 로우레벨에서 코딩 가능

print(n + 100)

# 내부적으로 스페셜 메소드 add가 실행되었음!
print(n.__add__(100)) # 따라서 이 문장은 위와 같이 n + 100이다!

print(n.__doc__)
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))

# 이런것들, 파이썬에서 만든 빌트인 메소드들을 통해서 나만의 메소드, 매직메소드를 만들 수 있다!

print('-'*15)

#클래스 예제1

class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f'Fruit Class Info : {self.name}, {self.price}'
    def __add__(self, x):
        print('called __add__')
        return self.price + x.price
    def __sub__(self, x):
        print('called >> __sub__')
        return self.price - x.price
    def __le__(self, x):
        print('called >> __le__')
        if self.price <= x.price: return True
        else: return False
    def __ge__(self, x):
        print('called >> __ge__')
        if self.price >= x.price: return True
        else: return False

# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

# 원래 매직메소드 없이 계산하려면
print(f'총 금액 = {s1.price + s2.price}')
# 그러나 매직메소드 add를 추가했으므로
print(f'매직 메소드로 계산한 총 금액 = {s1 + s2}')
# 원래 +는 int 형 데이터만 계산 가능한데 
# 매직 메소드를 통해 Fruit 클래스에서 정의한 add 메소드를 바꿀 수 있으니까
# +로 계산 가능하다!!

# 두 번째 예시로

print(s1 - s2)

# 그러면 +, -, *, / 말고 다른 함수같은 것들도 메소드로 정의되어 있는데 뭐가 뭔 메소드로 정의되어있는지 그걸 어떻게 아나??

print(s1 >= s2) # ge가 호출됨!
print(s1 <= s2) # le가 호출됨!
print(s1 - s2)
print(s2 - s1)
print(s1)
print(s2)