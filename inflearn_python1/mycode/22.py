# 집합
# numpy, scipy 이런거에서 잘 쓰인다.
# 순서가 없다, 중복을 허용하지 않고 수정하거나 삭제는 할 수 있다.

# 선언
a = set()

print(a) 

b = set([1,2,3,4, 4,4,4])
c = set([1,2, 'study','python', 'deeplearning'])
e = {1, 2, 3, ('f','i','x'), False,'~dict','set'} # 딕셔너리에서 키를 지정 안해주면 set이 된다.

print(a)
print(b)
print(c)
print(e)

# set에서 튜플, 리스트 등으로 변환 가능 바꾸면 슬라이싱 활용 가능!

t = tuple(b)
print(t)

l = list(c)
print(l)

# 길이 탐색 가능
print(len(a), len(b), len(c), len(e))

# 집합 자료형 활용

s1 = {1,3,4,5,6,7,9}
s2 = {2,4,6,8}

print(f's1 & s2 = {s1&s2}')
print(f's1 & s2 = {s1.intersection(s2)}') # 교집합

print(f's1 | s2 = {s1|s2}')
print(f'st|s2 = {s1.union(s2)}') # 합집합

print(f's1-s2 = {s1 - s2}')
print(f's1-s2 = {s1.difference(s2)}') # 차집합

#중복 원소 확인
print(f's1 & s2 is {s1.isdisjoint(s2)}') # 중복 원소 여부에 따라 T/F boolin 출력

#부분 집합 확인

print(f's1`s subset is {s1.issubset(s2)}') # 부분 집합 여부테 따라 T/F boolin 출력

# 추가 & 제거

s1 = {1,2,3,4}

s1.add(5) # 추가!
print(s1)

s1.remove(2) # 제거. 그러나 없는 원소 제거는 안됨 에러가 발생함

s1.discard(7) # 이것도 제거이나 없는 원소를 제거하면 에러가 안남 그냥 넘어감

print(s1)

s1.clear() # 모든 원소 제거
# clear는 list에서도 작동한다. 알아놓고 써먹자
print(s1)