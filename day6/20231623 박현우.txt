import random 
import webbrowser
from urllib import parse

menu = 0

music_list = []

while True:
    print('-'*50)
    print('         음악 플레이리스트 관리 프로그램        ')
    print('-'*50)

    print('1. 음악 추가')
    print('2. 음악 삭제')
    print('3. 음악 목록 보기')
    print('4. 음악 하나 추천하기')
    print('5. 음악 5개 추천하기')
    print('6. 유튜브에서 음악 검색하기')
    print('7. 종료')
    print('')    

    menu = int(input('메뉴를 선택하세요 : '))
    print('')
    if menu == 1:
        music = input('추가할 음악을 입력하세요 : ')
        music_list.append(music)
        print('음악이 추가되었습니다.')
        print('')

    elif menu == 2:
        music = input('삭제할 음악을 입력하세요 : ')
        music_list.remove(music)
        print('음악이 삭제되었습니다.')
        print('')

    elif menu == 3:
        print('음악 목록')
        print('-'*50)
        for i in music_list:
            print(i)
        print('')
    
    elif menu == 4:
        print('음악 추천')
        print('-'*50)
        print(random.choice(music_list))
        print('')

    elif menu == 5:
        print('음악 추천')
        print('-'*50)

        if (len(music_list) < 5):
            print('음악이 5개 이하입니다.')
            print('')
            continue

        recommend_musics = random.choices(music_list, k=5)
        for music in recommend_musics:
            print(music)
        print('')

    elif menu == 6:
        print('유튜브에서 음악 검색')
        print('-'*50)
        search = input('검색할 음악을 입력하세요 : ')
        print('')

        search = parse.quote(search)
        webbrowser.open(f"https://www.youtube.com/results?search_query={search}")

    elif menu == 7:
        print('프로그램을 종료합니다.')
        break