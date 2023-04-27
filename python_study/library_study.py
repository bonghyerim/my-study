# 표준 라이브러리
# 파이썬에서 지원하는 표준 라이브러리
# 파이썬을 설치할 때 자동으로 함께 설치
# 따로 설치하지 않고 import 명령어로 불러옴

# datetime 라이브러리 
# 날짜 관련 라이브러리
# datetime의 date 객체 사용
import datetime
day1 = datetime.date(2023, 4, 17)
day_end = datetime.date(2023, 9, 18)
diff = day_end - day1
print(diff.days)

# 2018년 8월 6일 무슨 요일일까요?
# weekday() ---> 0:월요일 1:화요일 ~ 6:일요일
# import datetime
# day = datetime.date(2018, 8, 6)
# weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
# print(day.weekday())
# print(weekdays[day.weekday()])

# datetime의 포맷팅 코드
# 날짜랑 시간 표시하는 방법
# 년 / 월 / 일
# 월 / 일 / 년
# 일 / 월 / 년
# 2023년 4월 27일
# 2023-04-27
# 23년 4월 27일

import datetime
today = datetime.datetime.today()
print(today)
# strftime()
print(today.strftime("%Y년 %m월 %d일"))
# %Y 년도 4자리 다
# %y 년도 2자리
# %m 월
# %d 일
# %H 시간(24시간)
# %I 시간(12시간)
# %M 분
# %S 초
# %A 요일
print(today.strftime("%A"))

# time 라이브러리
# 시간 관련
import time
time_now = time.time()
print(time_now)
print(time.strftime("%H:%M:%S", time.localtime(time_now)))


# time.sleep()
# import time
# print("before")
# time.sleep(1) # 기재한 시간만큼 멈췄다가 실행한다.
# print("after")
# for i in range(10):
#     print(i)
#     time.sleep(1) # 값은 정수형, 실수형으로 넣을 수 있다.
    
# math
# 수학 관련
import math
result = math.ceil(1.1)
print(result)
result = math.floor(1.9)
# print(result)
# print(math.pi)

# random
# 난수 관련
import random
# random.random()
# 0.0 ~ 1.0 사이의 실수 중 난수 값
random_value = random.random()
print(random_value)

# random.randint(시작, 끝)
# 시작 ~ 끝 사이의 정수 중 난수 값
random_value = random.randint(1, 10)
print(random_value)

# random.choice(리스트)
# 리스트의 요소 중 무작위로 하나를 리턴
foods = ["음식1", "음식2", "음식3", "음식4"]
food = random.choice(foods)
print(food)

li = [1, 2, 3, 4, 5]
random.shuffle(li)
print(li)

lotto_numbers = list(range(1, 46))
my_lotto = []
for i in range(6):
    random_value = random.choice(lotto_numbers)
    if random_value not in my_lotto:
        my_lotto.append(random_value)
print(my_lotto)

# in 연산자
# a in b
# a가 b에 포함되어 있으면 True
# a가 b에 포함되어 있지 않으면 False

# not in 연산자
# a not in b
# a가 b에 포함되어 있지 않으면 True
# a가 b에 포함되어 있으면 False

li = [1, 2, 3, 4, 5]
a = 10
for i in li:
    if a == i:
        print("이미 있음")

if a in li:
    print("이미 있음")

lotto_numbers = list(range(1, 46))
random.shuffle(lotto_numbers)
my_lotto = lotto_numbers[:6]
print(my_lotto) 

# 색 이름과 음식 이름을 합치면 멋진 밴드 이름이 된다고 합니다.
# 색 이름과 음식 이름을 무작위로 뽑아
# 밴드 이름을 추천하는 프로그램을 만들어 보세요.

"""
베이지 블랙 블루 회색 청색 레드 파란 핑크 그레이
쭈꾸미 요거트 오란다 와플 아이스티 떡볶이 커피
"""
# import random
# colors = ["베이지", "블랙", "블루", "회색", "청색", "레드", "파란", "핑크", "그레이"]
# foods = ["쭈꾸미", "요거트", "오란다", "와플", "아이스티", "떡볶이", "커피"]

# color = random.choice(colors)
# food = random.choice(foods)

# print(f"{color} {food}")

# 1. 정답을 정한다. 정답은 4자리 숫자(랜덤)
# 2. 게임 유저가 정답을 입력한다.
# 3. 정답과 비교해서 S / B / OUT 개수 알려준다.
# 4. 정답을 맞추거나, 종료를 입력하면 끝낸다.
# 5. 정답을 맞췄을 때 -> 한번 더 하시겠습니까?

