

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
print(a) # none 출력
print(b) # 결과 출력



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
    return a, b # 지역변수

a = 1 
b = 2 # 전역변수
print("함수 호출 전", a, b)
a, b = swap_number(a, b) 
print("함수 호출 후", a, b)


# 다음 함수를 정의하세요.
# 함수 이름 : mul
# 함수 입력값 : 정수 2개
# 함수 출력값 : 정수 2개의 곱

def mul(n1, n2):
    return n1 * n2

print(mul(1, 2))

result = mul(1, 2)
print(result)

a = 1
b = 2
c = 3
a, b, c = 1, 2, 3
d, e, f = [4, 5, 6]
g, h, i = (7, 8, 9)

temp = a
a = b
b = temp
a, b = 1, 2
a, b = b, a

# 기본 값 매개변수
# default value parameter
# 함수 호출 시 n2에 입력된 값이 없으면 기본값 사용

def mul(n1, n2 = 1): 
    return n1 * n2

mul(1, 2)
mul(1)

def test_func(x, test=[]):
    test.append(x)
    print(x, test)

test_func(1)
test_func(2) # list 지역변수

# 기본값을 사용할 때 리스트를 사용하면 값이 누적된다.
# 기본값으로 리스트를 쓰면 안 된다.

def test_func1(x, test=5):
    test = test
    print(x, test)

test_func1(1)
test_func1(2)


def test_func2 (x, text=None): 
    if test == None:
        test = [] 
    test.append(x)
    print(x, test)


# 기본값이 있는 매개변수는 기본값이 없는 매개변수보다 뒤에 위치해야함

def sub(n1, n2, n3):
    print(n1 - n2 - n3)

# 1 ~ 10까지 더한다.
# *를 사용한 매개변수
# 입력값이 몇 개가 될지 모를 때 (안 정해졌을 때)

def add_many(*args):
    # 튜플처럼 사용
    # 인덱싱, 슬라이싱
    result = 0
    for i in args:
        result += i
    return result

result1 = add_many(1, 2, 3, 4, 5)
print(result1)

result2 = add_many(3, 2, 5, 9, 1)
print(result2)

result3 = add_many(1, 2)
print(result3)


# 일반 매개변수랑 같이 사용 가능하다
def calc_many(n1, *args):
    result = n1
    for i in args:
        result += i
    return n1

# 키워드 매개변수
# **kwargs
# keyword arguments
# 딕셔너리로 사용
# 뒤에 들어오는 값들이 유동적일 때 사용

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1, b=2)
print_kwargs(name='이름', age=10)

# 함수의 반환
# return 반환값
# return을 만나면 반환값을 반환함과 동시에 함수가 종료된다.
# 함수의 반환값은 무조건 1개
def test_func5():
    print(1)
    print(2)
    return None
    print(3)
    print(4)
    print(5)

def test_func6(a, b):
    # return (a + b, a * b)
    return a + b, a * b 
result = test_func6(1, 2)
res_add, res_mul = test_func6(1, 2)
# res_add, res_mul = test_func6(a+b, a*b)
print(result)
print(res_add, res_mul)

# 개수나 용도가 정해지지 않았을 때 *, **

# 홀수 판별 함수
# 정수 1개를 입력받고 홀수인지 판별하는 함수
# 함수 이름 : is_odd_number
# 파라미터 : n
# 반환값 : 홀수면 True, 짝수면 False

# 1
def is_odd_number(n):
    if n % 2 == 1:
        return True
    else :
        return False

# 2
def is_odd_number(n):
    if n % 2 == 1:
        return True
    return False

# 3
def is_odd_number(n):
    return n % 2 == 1


# 테두리를 출력하는 함수
# 문자열을 입력받고 print 함수를 이용해 테두리와 함께 문자를 출력한다.
# 함수 이름 : get_bordered_str
# 파라미터 : message
# 반환값 : None
# print 예시

"""
*****
hello
*****
"""

def get_bordered_str(message):
    message = str(message)
    n = len(message)
    print("*" * n)
    print(message)
    print("*" * n)

get_bordered_str ("hello")
get_bordered_str (12345)


# 속도를 변환하는 함수
# m/s단위의 속도가 입력되면 -> km/h단위의 속도로 변환한다.
# 함수 이름 : convert_velocity
# 파라미터 : velocity
# 반환값 : km/h로 변환된 속도

def convert_velocity(velocity):
    # 1초에 1m -> 1m/s
    # 1m/s로 한 시간 동안 가면 몇 m?
    # 1m/s * 3600(1시간)
    # 3600m/h
    # 1k는 몇 m? 1000m
    # 3600m/h 는 몇 km/h?
    # 3600m/h / 1000(1km)
    # 1m/s ==> 3.6km/h
    # 1m/s * 3600 / 1000 ==> 3.6km/h
    # 초속 * 3600 / 1000 ==> 시속
    result = velocity * 3.6
    return result

velocity = convert_velocity(10)
print(velocity)

"""
출력 결과 n -> 4
*
**
***
****
"""
# 별 찍기 함수
# 정수를 함수에 입력하여 호출하면 해당 정수 줄의 별을 화면에 출력한다.

# 함수 이름 : print_stars
# 파라미터 : n
# 반환값 : None

def print_stars(n):
    for i in range(0, i+1):
        print(n * "*")

    for i in range(1, i+1):
        print(i * "*")
    
    for i in range(n):
        print("*" * (i + 1))

print_stars(5)

def print_stars(n):
    i = 0
    while i < n:
        j = 0
        while j < i+1:
            print("*", end="")
            j += 1
        print()
        i += 1

# 2중 for문
def print_stars(n):
    for i in range(n): # 0 ~ n-1
        for j in range(i+1): # 0 ~ i j가 중요한 게 아니라 횟수
            print("*", end="")
        print() # 줄바꿈
    
print_stars(5)