import random

def number_compare(number, g_number):
    choice = 'y'

    if number < g_number:
        print('입력한 숫자가 정답보다 작습니다.')
        print('숫자를 다시 입력하세요')
        print('-'*20)

    elif number > g_number:
        print('입력한 숫자가 정답보다 큽니다.')
        print('숫자를 다시 입력하세요')
        print('-'*20)

    else:
        print('정답!')
        print('-' * 20)
        print('축하! 정답입니다. 숫자를 잘 찾으셨군요.^^')
        choice = input('다시 하시겠습니까? (y/n)? : ')
        if (choice == 'y'):
            print('프로그램을 종료합니다.')
            return choice

    return choice

choice = 'y'
guess_number = 0
index = 0

random_number = random.randint(1, 50)

print('숫자 맞추기 게임\n')
print('-'*20)
print('1부터 50까지의 숫자만 입력하세요.\n')
print('숫자를 맞출 수 있는 기회는 10번입니다.\n')

while choice == 'y':
    if index >= 10:
        print('10번의 기회가 끝났습니다.')
        print('프로그램을 종료합니다.')
        break

    elif random_number == guess_number:
        index = 0
        random_number = random.randint(1, 50)
        break

    else:
        print('-'*20)
        guess_number = int(input('숫자를 입력 : '))
        print('')
        choice = number_compare(guess_number, random_number)
        index += 1.

    