# s -> 숫자 O, 자리 O B -> 숫자 O, 자리 X

# import random
# numbers = list(range(10))
# random.shuffle(numbers)
# answer = numbers[1:5] if numbers[0] == 0 else numbers[:4]
# while True:
#     user_input = input("정답은? ")

#     # 만약 숫자가 아닌 값이 입력되면
#     # 다시 입력하게 한다. ---> 처음으로 간다 ----> continue
#     # 숫자로만 이루어져 있으면 True 아니면 False
#     if user_input == "종료":
#         print("종료합니다.")
#         break
#     if not user_input.isdigit() :
#         print("숫자로 입력해주세요.")
#         continue
    
#     # 만약 4자리 숫자가 아니면 다시 입력하게 한다.
#     # ----> 처음으로 간다 ---> continue

#     elif len(user_input) != 4:
#         print("4자리 숫자로 입력해주세요.")
#         continue
    
#     # 첫 글자가 0인 경우
#     elif user_input[0] == "0":
#         print("첫 번째 숫자를 0이 아닌 다른 숫자로 바꿔주세요")
#         continue

#     # 중복 확인
#     duplicate = False
#     for i in range(3):
#         if user_input[i] in user_input[i+1:]:
#             duplicate =True
#             break
#     if duplicate:
#         print("중복된 숫자가 없게 입력하세요.")
#         continue
#     strike = 0
#     ball = 0
#     out = 0

#     for i in range(4):    
#         input_value = int(user_input[i])
#         if input_value not in answer:
#             out += 1
#         elif input_value == answer[i]:
#             strike += 1
#         else:
#             ball += 1
        
#     print(f"strike: {strike}, ball: {ball}, out: {out}") 
        

#     if strike == 4:
#         print("정답!")
#         user_input = input("한번 더 하시겠습니까? [y/n] ")
#         if user_input == "y":
#             numbers = list(range(10))
#             random.shuffle(numbers)
#             answer = numbers[1:5] if numbers[0] == 0 else numbers[:4]
#         else:
#             break

# 삼항 연산자
# 참일 때 값 if 조건 else 거짓일 때 값
# result = "참" if True else "거짓"
# result = "참" if False else "거짓"
# print(result)


# def is_odd_number(n):
#     return "홀수" if n % 2 == 1 else "짝수"

# OS
# OS 자원을 제어

import os
# os.environ
# 시스템의 환경 변수 값을 리턴한다.
# print(os.environ)

# os.getcwd()
# get current working directory
# print(os.getcwd())

# os.mkdir(디렉터리)
# 디렉토리(폴더)를 만든다.
# os.mkdir("폴더1")

# os.rename(원래이름, 바꿀이름)
# 파일의 이름을 바꾼다.
# os.rename("파일1", "파일2")

# os.rmdir(디렉터리)
# 디렉터리(폴더)를 지운다.
# 폴더 안에 아무것도 없어야 함
# os.rmdir("폴더1")

# os.unlink(파일)
# 파일을 지운다.
# os.unlink("파일2")

# os.unlink(파일)
# 파일을 지운다.

# os.path
# os.path.exist("경로")
# 파일이 있으면 True, 없으면 False
import os
if not os.path.exists("없는파일"):
    f = open("없는 파일", "w")
    f.close
f = open("없는 파일", "r")

# os.path.join("경로", "경로", "경로")
# 경로를 합쳐서 1개의 경로로 만들어준다.
# import os
# cwd = os.getcwd()
# my_folder = "python_study"
# file_name = "test_file.txt"
# file_path = os.path.join(cwd, my_folder, file_name)
# with open(file_path, "w", encoding="utf-8") as f:
#     f.write("테스트 파일을 작성합니다.")


# 외부 라이브러리
# 파이썬 표준 라이브러리가 아닌 라이브러리
# pip를 사용해서 설치한다.

# pip
# package installer for python
# 파이썬 모듈, 패키지 설치하는 도구
# PyPI(Python Package Index) 파이썬 소프트웨어 저장 공간
# PyPI에 있는 파이썬 패키지를 설치해준다.

# 패키지 설치(최신 버전 설치)
# pip install 패키지 이름

# 패키지 삭제
# pip uninstall 패키지 이름

# 특정 버전으로 설치
# pip install 패키지 이름--1.0.5

# 최신 버전으로 업그레이드
# pip install --upgrade 패키지 이름

# 설치된 패키지 리스트 확인
# pip list