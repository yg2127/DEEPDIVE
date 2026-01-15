# 딕셔너리 (가장 많이 사용된다고 함)
# JSON도 딕셔너리 형태
# 딕셔너리 자료형은 순서가 없음, 키 중복 허용하지 않음(사전에 단어가 두개가 있지는 않잖아), 수정 가능, 삭제 가능

# 선언
a = {'name' : 'Kim', 1 : '01041846662', 'birth' : '010101', 'how many' : 10}

c = {'arr' : [1,2,3,4]}
d = {
    'name' : 'yugeon',
    'age' : 26,
    'City' : 'Seoul',
    'git' : 'yg2127'
}

f = dict( # 이렇게도 선언할 수 있다
    Name = 'niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)

student = [d, f] # 이런식으로 한명의 데이터를 딕셔너리로 저장하고 이 딕셔너리를 배열로 저장한다 와우! 

print(f'a`s type is {type(a)}')
print(f'f`s type is {type(f)}')

# 출력
print(f'a`s name = {a['name']}')
print(f'a`s name = {a.get('name1')}') # get 함수를 통해서 'name' 키의 value(kim) 을 가져올 수 있다

# 그런데 get 함수로 없는 키 (예를들어 'address')를 호출할 경우?? 함수의 반환값은 'None'을 반환한다. 코드 에러가 일어나지 않음!!!

# 딕셔너리 추가

a['address'] = '광진구'
print(a)

a['rank'] = [1,2,3]
print(a['rank'][1])

print(len(a)) # 키가 몇 개인지 알 수 있음

# dict_key, dict_value, dict_items : 반복문에서 사용가능

print(a.keys()) # a의 키값들만 출력
print(c.keys())

print(list(a.keys())) # a의 키값들이 배열이 되어서 출력된다!

print(list(a.values())) # a의 value들만 출력

print(f.items()) # 키와 벨류들을 튜플 값들로 출력해준다.

print(f.pop('Status')) # Status 키와 벨류를 제거하고 value를 출력하거나 선언할 수 있게 해준다
print(f)
print(f.popitem()) # 무작위 아이템을 하나 제거한다.

print('birth' in a) # a 키중에 'birth'가 있는지 검사하고 boolin 형태로 출력해준다
a['test'] = 'test in dict'

a['address'] = 'cheonan' # 수정

a.update(birth='001228') # 딕셔너리 수정하는 메소드

print(a)