# 모듈을 모아놓은 폴더를 패키지라고 생각하면 된다.

# 패키지 작성 및 사용법 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
#상대경로 : .. (부모 디랙토리), . (현재 디랙토리) -> 모듈 내부에서만 사용

# sub 패키지 분석 ㄱㄱ inflearn_python1/source_code/sub 에 있음

import sys

# 위의 파일경로는 현재 42_43 파일의 위치와 다르니까 sys.path.append 를 수행해줘야 함
sys.path.append('/Users/yugeon/DEEPDIVE/inflearn_python1/source_code/sub') # 절대 경로를 써야함
print(sys.path)
# 만약 부모폴더가 같으면 sys.path.append 할 필요 없음
# 예제1

import sub1.module1
# 지금 나는 source_code/sub 의 절대경로를 path에 추가했다. 이러면 sub의 하위 폴더들을 import 할 수 있다.
# 현재 파일의 부모 폴더가 sys.path에 등록되기 때문에 현재 파일의 부모폴더의 하위항목들에 대해 import 할 수 있다.

import sub2.module2
print('_' * 15)
# 사용
sub1.module1.mod1_test1() # 출력 2번
sub1.module1.mod1_test2()
print('_' * 15)
sub2.module2.mod2_test1()
sub2.module2.mod2_test2()

print('\n\n\n')

# 예제2

# sys.path 에 등록된 경로가 모듈에 비해 너무 상위의 부모패키지 일 때

from sub1 import module1
from sub2 import module2 as m2 # as ~~ 는 별칭

module1.mod1_test1()
module1.mod1_test2()

print('-' *15)

m2.mod2_test1()
m2.mod2_test2()

print('\n'*3)

from sub1 import * # <- 이거는 sub1의 모든 모듈을 갖고 온다.
from sub2 import * # 이거는 남발하면 파이썬 파일 실행할 때 메모리를 잡아먹을 수 있다.

module1.mod1_test1()
module1.mod1_test2()
print('-'*15)

module2.mod2_test1()
module2.mod2_test2()

# __init__.py는??
# pycache는 지워버려

# __init__.py는 python3.3부터는 없어도 패키지로 인식함 a-> 단 하위호환을 위해 작성을 추천
# 파일 경로에 따라 패키지로써 인식을 하고 import를 하기 위해선 __init__.py를 했어야 import 가능했음
# 최신 버젼은 init 파일 없어도 됨 근데 3.3 이하버젼의 파이썬 개발을 위해서

#init 파일 안의 __all__ [~] 이 내용들은 외부에서 import를 할 수 있도록 허가해주는 리스트임
