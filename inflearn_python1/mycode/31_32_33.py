# 함수 정의
# def f1(param):
#   code1
#   code2

def f1(w):
    print(f'hello {w}')

word = 'Good boy'

f1(word)

# 예제2

def r_f(w):
    return f'Hello {w}'

x = r_f('yugeon')

print(x)


# 다중 반환 매우 중요하다
def f2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = f2(10)

print(x,y,z)

q = f2(20) # 이런식으로 하면 튜플로 반환된다

print(type(q), q)

r = list(f2(20))

print(type(r), r) # 이렇게 리스트 선언해주면 리스트로 변환됨

# 딕셔너리 리턴

def f3(x):
    y1 = x*100
    y2 = x*1000
    y3 = x*10000
    return{'v1' : y1, 'v2' : y2, 'v3' : y3}

d = f3(11)

print(type(d), d, d.get('v2'), d.items(), d.keys())

# 중요하다
# *args, **kwargs
# *args (unpacking)

def args_f(*a): # 튜플 형식이라면 몇개를 입력받던 상관이 없이 계속 입력받을 수 있음!
    for i, v in enumerate(a):
        print(f'result : {i} {v}')
    print('------')

def args_f100(*a):
    for i, v in enumerate(a):
        print(f'result : {i, v}')
    print('------')
    
#와 시발 f-string 쓸 때 왜 {a, b} 하면 튜플형식으로 출력되는지 이제 알았네... 이것도 패킹이라서 그런거임.... 진짜 미쳤다
# 변수들이 패킹될 때 왠만하면 튜플 형식으로 병합되는구나
# 파이썬에서 콤마로 값들을 나열하면 자동으로 튜플로 패킹됨

# ex

v = 1
w = 2
x = 3

z = v,w,x

print(type(z), z)

args_f('Lee')
args_f('lee','park','kim')

# **kwargs(unpacking) 딕셔너리 형태의 변수를 입력받는데 몇개를 입력받던 상관이 없음!

def kwargs_f(**x):
    for v in x.keys():
        print(f'{v} {x[v]}')
    print('-------')
    
kwargs_f(name1 = 'Yu')
kwargs_f(name1='yu', name2='Geon', city = 'seoul')

def ex(x1, x2, *x3, **x4):
    print(x1, x2, x3, x4)
    
    
ex(10, 20, 'Lee','Kim','Park', age1=20, age2 = 30, age3=40)

# 와우.... 파이썬 함수 인자를 쓸 때 입력값이 몇개가 되던 튜플, 딕셔너리 형태의 입력은 몇 개가 되던 상관이 없네....

# 중첩함수

def n_f(num):
    def f_in_f(num):
        print(num)
    print(f'in func {num}')
    f_in_f(num+100)
    
n_f(100)

# 중첩함수를 밖에서 사용하면 사용이 안된다!

# 람다 lambda 예제
# 메모리 절약, 가독성 항상, 코드 간결
# 함수는 객체 생성 후에 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) 한 후에 메모리 초기화
# 남발 시 가독성 오히려 감소

x = 5
y = 10

def m_f(x,y):
    return x*y
a = m_f(x,y)

print(a)

b = lambda x, y : x*y

print(b)
# 둘은 출력되는 결과값이 똑같다!

lambda_mal_func = lambda x,y : x*y
print(lambda_mal_func(10,20))

def f_f(x, y, func):
    print(x*y*func(100,100))
    
f_f(10,20,lambda x,y:x*y) # 이렇게 입력을 함수로 받을 때에도 lambda를 바로 써도 된다
