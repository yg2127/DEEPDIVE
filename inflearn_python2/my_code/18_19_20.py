# 객체 -> 파이썬의 데이터를 추상화

# 모든 객체 -> id, type으로 확인가능 -> value. != => >= <=
# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)
# 근데 이렇게 쓰면 뭐가 뭔지 어케아는데 이따가 모델링을 할 때 명시를 해줘야해

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

print(l_leng1)

from collections import namedtuple
# 네임드 튜플 사용 튜플인데 딕셔너리의 성질을 갖고있음

Point = namedtuple('Point', 'X Y')

#뭔가 클래스 포인트 하는거랑 비슷한거같은데? 그러면 메서드들 전부 다 할 수 있나?
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3)
print(pt4)
print(pt3.X, pt4.X) # 이렇게 키로도 접근 가능

l_leng2 = sqrt((pt3.X - pt4.X) ** 2 + (pt3.Y - pt4.Y) ** 2)
print(l_leng2)

# 네임드 튜플 선언 방법

Point1 = namedtuple('Point', ['x', 'y']) # 첫 번째 방법 리스트로 선언
Point2 = namedtuple('Point', 'x, y') # 두 번째 방법 컴마로 구분
Point3 = namedtuple('Point', 'x y') # 세 번째 방법 띄어쓰기로 선언가능
Point4 = namedtuple('Point','x y z class', rename = True) # default = False 이다 # 네임드튜플에 사용되는 이름이 예약어인경우 rename을
# 켜줘서 난수 형태의 변수로 출력된다. p4 출력을 보면 class 이름은 _3으로 되어있다.

print(Point4)

# 출력
print(Point1, Point2, Point3, Point4)

# Dict 2 unpacking
temp_dict = {'x' : 75, 'y' : 55}

p1 = Point1(x = 10, y = 35)
p2 = Point2(20, 40)
p3 = Point3(45, y = 20)
p4 = Point4(10, 20, 30, 40)
p5 = Point1(**temp_dict) #딕셔너리를 언패킹한 후에 네임드튜플에 입력해주면 자동으로 입력된다.

print('-' * 15)
print(p1)
print(p2)
print(p3)
print(p4) # rename 테스트

print(p1[0] + p2[0])
print(p1.x + p2.x)
x, y = p3 # 언패킹
print(x, y)

# 네임드 튜플 메소드

tmp = [52, 38]

p4 = Point1._make(tmp) # 리스트를 네임드튜플로 변환하는 메소드 = _make

print(p4)

# _fields : 필드 네임 확인
print(p1._fields, p2._fields, p4._fields)

#_asdict : 정렬된 딕셔너리를 반환

print(p1._asdict(), p2._asdict())


# 실 사용 실습
# 반 20명, 4개의 반(A, B, C, D)

classes = namedtuple('classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)] # 1 ~ 20 까지의 str 숫자배열
ranks = 'A B C D'.split()

print(numbers, ranks)

# List Comprehension

students = [classes(rank, number) for rank in ranks for number in numbers]

print(len(students))
print(students)

# 추천

students2 = [classes(rank, number)
             for rank in 'A B C D'.split()
             for number in [str(n) for n in range(1, 21)]]

print(len(students2))

for s in students2:
    print(s)