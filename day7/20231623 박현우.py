import random

# 음악 추천 프로그램
rec_music_list = ['팝', '록', '힙합', 'R&B', '컨트리', '재즈', '전자', '클래식']
rec_music = random.choice(rec_music_list)
print(f"추천 음악: {rec_music}")

if rec_music == '팝':
    print("팝 음악은 1950년대에 시작된 장르로 단순하고 중독성 있는 멜로디와 경쾌한 리듬이 특징입니다.")

elif rec_music == '록':
    print("록 음악은 1950년대와 60년대에 발전한 장르로 일렉트릭 기타, 그럼, 베이스를 사용하는 것이 특징입니다.")

elif rec_music == '힙합':
    print("힙합은 1970년대에 시작된 장르로 랩, 비트박스, 샘플링 등을 사용하는 것이 특징입니다.")

elif rec_music == 'R&B':
    print("리듬앤블루스는 1940년대에 시작된 장르로 소울풀한 보컬, 블루스 멜로디, 종종 복잡하나 하모니를 사용하는 것이 특징입니다.")

elif rec_music == '컨트리':
    print("컨트리 음악은 미국 남부에서 시작된 장르ㅐㅣ로 어쿠스틱 기타, 피들, 벤조를 사용하는 것이 특징입니다.")

elif rec_music == '재즈':
    print("재즈는 19세기 말과 20세기 초에 시작된 장르로 즉흥 연주, 스윙 리듬, 금관 악기 및 목관 악기 사용이 특징입니다.")

elif rec_music == '전자':
    print("전자 음악은 1970년대에 시작된 장르로 전자 악기와 디지털 제작 기술을 사용하는 것이 특징입니다.")

elif rec_music == '클래식':
    print("클래식 음악은 중세 시대로 거슬러 올라가는 서양 고전 전통의 읨악을 포괄하는 장르입니다. 오케스트라 악기, 복잡한 화성, 형식적 구조를 사용하는 것이 특징입니다.")



# 축구 게임
user_select = input("어디를 공격하시겠어요?(왼쪽 상단, 왼쪽 하단, 중앙, 오른쪽 상단, 오른쪽 하단): ")

computer_option = ['왼쪽 상단', '왼쪽 하단', '중앙', '오른쪽 상단', '오른쪽 하단']
computer_select = random.choice(computer_option)

if user_select == computer_select:
    print('컴퓨터가 수비에 성공하엿습니다.')
else:
    print('패널티킥이 성공하였습니다.')