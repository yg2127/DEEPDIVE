# 기본 선언
n = 700

print(n) 

print(type(n))

#동시선언
x = y = z = 200

print(x+y+z)

var = 700
#재 선언
var = "Change Value"

print(var)
print(type(var))

#object reference

# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

#예1)

print(300)
print(int(300))

n = 777

m = n

# m -> 777 <- n

print(m, n)
print(type(m), type(n))

#id, identity 확인

m = 800
n = 600

print(id(m))
print(id(n))
print(id(m)==id(n))

m = 800
n = 800

print(id(m))
print(id(n))
print(id(m)==id(n))

#파이썬 인터프리터는 효율성을 위해서 위와같이 