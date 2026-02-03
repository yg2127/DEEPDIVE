# pandas
# matplotlib, Seaborn 안함
# plotly를 활용한 데이터 시각화

import numpy as np
import pandas as pd
np.random.seed(0)
arr = np.random.randint(10, size = (2,2)) # 2,2 짜리 랜덤 arr 생성
print(arr)

# copy true는 원본 데이터 (여기선 arr) 수정해도 인스턴스 변경 안됨
# False는 원본 데이터가 수정될 경우 그대로 판다스 df에 반영됨
# Class pandas.DataFrame() 판다스 데이터프레임은 2차원 배열 인스턴스를 반환한다.
# 입력값으로는 
#   data(2차원 행렬값, 입력 : iterable 변수), 
#   index(행 레이블, 입력 : list, tuple 형태의 객체, 기본값은 인덱싱 0, 1, 2, 3...),
#   columns(열 레이블, 인덱스 또는 배열형태의 객체, 기본값은 인덱싱 0, 1, 2, 3...)
#   dtype(데이터 유형 설정, 기본값은 pandas가 data 보고 자동으로 추론)
#   copy(원본 데이터 data와 똑같이 수정/제거 되려면 False, 별개의 값으로 복사하려면 True)
df1 = pd.DataFrame(arr, copy = False)
df2 = pd.DataFrame(arr, copy = True)
arr[0,0] = 99
print(df1) # arr에 영향 받음
print(df2) # arr에 영향 안받음

# 예시 01 : dictionary로 pd dataframe 만들기
print('-'*5, '예시1', '-'*5)
d3 = {'A' : [1,2], 'B' : [3,4]}
df3 = pd.DataFrame(data = d3)

print(df3) # 자동으로 dict의 key 값들이 columns 로 할당되고 
# 해당 key 의 value값들이 해당 column의 열 데이터가 된다.

# 예시2 - 인덱스와 컬럼 지정
print('-'*5, '예시2', '-'*5)

d4 = np.array([[1,2],[3,4]])
i1 = ['R1','R2']
c1 = ['C1','C2']

df4 = pd.DataFrame(data=d4, index=i1, columns=c1, copy=1)
print(df4)

# pandas 메소드 add
print('-'*5, 'add', '-'*5)
# df.add() : 다른 데이터 프레임이나 Series, 스칼라 등을 data에 더하는 메소드
# 입력값들
#   other : 해당 인스턴스에 더해줄 값, 입력값 : [dataframe, Series, Scalar]
#   axis : 더해줄 Label을 설정함, 0은 행에 더해주고 1은 열에 추가해준다. ?? 몇번행이나 몇번열에 더할지 어케 알아
#   level : multiindex에서 계산할 index의 레벨 ?? 무슨 말이야
#   fill_value : Nan으로 표기될 누락 값들을 해당 값으로 대체

d = [[1,10,100],[2,20,200],[3,30,300]]
c = ['c1', 'c2','c3']
r = ['r1','r2','r3']

df5 = pd.DataFrame(data = d, columns = c, index = r)
print(df5)

re = df5.add(1)
print(f'\nadd(1) = \n{re}')

d2 = [[3],[4],[5]]

df6 = pd.DataFrame(data = d2, index = r, columns = ['c1'])
print(f'\n {df6}')

print(df5.add(df6))
# df6가 어디 열에 들어갈 줄 어떻게 알아요? -> 같은 열 이름인 column 으로 간다.
# columns 안의 열 이름을 c1, c2, c3로 바꾸면 그 위치로 간다!

# fill_value 사용시 df5에 더해질 df6의 자리가 없는 경우 nan으로 반환 되지만
# fill_value = 0으로 df6에는 없는 c2, c3열들을 0값으로 채워넣은 뒤 계산한다!
print('\nfill_value=\n', df5.add(df6, fill_value = 0))

# sub 메소드 (sub, rsub)
# df.sub() & df.rsub() 는 다른 데이터 프레임, Series, 스칼라 등 데이터에서 빼기를 해주는 메소드
# df1.sub(df2)는 df1 - df2, df1.rsub(df2)는 df2-df1로 빼는 대상이 다르다
