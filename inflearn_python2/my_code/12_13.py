# 클래스 메소드 심화3

class car(object):
    """
    Car class
    Author : Yu
    Date : 2026.01.22
    Description : Class, Static, Instance Method
    """
    # 클래스 변수 : 모든 인스턴스가 공통적으로 갖고있는 속성
    car_count = 0
    price_per_raise = 1.0
    
    def __init__(self, company, details): # init 블록 내부가 바로 네임스페이스
        self.company = company
        self.details = details
        car.car_count += 1
    
    def __str__(self): # 프린트문으로 문자열을 출력하는 사용자 입장에선 __str__을 하고
        return f'str : {self.company} - {self.details}'
    
    def __repr__(self): # 얘는 개발자 레벨에서 객체값을 엄격하게 규정하여 반환할 때에 사용한다.
        return f'repr : {self.company} - {self.details}'
    
    # 지금까지 사용한게 instance method
    # self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print(f'Current id : {id(self)}')
        print(f"Car Detail Info : {self.company} {self.details.get('price')}")
    def get_price(self):
        return f"Before Car Price -> company : {self.company}, price : {self.details.get('price') * car.price_per_raise}"
    def __del__(self):
        car.car_count -=1
    #Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        print(f'Success! Price increase {per}!')
    #클래스 메소드를 사용해서 여러가지 함수 실행을 할 수 있다!
    #Static method = 아무것도 받지 않는 메소드, 유연함
    @staticmethod
    def is_bmw(inst):
        if inst.company == "BMW":
            return f'This car is BMW!!'
        else: return f"This car is not BMW... it's {inst.company}.."

car1 = car('Ferrari', {'color' : 'White', 'horsepower' : 680, 'price' : 700000000})
car2 = car('BMW', {'color' : 'Black', 'horsepower' : 450, 'price' : 120000000})
car3 = car('Audi', {'color' : 'Silver', 'horsepower' : 300, 'price' : 60000000})

car2.detail_info()

#가격 접근
print(car2.details.get('price'))
# 직접 자기 인스턴스에 접근하는건 별로 좋지 않음!! 
print(car2.details['price'])

print(car1.get_price())
print(car2.get_price())

car.price_per_raise = 1.2 # 클래스 변수 변화함

print(car1.get_price())
print(car2.get_price())

car.raise_price(1.6)

print(car1.get_price())
print(car2.get_price())

#static mathod
print(car.is_bmw(car1))
print(car.is_bmw(car2))
print(car.is_bmw(car3))
