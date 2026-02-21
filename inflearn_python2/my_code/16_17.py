import math

# 난이도 있는, 필드에서 구현해볼법한 실습

# 클래스 예제2
# vector: (x, y) (5, 2) 
# Max((5,10)) = 10

class Vector(object):
    
    def __init__(self, *arg): # 패킹인자
        '''
        Create a vector, example : v = Vector(5, 10)
        '''
        if len(arg) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = arg # 언패킹
            
    def __repr__(self):           
        '''
        Return the Vector information
        '''
        return f'Vector({self._x}, {self._y})'
    
    def __add__(self, other):
        '''
        Return the vector addition of self and other
        '''
        return Vector(self._x + other._x, self._y + other._y)
    def __mul__(self, y):
        '''
        Multiply vector by input y as scalar
        '''
        return Vector(self._x * y, self._y * y)
    def __bool__(self):
        '''
        vec = (0, 0) 이면 False를 출력하고 아니라면 True를 출력한다.
        '''
        return bool(abs(max(self._x, self._y)))

    def __mag__(self):
        '''
        Return the size of the vector
        '''
        return math.sqrt(self._x ** 2 + self._y ** 2)

print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)
print(Vector.__bool__.__doc__)

v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector(3, 4)
v4 = Vector()

print(v1, v2, v3, v4)

print(v1 + v2)

print(v1 * 3)
print (v2 * 10)

v5 = Vector(*map(int, input().split(' '))) # map은 여러개의 객체를 반환하기 때문에 packing해줘서 iterable한 객체로 변환 후 넘겨줘야 Vector에서 unpacking 후 객체 지정한다.
print(f"input's magnitude (norm of the Vector) is {v5.__mag__()}")

print(bool(v1), bool(v4))