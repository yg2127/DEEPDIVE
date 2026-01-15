# 모듈 사용 실습

import sys

# 지금까지 사용한 함수들과 math, sys, time같은건 어디서 갖고온거임?

print(sys.path) #여기에 있는 path들에서부터 갖고 온다!

# 그럼 내가 사용하고 싶은 함수의 path를 어케 등록함? 40_41.py를 아예 다른 곳에 옮기면 어케 등록해?

print(type(sys.path)) # 리스트 변수네? append, pop, insert, index 으로 수정, 추가할 수 있겠네!

# # 모듈 경로 삽입
# sys.path.append('/Users/yugeon/Desktop/test_module') # 이 코드실행중에만 경로상에 추가가 된다. 

# print(sys.path) # 경로 추가되었는지 확인

# import test1

# print(test1.power(3,3)) # 이렇게 호출을 해서 test1.py 파일의 power 함수를 사용할 수 있다

# 그런데 출력문을 보면 test1 파일에 적혀있던 모든 print 문이 전부 다 출력된다.
# 따라서 외부에서 import해서 파일 실행하는것과 py 파일을 직접 실행할 경우를 구분하기 위한 예약어가 존재한다.

# main

import t40_41 # 아 ㅅㅂ 임포트할때 파일 이름이 숫자면 안된다.

print(t40_41.power(3,4)) # 이제 저 파일에서 print문이 __main__ 안에 있어서!

