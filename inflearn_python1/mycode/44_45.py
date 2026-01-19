# 예외 개념 및 처리
# 예외 종류와 예외 재연

#SyntaxError, TypeError, NameError, ValueError, KeyError
#문법적으로는 예외가 없지만 코드 실행 프로세스(단계발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다.
# 4. 예외 무시

# SyntaxError : 문법오류

# print('error'))
# if True
#   pass

# NameError : 참조 없음

# a = 10
# print(b)

#ZeroDivisionError : 수학적 오류
#print(100/0)

#IndexError : 리스트에서 없는 인덱스 접근
#x = [1,2,3]
#print(x[3])

# KeyError : 딕셔너리에서 없는 키 접근

#dic = {'name' : 'LEE', 'city' : 'Seoul}
# print(dic['school'])

# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장(EAFP)

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
#import time
#print(time.time2())

#ValueError : 리스트, 튜플에 없는 원소를 제거하려고 할 때
# x = [1,2,3]
#x.remove(10)

# FileNotFoundError : 없는 파일을 읽어오려고 할 때
# f = open('test.txt')

# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
#x = [1,2]
#y = (1,2)
#z = 'test'
#print(x+y), print(z+x), print(y+z) 이렇게 어떻게 바꿔야 할 지 감이 안올때
#이럴때 형변환 해야함

# 가장 중요한 예외 처리 기본
# try : 에러가 발생 할 가능성이 높은 코드 실행
# except 에러명1 : 여러개 가능
# except 에러명2 : 
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

from sys import exception # 이거 임포트 해야 try, except 사용할 수 있음


# name = ['Kim','Lee','Park']
# #예제1
# try: # 한번 시도해보고
#     z = 'Cho'
#     x = name.index(z)
#     print(f'{z} found it! {x+1} in name')
# except: # try 블록 안 코드 실행중에 에러가 나면 아래의 코드 실행
#     print(f'not found it! - Occured ValueError!')
# else:
#     print('Ok! else,') # try가 정상적으로 실행 될 때 실행됨
    
# print()

# try를 사용하면 컴파일 환경에선 절대 에러가 나지 않는다!
#예제 2번
# name = ['Kim','Lee','Park']

# try: # 한번 시도해보고
#     z = 'Cho'
#     x = name.index(z)
#     print(f'{z} found it! {x+1} in name')
# except Exception: # try 블록 안 코드 실행중에 에러가 나면 아래의 코드 실행
#     print(f'not found it! - Occured ValueError!')
# else:
#     print('Ok! else,') # try가 정상적으로 실행 될 때 실행됨
    
# print()

#예제 3번

# name = ['Kim','Lee','Park']

# try: # 한번 시도해보고
#     z = 'Cho'
#     x = name.index(z)
#     print(f'{z} found it! {x+1} in name')
# except Exception as e: # try 블록 안 코드 실행중에 에러가 나면 아래의 코드 실행
#     print(e) # 에러 내용을 출력해준다. 'Cho' is not in list 라고 뜬다
#     print(f'not found it! - Occured ValueError!')
# else:
#     print('Ok! else,') # try가 정상적으로 실행 될 때 실행됨
# finally: # 얘는 예외 발생 하건 안하건 무조건 실행, 연결리스트 노드 free 같은거 실행해줄때 사용
#     print('Ok! finally')

# print()

#예제 4번
# 예외 발생 : raise
# raise 키워드로 예외를 직접 발생시킬 수 있음

try:
    a = input()
    if a == 'Kim':
        print('OK! Pass!')
    else:
        raise ValueError # 이렇게 문법적으로나 다른 부분으로 
    #에러가 날 부분이 없어도 특정 조건에서 에러가 나게 설정할 수 있음!!!
except ValueError:
    print("Occured Exception!")
else:
    print('Ok else!')
    