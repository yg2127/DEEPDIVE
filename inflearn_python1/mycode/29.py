# while문, if, for, while만 제대로 알아도 입출력 제어를 깔끔하게 할 수 있다.

# while (condition):
#   statements(s)

# 예제 1번

n = 5

while n > 0:
    print(n)
    n-=1
   
s = 5 
while True:
    print(s)
    s-=1
    if s < 1: break
    
a = ['foo','bar','baz']

while a:
    print(a.pop())
    
# 와우! pop 진짜 개 야무지게 쓰이네 ㅎㅎ

# 예제3 break, continue

m = 5

while m > 0:
    m -=1
    if m == 2:
        continue
    print(m)
    
print("end")

i = 1

while i <= 10:
    print(f'i : {i}')
    if i == 6:
        break
    i += 1
    
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break

sl = ['foo','bar','baz','qux']
s = 'foo'

i = 0

while i < len(sl): # len(sl) 은 sl 리스트의 원소 개수를 말한다
    if sl[i] == s:
        print(f'{s} in sl')
        break
    i += 1
    
else: print(f'{s} is not in sl')

# if 문의 in, not in을 써서 이렇게 짧게 할 수도 있다!
if s in sl:
    print(f'{s} is in sl')
else: print(f'{s} is not in sl')

a = ['foo','bar','baz','qux']
while a:
    print(a.pop(0))
    

# a.pop(0) 은 맨 앞 원소부터 제거 & 반환!