import random
num = random.randrange(1,11)
count = 0
print('게임을 시작합니다. 숫자를 입력해주세요.')
while True:
    try:
        userNum = int(input())
        count += 1
        if userNum == num:
                print('정답입니다.')
                print(f'{count}번 시도하셨습니다.')
                print('게임을 더 진행할까요? (y/n)')
                try:
                    ans = input()
                    if ans == 'y':
                        print('게임을 시작합니다. 숫자를 입력해주세요.')
                        count = 0
                        num = random.randrange(1, 11)
                    elif ans == 'n':
                        print('게임을 종료합니다.')
                        break
                except:
                    print('y 혹은 n으로 입력해주세요.')
        elif userNum < num:
            print('위')
        elif userNum > num:
            print('아래')
    except:
        print('1~100까지의 숫자만 입력해주세요.')