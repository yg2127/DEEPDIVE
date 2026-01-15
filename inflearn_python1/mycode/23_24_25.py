# IF 구문 실습

# 기본 형식

print(type(True)) 
# 0이 아닌수, "abc", [1,2,3], {1 : 1, 2 : 2, 3 : 3}, (1,2,3), {1,2,3} 등의 비어있지 않은 변수
print(type(False)) # 0, "", [], {}, () 0과 빈 변수들

#예를 들어서
if 'a':
    print('Good')
    
if []: # 이렇게 비어있는 변수는 False처리
    print('really?')
else:
    print('fine')

# 관계연산자 (연산결과로 True, False 나옴)

# >= <= < > == !=

x = 10
y = 11

print(x == y)

print(x !=y) 

print(x >= y)

print(x <= y)

city = ""

if city:
    print(f'you are in {city}')
    
else:
    print(f'please enter your city')
    
city2 = "seoul"

if city2:
    print(f'your city is {city2}')
    
# 논리연산자 (중요)

# and, or, not, xor 등등

a = 10
b = 20
c = 30

print(f'a < b < c? {a < b and b < c}')

print(f'a < b || b > c?? {a < b or b > c}')

print(not 1)
print(not "")

# 산술, 관계, 논리 우선순위

print(f'3+12 >7+3? {3+12 > 7+3}')
# 산술연산(+-*/)이 가장 먼저 계산하고
# 그다음 관계연산자(> < <= >= != ==)를 계산하고
# 마지막으로 논리연산자 (and or xand xor) 을 계산한다.

print(5 + 10 > 0 and not 7+3==10)
# true and not true = true and false = false

# 복수의 조건이 모두 참일 때 실행

s1 = 90
s2 = 'A+'
if s1 >= 80 and s2 == 'A+':
    print(f'well done! your score is {s1} \n 축하드립니다!')
    

# 연쇄조건문
num = 90

if num >= 90:
    print('Grage : A')
elif num >= 80:
    print('Grade B')
elif num >= 70:
    print('grade C')
    
else:
    print('Grade F')

# 중첩 조건문
grade = 'A'
total = 95

if grade == 'A':
    if total >= 90: print('장학금 100%')
    elif total >= 80 : print('장학금 80%')
else : print('no scolarship')

# in, not in

q = [10, 20, 30]
w = {7, 8, 9, 10}
e = {"name" : "Lee", "City" : 'seoul' , "grade" : "A"}
r = (10, 100, 1000)


print(10 in q)
print("LEE" not in e.values())
print("grade" in e)
print(1000 in r)