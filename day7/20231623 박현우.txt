def set():
    a = {1, 2, 3, 4, 5}
    b = {3, 4, 5, 6, 7}

    print("a 집합 : ", a)
    print("b 집합 : ", b)

    while True:
        print("구하고 싶은 집합을 선택하세요")
        sel = input("1. 합집합 2. 교집합 3. 차집합 4. 종료 : ")

        if sel == "1":
            print("합집합 : ", a | b)
        elif sel == "2":
            print("교집합 : ", a & b)
        elif sel == "3":
            print("차집합 : ", a - b)
        elif sel == "4":
            break

def absolute():
    num = int(input("구히고 싶은 정수값을 입력하세요 : "))
    print('절대값, ', abs(num))

def power():
    # 거듭제곱을 구하는 함수
    num = int(input("구하고 싶은 거듭제곱의 아랫값을 입력하세요 : "))
    pow = int(input("구하고 싶은 거듭제곱의 지수를 입력하세요 : "))
    print(num, "의 ", pow, "제곱은 ", num ** pow, "입니다.")

def distance():
    # 두 점 사이의 거리를 구하는 함수
    x1, y1 = map(int, input("첫번째 점의 좌표를 입력하세요 : ").split())
    x2, y2 = map(int, input("두번째 점의 좌표를 입력하세요 : ").split())

    print("두 점 사이의 거리는 ", ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, "입니다.")

print('재미있는 수학을 알려주는 프로그램입니다')
while True:
    print('1. 집합 연산')
    print('2. 절대값 구하기')
    print('3. 거듭제곱 구하기')
    print('4. 두 점 사리의 거리 구하기')
    print('5. 종료')
    
    sel = input('원하는 기능을 선택하세요 : ')

    if sel == '1':
        set()
    elif sel == '2':
        absolute()
    elif sel == '3':
        power()
    elif sel == '4':
        distance()
    elif sel == '5':
        break