"""

eng 변수, kor 변수, math 변수를 만들고
각 변수는 과목의 시험 점수이다.
영어 점수는 80점
국어 점수는 60점
수학 점수는 50점
3과목 점수의 평균을 내고 
평균 점수에 따라 성적을 출력한다
A : 91 ~ 100
B : 81 ~ 90
C : 71 ~ 80
D : 61 ~ 70
F : 60 이하
"""

eng = int(input("영어 점수 : "))
# eng = int(eng)
kor = int(input("국어 점수 : "))
math = int(input("수학 점수 : "))

a = (eng + kor + math) / 3

if  a >= 91:
    print ("A")
elif  a >= 81:
    print ("B")
elif  a >= 71:
    print ("C")
elif  a >= 61:
    print ("D")
else:
    print ("F")

# input() 함수
# 정보를 입력받는 함수
# user_input = input()
# print(user_input)

# 정수형 변환 함수
# int() integer
