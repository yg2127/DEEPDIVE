# input 사용자 입력

# 기본 타입(str)

# 예제 1번

# name = input("Enter your Name")
# grade = input("enter your grade")
# company = input("Enter your company")
# print(f'{name}, {grade}, {company}')

# 예제 2번
# number = input("Enter number : ")
# name = input("Enter name : ")

# print(f'type of number {type(number)}')
# print(f'type of name {type(name)}')
# input으로 입력받은 변수는 모두 str 형식이다.

# 예제 3 (계산)

# f1 = int(input("n1 is "))
# f2 = int(input("n2 is "))

# print(f'n1 * n2 is {f1*f2}')
#이렇게 int 형식을 씌워줘서 숫자로 인식하게 한다!

# 예제 4 float도 가능

# f1 = float(input("float n : "))

# print(f'input float is {f1} \ninput type is {type(f1)}')

# 예제 5 이렇게 출력문에서 바로 입력받고 출력도 가능하다

# print(f'First Name - {input("enter your first name : ")}, Last Name - {input("enter your last name : ")}')

# 예외처리는 어떻게 하는지?

# n = int(input("enter the number : ")) #이거 실행할 때 문자를 입력하면?? 에러가 난다.

# 그래서 try, except 를 사용한다.

# try:
#     n = int(input("enter the number"))
#     print(f'your n is {n}')
# except ValueError:
#     print(f'This is not a number') 
    
# 올바른 값이 나올 때까지 계속 입력받는 방법 (이거 많이 나온다)

while True:
    try:
        n = int(input("enter your n : "))
        break
    except ValueError:
        print("this is not a number")
print(f'{n} is your number')