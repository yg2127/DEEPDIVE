# for 문 실습 코딩의 핵심임
# for in collection
#   loop body

for v1 in range(10): # 0 ~ 9
    print(f'v1 is {v1}')
    
for v2 in range(1, 11): # 1 ~ 10
    print(f'v2 is {v2}')
    
for v3 in range(1, 11, 3): # 1, 4, 7, 10
    print(f'v3 is {v3}')
    
# 1 ~ 1000 까지의 합

s = 0

for v in range(1, 1001):
    s+=v

print(s)

# for문 말고 합 사용하는법

print(f'1~1000 Sum is {sum(range(1,1001))}')

print(type(range(1,11)))

print(f'1~1000 까지 4의 배수의 합 : {sum(range(1,1001,4))}')

# Iterables : 자료형 반복
# string, List, Tuple, set, dictionary
#iterable 반환 함수 : range, reversed, enumerate, filter, map, zip

nums = ['1','2','3','4','5'] # 자료형이 문자열이여도 nums안에 대입될 수 있음!

for n in nums:
    print(f'there are {n}')
    

lotto_num = [11,19,21,28,36,37]

for n in lotto_num:
    print(f'num is {n}')
    
my_info = {
    'name' : 'yugeon',
    'age' : 33,
    'City' : 'Seoul'
}

for k in my_info:
    print(f'value is {my_info[k]}')

for v in my_info.keys():
    print(f'key is {v}')

for v in my_info.values():
    print(f'value is {v}')
    
    
name = "FineAPPlE"

for n in name:
    if n.isupper():
        print(n, end='')
    else:
        print(n.upper(), end='')\

print()

# break

nums = [1,2,3,4,5,10,15,1456,1234567,123415346123567]

for n in nums:
    if n == 15:
        print("Found 34!")
        break
    else:
        print("not found")
        
# continue

l = ["1",2,5,True,4.3, complex(4)]

for v in l:
    if type(v) is bool:
        continue
    else: 
        print(f'Current type v ({v})is {type(v)}')
        print(f'multiply by 2 = {v * 2}')

# for - else 이런 문법도 있다! 와우~

numbers = [14,3,4,7,10,24,17]

for num in numbers:
    if num == 100:
        print("found 24")
        break
else:
    print('not found')
    
# for문에서 모두 반복되었는데도 break가 안된다면 실행한다

for i in range(2,10):
    for j in range(1,10):
        print(f'{i} times {j} = {i*j}')
    print(f'next')
    
# 변환 예제

n2 = 'Aceman'

print('Reversed', reversed(n2))
print(list(reversed(n2)))
print(tuple(reversed(n2)))
for i in list(reversed(n2)): print(i,end = '')
print()
# 슬라이싱을 이용해서 역순 출력도 있다!

print(n2[::-1])