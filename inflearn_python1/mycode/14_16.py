# 문자열 생성

str1 = "I am Python"
str2 = 'Python'

str3 = "How are you?"

print(type(str1), type(str2), str3)
print(len(str1))

# len함수는 str의 길이를 알려준다! 와우!!!

# 빈 문자열

str4 = ''
str5 = str()

print(f'len of str4 : {len(str4)} and type of str5 is {type(str5)}')

# 이스케이프 문자 ` 출력하고 싶으면?

# \n : 개행(줄바꿈)
# \t : 탭(tab)

print("`")
print('`') # 엥?? 뭐야. 다되는데? 버젼 업글되면서 그냥 다 되나봐

# Raw String

s1 = r'D:\tpython\t``est'
# 역슬레시나 이런 문자들을 있는 그대로 쓴다
print(s1)

# 멀티라인 입력 = 여러줄에 걸쳐서 한번에 입력받는거

lstr = "řrfdsafdsafdsafdsafqiotr gjkgfd;gdfjiop;faopfweaioweafvhncjk;sjklwaerfujp;tgreaiogjhklfdahjkvcdhrwiaeuytugirweahjgkdfslhjklasdfkl"

#이런거 보기 어려우니까

mlstr = '''
String
Multi line
test
'''

# 작은따옴표 세 번 ''' ''' 이 사이의 텍스트들을 그대로 읽는다
print(mlstr)

# 문자열 연산

st1 = "Python"
st2 = "Apple"
st3 = "Mac book air"
st4 = "Mac Book Pro"

print(st1 * 3)
print(st1 + st2)
print('m' in st3)
print(int('P' not in st2))

# 문자열 형 변환

print(str(66),type(str(66)))

print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha)

print("Capitalize: ", st1.capitalize()) # 첫 글자를 대문자로 바꿔준다
print("endswith? :", st2.endswith('e')) # 문자열의 마지막 문자가 endswith() 안의 내용 'e'가 맞는지 알려준다
print(f'replace : {st3.replace("air", "pro")}') # st3의 일부분을 바꿔서 출력한다
print(st3) 

print(f'sorted : {sorted(st1)}') # 문자열을 순서대로 정렬한 후 배열로 출력하는 것
print(f'split : {st3.split(' ')}') #split() 안의 문자를 기준으로 나눠서 배열로 출력하는 것

# print에서만 쓸 수 있는게 아니라 변수 선언이나 다양한 상황에서도 사용 가능하다!

# 반복(시퀀스)

sstr = "Good boy!"

print(dir(sstr)) # __iter__

# 출력
for i in sstr:
    print(i)

# 슬라이싱

srl = "Nice Python"

# 슬라이싱 연습
print(srl[:4]) # 0번 인덱스부터 시작해서[이상:미만] 의 범위로 나온다.

# [5:] 이렇게 하면 인덱스 5 이상부터 끝까지를 의미한다
# [:3] 이렇게 하면 처음부터(0번 인덱스부터) 3 인덱스 미만으로 (2 인덱스 까지)

print(srl[-6:])

# 음수 인덱스는? 문자열의 맨 마지막 자리부터 -1로 시작하는 숫자를 의미
# [-6:] 뒤에서부터 6번째 인덱스부터 끝까지 출력하느걸 의미
# [0:11:2] = 0번 인덱스부터 10번 인덱스까지 두칸 간격으로 출력한다는 의미
# [::-1] = 처음부터 끝까지 뒤에서부터 역순으로 출력한다는 의미

# 아스키 코드

print(ord('a')) # 'a'의 아스키코드는 97이다.
print(chr(122)) # 아스키코드 122번인 'z'를 출력한다