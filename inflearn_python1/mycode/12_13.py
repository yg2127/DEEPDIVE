# 파이썬 모든 자료형, 데이터 타입 선언, 연산자 활용, 형 변환, 외부 모듈

#12강

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린 (true false)
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

str1 = "python"
bool = True
str2 = "Anaconda"
float1 = 10.0
int2 = 7
list3 = [str1, str2]
dict4 = {
    "name" : "Machine Learning",
    "version" : 2.0
}

tuple = (7,8,9)
set = {7,8,9}

# 데이터 타입 출력
print(type(str1))
print(type(str2))
print(type(bool))
print(type(float1))
print(type(list3))
print(type(int2))
print(type(dict4))
print(type(tuple))
print(type(set))

#숫자형 연산자
"""
+
-
*
/
// 목만 계산
% 나머지만 계산
abs(x) : 절대값
pow(x, y) : 제곱 x ** y
"""

# 정수 선언

i = 77
i2 = -14
big_int = 56784392067845327068543076859437605894


# 정수 출력

print(i)
print(i2)
print(big_int)

# 실수 출력

f1 = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3/9

print(f1)
print(f2)
print(f3)
print(f4)

# 연산 실습

i1 = 1000
i2 = 100
big_int1 = 4832910
big_int2 = 4563721546732146738291645782

print("+")
print(f'i1 + i2 : {i1 + i2}')
print(f'f1 + f2 : {f1+f2}')
print(f'big_int1 + big_int2 : {big_int1+big_int2}')

a = 3 + 1.0

print(f'3 + 1.0 = {a} = a and type is {type(a)}')

# 형 변환 실습

a = 3.
b = 6
c = .7
d = 12.7

print(f'{type(a)}, {type(b)}, {type(c)}, {type(d)}')

print(float(b))
print(int(c))
print(int(d))
print(int(True))
print(float(False))
print(complex(3))

print(int('3'))

print(int('123') +321) #와 이거 c언어에서 하려면 개지랄해야하는데 진짜 개똑똑하네...

#수치 연산 함수

print(abs(-7)) # 절댓값
x, y = divmod(100, 8)

print(f'x = {x}, y = {y}')

print(f'pow(5, 3) means 5 ** 3 = 5 * 5 * 5 = {5**3}')

# 외부모듈 math

import math
print(math.pi) #오 이런 모듈도 있네 ㅎㅎ