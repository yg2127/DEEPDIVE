lambda_mal_func = lambda x,y : x*y
print(lambda_mal_func(10,20))

def f_f(x, y, func):
    print(x*y*func(100,100))
    
f_f(10,20,lambda x,y:x*y) # 이렇게 입력을 함수로 받을 때에도 lambda를 바로 써도 된다

