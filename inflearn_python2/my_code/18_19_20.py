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

Point1 = namedtuple('Point', ['x', 'y'])