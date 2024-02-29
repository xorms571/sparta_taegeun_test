def restart():
    print('게임을 계속하시겠습니까? (y/n)')
    try:
        choice = input()
        if choice == 'y':
            game()
        elif choice == 'n':
            print('게임을 종료합니다.')
            breakpoint()
        else:
            print('y 혹은 n으로 입력해주세요.')
            restart()
    except:
        print('y 혹은 n으로 입력해주세요.')
        restart()
def game():
    import random
    com = ['가위','바위','보']
    choiceCom = random.choice(com)
    print('게임을 시작합니다.')
    print('"가위, 바위, 보" 중에서 하나만 입력해주세요.')
    while True:
        try:
            choiceUser = input()
            print(f'"플레이어 : {choiceUser}" vs "컴퓨터 : {choiceCom}"')
            if choiceUser == choiceCom:
                print('비겼습니다.')
            elif choiceUser == '가위' and choiceCom == '바위':
                print('졌습니다.')
            elif choiceUser == '보' and choiceCom == '바위':
                print('이겼습니다.')
            elif choiceUser == '바위' and choiceCom == '보':
                print('졌습니다.')
            elif choiceUser == '가위' and choiceCom == '보':
                print('이겼습니다.')
            elif choiceUser == '보' and choiceCom == '가위':
                print('졌습니다.')
            elif choiceUser == '바위' and choiceCom == '가위':
                print('이겼습니다.')
            else:
                print('입력오류!!')
                game()
            restart()
        except:
            print('입력오류!!')
            game()
game()