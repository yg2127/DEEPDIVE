# 리스트 ㅈㄴ 중요하다. 처음부터 끝까지 잘 알아놓도록 하자
# 슬라이싱 인덱싱 이런건 저번에 한 문자열 슬라이싱이랑 똑같다! 화이팅!!
# c언어든 파이썬이든 자료구조, 알고리즘 등에서 모두 다 쓰이니까 매우 중요

# 리스트 자료형 (순서 있고 중복 있고 수정 되고 삭제도 됨)

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, ["Ace", 'Base', 'Captain']]
e = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱 (찾아가는거)

print(f'd`s type is {type(d)}')
print(f'all c is {c[0]+c[1]+c[2]+c[3]}')
print(f'd[-1][1] is "{d[-1][1]}"')

print(f'd`s letter is {list(d[-1][1])}')

# 슬라이싱 (배열 자르기)

print(f'e[2:] : {e[2:]}')

# 리스트 연산

print(f'c+d = {c+d}') # 앞에꺼 먼저 출력하고 뒤에꺼 뒤에 붙여서 출력
print(f'c * 3 = {c*3}') # 리스트를 3번 연속해서
# print(f"'test' + c[1] = {'test'+c[1]}") # 이렇게 변수 형식이 다르면 에러가 난다! 그래서 형식을 맞춰 줘야함
print(f"'test' + c[1] = {'test'+ str(c[1])}") # 이렇게 형식을 통일시켜줘야 한다

# 값 비교

print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])

# Identity(id)

temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제

c[0] = 4
print(f'c = {c}')
c[1:2] = ['a', 'b', 'c'] # 이건 c[1] 아님? 맞음 똑같음
print(f'c = {c}')

c[1:3] = [] # 리스트 내용을 제거 (와우 중간 내용이 삭제되고 뒤의 원소들이 자돌으로 연결되네)
print(c)

del c[3]

print(c) # 이렇게 해도 된다.

# 리스트 함수

a = [5,1,2,4,3]

print(a)
a.append(10) # 맨 뒤에 원소 추가
print(f'a = {a}')

a.sort() # 정렬
print(a)

a.reverse() # 역순으로 정렬
print(f'{a}')

print(a.index(3)) # 원소 3의 인덱스를 출력해준다

a.insert(2,7) # 2번 인덱스에 원소 7 추가하고 기존에 있던 2번 이후의 배열들은 한칸씩 뒤로 미뤄준다
print(a)

print(a.index(7))

del a[6] #  이거는 인덱스 6을 지워주는거
a.remove(10) # 이거는 원소 10을 제거해주는거

print(a)

print(f'a -> {a.pop()}')
# pop은 맨 뒤의 원소를 제거하고 출력하거나 선언하게 해주는거
print(a)
# 아니 그러면 파이썬으로 알고리즘 문제 풀면 진짜 너무 쉬울거같은데? 와... 개꿀이다 진짜

b = [10,11,12,13]

a.extend(b) # 배열 두 개를 concat 해주는거

print(a)

while a:
    data = a.pop()
    print(data)
