# 모듈

import math
from operator import mul



# 이런식으로 임포트해서 쓸 수 있는 것들을 말한다.
# 라이브러리랑 같은 내용인가?? 깃헙이나 그런곳에서 갖고 올 수 있댜!

#파이썬 모듈 : 함수, 변수, 클래스 등 파이썬 구성요소 등을 모아놓은 파일, 재사용하고 파일 갖다 쓸 수 있음

def add(x, y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def power(x,y):
    return x**y

if __name__ == '__main__': # 이걸 사용해서 import를 해도 실행되지 않게 한다.
    print('-' *10)

    print('called inner!!')

    print(add(5,5))
    print(subtract(15,5))
    print(multiply(10,10))
    print(divide(10,2))
    print(power(3,3))
    print('-' *10)

# 다른 파일에서 위 함수 4개를 사용할 수 없나...?? ㅠㅜ -> 할 수 있음!
