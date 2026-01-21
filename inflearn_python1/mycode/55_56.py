# 행맨 게임

import time

name = input("what is your name?")

print(f'Hi, {name}, Time to play Hangman')
print()

time.sleep(1)

word = "secret"

# 추측 단어

guesses = ''

# 기회
life = 10

# 핵심 = while문
while life > 0:
    # 실패 횟수
    failed = 0
    
    # 정답 단어 반복
    
    for char in word:
        # 정답 단어 내에 추측 문자가 포함되어 있는 경우
        if char in guesses:
            print(char, end = '') 
        else:
            print("_", end = '')
            failed += 1
        if failed == 0:
            print()
            print()
            print(f'Congratulations! The Guesses is correct!')
            # while 구문 중단
            break
    print()
    
    print()
    guess = input('Guess a character.')
    
    guesses += guess
    
    # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        # 목숨 개수 감소
        life -= 1
        print("Wrong character~")
        print(f'you have {life}, more guesses!')
        
        if life == 0:
            print('you failed looser! :P')