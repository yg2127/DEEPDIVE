# csv 파일 작성 데이터 사이언스 분야에서 매우 많이 사용한다고 함! 와우~~
# 컴마, 쉼표로 구분되는 record set

# csv 파일 읽기 및 쓰기
# csv : MEME - text/csv

import csv

# test1 은 컴마 (,) 로 구분되어 있고 test2 는 |(or 기호) 로 구분되어있음

# 예제1

# with open('/Users/yugeon/DEEPDIVE/inflearn_python1/source_code/resource/test1.csv', 'r') as f:
#     reader = csv.reader(f) # 기본적으로 컴마를 기준으로 구분한다.
#     next(reader) # 헤더 스킵
#     # 객체 확인
#     print(reader)
#     # 타입 확인
#     print(dir(reader)) # __iter__가 있는지 확인해서 4가지 자료형(list, tuple, dict, set) 인지 확인
#     print()
    
#     for c in reader:
#         # print(c)
#         # 타입 확인 : 리스트
#         print(' : '.join(c)) # list 2 str
    
    
# 예제 2
# with open('/Users/yugeon/DEEPDIVE/inflearn_python1/source_code/resource/test2.csv', 'r') as f:
#     reader = csv.reader(f, delimiter ='|')
    
#     for c in reader:
#         print(c)

# # 예제 3
# with open('/Users/yugeon/DEEPDIVE/inflearn_python1/source_code/resource/test2.csv', 'r') as f:
#     reader = csv.DictReader(f, delimiter = '|') # dict 형식으로 읽어오는 함수로 key 는 Header, value는 각 line의 데이터이다.
#     # 위와같이 파싱하면 각 라인마다 하나의 dict가 생성되며, key는 Header, value는 각 line의 데이터값이다.
#     print(reader)
#     print(type(reader))
#     print(dir(reader))
#     print()
    
#     for c in reader: # 모든 dict들을 순회하면서
#         for k, v in c.items(): # 개별 dict의 키와 value를 한 줄씩 출력한다.
#             print(k, v)
#         print('-' * 15)
        
# 예제 4 (쓰기)
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]

w1 = []

for i in range(7):
    w1.append([3*i+1,3*i+2,3*i+3])
print(w1==w)

with open('/Users/yugeon/DEEPDIVE/inflearn_python1/source_code/resource/write1.csv', 'w', encoding = 'UTF-8') as f:
    print(dir(csv))
    wt = csv.writer(f)
    
    # dir 확인
    # print(dir(wt))
    # 타입 확인
    # print(type(wt))
    
    for v in w:
        wt.writerow(v)
        
# 예제5 딕셔너리로 Header 사용
with open('/Users/yugeon/DEEPDIVE/inflearn_python1/source_code/resource/write1.csv', 'w', encoding = 'UTF-8') as f:
    field = ['mod1','mod2','mod3']
    wt = csv.DictWriter(f,fieldnames = field) # 헤더 지정
    wt.writeheader()
    
    for v in w1: # w1은 하나씩 읽을 때마다 하나의 list를 가져온다. 따라서 v는 한 줄을 가져온다.
        wt.writerow({'mod1':v[0], 'mod2':v[1],'mod3':v[2]})