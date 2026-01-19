# 파이썬 내장 함수
# 자주 사용하는 함수 위주로 실습
# 사용하다보면 자연스럽게 숙달
# str(), int(), tuple() 형변환 이미 학습

# 절댓값
# abs() 이런건 인터프리터가 이미 내장하고 있음

print(abs(-3))

# all : iterable 요소 검사 (참, 거짓)

print(all([1,2,3,'asdf'])) # all 안의 모든 요소들이 참이어야 참을 반환함

# any : 하나라도 true이면 true 반환
print(any([1,2,0])) # true 반환

# chr : 아스키 -> 문자, ord : 문자 -> 아스키

print(chr(67))
print(ord('C'))

#enumerate : 인덱스 + Iterable 객체 두개를 동시에 반환

for i, name in enumerate(['abc','bcd','efg']): # enumerate로 반환된 두개의 객체를 unpacking 한다
    print(i+1, name)
    
# filter 반복 가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출

def conv_pos(x): # 간단한 조건식
    return abs(x) > 2

print(list(filter(conv_pos, [1,-3,2,0,-5,6]))) # conv_pos함수가 참으로 반환하는 요소들 
# (-3, -5, 6) 을 iterable 형태로 반환하고 그 값들을 언패킹하거나 list함수로 씌워서 출력하거나 다룰 수 있다.
# lambda 식을 이용해서 바로 반환할 수도 있음

print(list(filter(lambda x : abs(x)>2, [1,-3,2,0,-5,6])))

# id : 객체의 주소값 반환

print(id(int(5)))
print(id(int(34)))

# len : 요소의 길이 반환
print(len('abcdefgh'))

print(len([1,2,3,4,5,6,7]))

# max, min : 최댓값, 최소값 반환

print(max([1,2,3]))
print(max('python study'))

print(min([1,2,3]))
print(min('python_study'))

# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
# filter는 지정한 함수 값이 true인 경우만 걸러서 반환하면 얘는 다 반환함!

def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [1,-2,3,-4,5,-6,7])))

#x,y,z = map(int, input().split(' ')) # 이거 map 함수로 개 많이 쓰는 예제 중 하나임

#print(x, y, z)

print(list(map(lambda x:abs(x), [1,-3,2,-5,-6,4,7,-11])))

# pow : 제곱값 반환
print(pow(2,10))

# range : 반복가능한 객체들 반환
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(15,0,-1)))

#round : 반올림

print(round(6.5781, 2)) # 소숫점 2자리 까지
print(round(4,6)) # 소숫점을 반올림

# sorted : iterable 객체를 정렬 후 반환
l1 = [1,6,8,23,7,89,1,23]
l2 = sorted(l1)
print(sorted(l1))
print(l2)

#sum : iterable 합 반환

print(sum([1,2,3,4,5,6,7,8,9,10]))

# type : 자료형 확인

print(type(3))
print(type({}))
print(type(()))
print(type([]))

# zip : iterable의 요소 묶어서 반환

print(list(zip([1,2,3],[4,5,6])))
#각각의 원소를 묶어서 튜플로 반환

# 이거 파이썬 웹사이트에 내장함수 문서에 함수들이
# 모두 다 있고 이 중에서 좋은 것들만 골라서 알려줌

