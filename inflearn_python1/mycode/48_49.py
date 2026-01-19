#파이썬 외장함수
# 종류 : sys, pickle, shutil, temfile, time, random 등

# 예제1

import sys
#print(sys.argv)

# 예제2 (강제 종료)

# sys.exit()

# 예제3 (파이썬 패키지 위치)

#print(sys.path)
#append 해서 패키지 추가 가능

# pickle : 객체 파일 쓰기
# 파이썬에서 데이터타입을 파일에 직접 쓸 수 있다! 이건 나중에 써라
import pickle

# 예제4 (쓰기)

f = open("Test.obj", 'wb')
obj = {1 : 'python', 2: 'Study', 3:'basic'}
pickle.dump(obj, f)
f.close()
#위와 같이 사용한 리소스는 반환해야 함

# 예제5 (읽기)

f = open('Test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close

# os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
# mkdir, rmdir(비어 있으면 삭제), rename

import os
print(os.environ)
print(os.environ["USER"])

print(os.getcwd())

# time : 시간 관련 처리
import time

# 예제 8번
print(time.time())

# 예제9 (형태 변환)
print(time.localtime(time.time()))

# 예제10

print(time.ctime())

#예제 11
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

#예제 12

for i in range(5):
    print(i)
    # time.sleep(1) # 1초간 기다려라!
    
import random
print(random.random()) # 0~1 실수

print(random.randint(1,45))

print(random.randrange(1,45))

# 예제 15 (섞기)

d = [1,2,3,4,5]
random.shuffle(d)
print(d)

# 예제 16(무작위 선택)
c = random.choice(d) # iterable 한테
print(c)

#web browser : 본인 os의 웹 브라우저 실행

import webbrowser

webbrowser.open("https://www.naver.com/")
webbrowser.open_new("https://www.naver.com/")
