#filewrite
# 파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기모드 w, 추가 모드 a, 텍스트 모드 t, 바이너리 모드 b
# 상대 경로 ('../,./'), 절대 경로 ('/Users/yugeon/DEEPDIVE/inflearn_python1/mycode/50_51_52.py')
# 상대경로는 어떤 환경에서든 돌아갈 수 있게 하고 절대 경로는 오류 가능성이 적어진다는 이점이 있다.


# 파일 읽기
# 예제 1

f = open('/Users/yugeon/DEEPDIVE/inflearn_python1/source_code/resource/it_news.txt', 'r', encoding='UTF-8') # 인코더 기본값이 UTF-8
# 인코더가 중요함. UTF-8이나 다른거면 맞춰줘야함

# 속성 확인 (현재 파일과 연결되어있는 f에서 사용할 수 있는 method들을 확인활 수 있다.)
print(dir(f))

# 인코딩 확인
print(f.encoding)

#파일 이름
print(f.name)

#모드 확인
print(f.mode)
cts = f.read
print(cts)

f.close()

# 예제2

# with open('/Users/yugeon/DEEPDIVE/inflearn_python1/source_code/resource/it_news.txt','r') as f:
#     c = f.read()
#     print(c)
#     print(iter(c)) #iter 문을 통해서 1글자씩만 읽어오니까 for문, while문을 통해서 연속적으로 출력할 수 있겠지
#     print(list(c))
    
# print()

with open('/Users/yugeon/DEEPDIVE/inflearn_python1/source_code/resource/it_news.txt','r') as f:
    c = f.read(20)
    print(c)
    c = f.read(20) # read 함수를 사용하면 그 위치를 기억했다가 다음에 read를 사용할 때 읽었던 부분 뒤부터 읽어온다.
    print(c)
    c = f.read(20)
    print(c)
    f.seek(0,0)
    c = f.read(20)
    print(c)
    
print()

# 예제 4
# readline : 한줄 씩 읽기

with open('/Users/yugeon/DEEPDIVE/inflearn_python1/source_code/resource/it_news.txt','r') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

print()

#예제5
# readlines : 전체를 읽은 후 줄 단위를 리스트로 저장

with open('/Users/yugeon/DEEPDIVE/inflearn_python1/source_code/resource/it_news.txt','r') as f:
    cts = f.readlines()
    for c in cts:
        print(c)
        
        
# 파일 쓰기(write)

# 예제1
with open('/Users/yugeon/DEEPDIVE/inflearn_python1/source_code/resource/contents1.txt', 'w') as f:
    f.write('i love python\n')
    
#예제2
with open('/Users/yugeon/DEEPDIVE/inflearn_python1/source_code/resource/contents1.txt', 'a') as f:
    # open 함수의 인자를 'w' 를 사용할 경우 기존 텍스트 내용을 덮어쓰기 하는데 반해 'a' 를 사용할 경우 기존 텍스트 뒤에 추가한다.
    f.write('I love python2')
    
#예제3
#writelines : 리스트 -> 파일
with open('/Users/yugeon/DEEPDIVE/inflearn_python1/source_code/resource/contents2.txt', 'w') as f:
    l = ['Python\n','Torch\n','GoogleCloud\n','Linux\n','Docker\n','Transformer\n']
    f.writelines(l)
    
#예제4
with open('/Users/yugeon/DEEPDIVE/inflearn_python1/source_code/resource/contents3.txt', 'w') as f:
    print('Test the write!',file=f)
    print('Test the write!',file=f)
    print('Test the write!',file=f)
    print('Test the write!',file=f)
    