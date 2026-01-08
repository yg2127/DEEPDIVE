print("안녕하세요")
print('python start')
print("""파이썬 시작""")
print('''큰따옴표 작은따옴표 다 상관없음''')

print('p', 'y', 't', 'h', 'o', 'n', sep='-')

#sep 옵션은 컴마 , 사이에 추가 삽입되는 값들

print('010', '4184','6662', sep='-')

#end 옵션은 마지막 출력을 수정해주는것, 개행문자 제거할 때 end = '' 하면 print에 포함된 엔터입력 제거됨

print('hello my name is', end = ' ')
print ('yu geon')

#file 옵션은 나중에 파일 쓰기할 때 배워라 아무튼 print에서 파일 옵션을 지정할 수 있음

#format 사용 (d, s, f)

# d = digit, f = float, s = string

print('%s %s' %('one', 'two'))
print('{} {} {}'.format('one', 'two', 1))
print('{1} {0}'.format('one', 'two'))

# {} 안에 format 함수의 인자의 인덱스 지정을 해줘서 1, 0번째 순서인 two, one가 출력되는 것이다

# %s

print('%10s' %('nice')) #10자리 확보하고 남는 자리수는 왼쪽에 공백 ' ' 으로 처리
print('{:>10}'.format('nice'))

print('{:10}'.format('nice')) #반대쪽에서 공백 확보

print('{:$>10}'.format('nice')) # 공백이 아니고 다른 문자로도 채워놓을 수 있음. 이 코드는 달러표시 $를 넣음
print('{:^10}'.format('nice')) # 왼쪽, 오른쪽에 공백을 확보하는것 뿐만 아니라 중앙정렬도 할 수 있음

print('%.5s' %('python stㅕdy')) # 출력 문자 자리수 확보 뿐만 아니라 자리수 제한도 걸어놓을 수 있음. 5자리로 제한한다는 의미


# %d
print("%d %d" %(1, 2))
print("{} {}" .format(1234, 5678))

print('%04d' %(1234567890))
print("{:>4d}". format(23456789))

# %f

print('%1.7f' %(3.141592432432543254325)) # 정수자리 -> 1, 실수자리 -> 7
print('%06.4f' %(3.14159287695673)) #06 = 모든 자리가 6자리이고 그 중 소수점이 4자리


# f-string 꼭 배워라 개편하다 ㄹㅇ
n = "LEE"
s = 12345678
x = 10
y = 1 
ex3 = f'n = {n}, s = {s}, sum={x+y}'
print(ex3)

print(f'x+y = {x+y}, s = continuous number until 8 = {s}, x = {x}, y = {y}')