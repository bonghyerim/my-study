

# function 함수
# 입력 -> 처리 -> 출력
# input(입력)을 받아서 특정 작업(처리)을 수행하고 output(출력)을 반환한다.

# 내장 함수(built-in)
# 파이썬이 기본적으로 제공하는 함수
# print(), len(), zip(), int(), float(), str(), list()
# range()

# abs(값)
# absolute의 약자 숫자형0 데이터의 절댓값을 반영한다.

# print(abs(100))
# print(abs(-100))
# print(abs(3.15))
# print(abs(-3.15))

# sum(리스트)
# 리스트 안의 숫자를 더한 값을 반환한다.
# print(sum([1, 2, 3, 4, 5])) # 15

# max(리스트)
# 리스트 안에서 최댓값을 찾아 반환한다.
# print(max([1, 2, 3, 4, 5]))

# min(리스트)
# 리스트 안에서 최솟값을 찾아 반환한다.
# print(min([1, 2, 3, 4, 5]))

# chr()
# 정수 1개를 입력받고 해당하는 유니코드 문자를 반환한다.
print(chr(65))

# ord()
# 문자 1개를 입력받고 해당하는 정수를 반환한다.
print(ord('A')) # 65

# round(값)
# round(값, 소수자릿수)
# 반올림 함수
print(round(1.234)) # 1
print(round(1.234, 2)) # 1.23
print(round(1.369, 1)) # 1.4

# 함수 정의 (define)
# 함수 이름
# 함수 입력값 parameter
# 함수 결괏값 return value

"""
def 함수이름(함수입력값):
    함수기능코드
    return 함수 결괏값
"""
# def 함수를 정의하는 명령어
# 함수 이름도 변수 이름처럼 규칙을 지켜서 지어야 한다.
# 영어, 숫자, _만 사용
# 숫자로 시작하면 안 됨
# 띄어쓰기하면 안 됨
# 키워드 사용하면 안됨
# 기존에 이미 정의된 함수 이름도 피하는 것이 좋음

def print_names():
    print("손흥민")
    print("황희찬")
    print("김민재")
    print("이강인")
    
# 출력만 주르륵 하고 종료
# output이 없는 함수
# print_names()

def get_name():
    return "bonghyerim"
# return이 있으면 반환값이 있다

def print_my_name():
    print(get_name())

print_my_name()
a = print_names() # 리턴이 없음 
b = get_name() # 리턴이 있음
print(a)
print(b)



# 매개변수, parameter 함수에 입력하는 값
# argument 혼용

def add(a, b): 
    return a + b



# result = add(1, 2)
# print(result)

# print_add(1, 2)
# result = print_add(1, 2)
# print(result)

def print_add(a, b):
    print(a + b)
    
print_add("안녕", "하세요")
print_add(b = "하세요",a = "안녕")

def swap_number(a, b):
    temp = a
    a = b
    b = temp
    print(a, b)

a = 1
b = 2
print("함수 호출 전", a, b)
a, b = swap_number(a, b)
print("함수 호출 후", a, b)
