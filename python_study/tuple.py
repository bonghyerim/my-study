# tuple(튜플)형
# 값이 정해지면 값을 수정할 수 없다
# 튜플은 element의 값을 수정할 수 없다.
# 수정을 하면 안 되는 데이터에 사용
# mutable / immutable
# mutable 수정 가능한
# list, dict
# immutable 수정 불가능한
# int, float, str, tuple

my_list = [1, 2, 3]
my_list[0] = 5
print(my_list) # 5, 2, 3

my_tuple = (1, 2, 3)
my_tuple[0] = 5 # Error tuple형은 수정 불가능
print(my_tuple)

tuple_1 = ("Hello", "World", "Python")
t2 = (1, 2, 3, 4, 5)
t3 = (1, 2, "Hello")
t4 = 1, 2, 3
t5 = (1, 2, (3, 4, 5))

t6 = tuple_1 + t2
t7 = t3 * 3
t7 = t3 * 4

# 값을 수정하는 게 아니라 새로운 값을 만드는 거라 가능


print(t3[2])
print(t3[0:2]) # 슬라이싱을 하면 튜플 형태로 가져온다.
len(t3)

t5 = (1, 2, (3, 4, 5))
print(t5[2][1]) #4
t8 = (5, 3, 1, 4, 2)
# 순서를 정렬할 수 없다 값이 바뀌니깐..

for i in t8:
    print(i)

# 인덱스 순서대로 출력에 들어간다
# 인덱스, 튜플은 순서가 있는 데이터
# for문 돌릴 때 순서대로 꺼낸다


# 2 ~ 9 사이의 숫자를 입력받아 해당하는 단의 구구단을 출력하세요.
# 2 ~ 9 사이의 숫자가 아닌 값이 입력된 경우, 잘못 입력되었다고
# 출력하고 다시 입력받으세요.


# if a >= 2 and a <= 9:
#     pass
# if 2 <= a <= 9:
#     pass
    
n = int(input("몇 단? "))
while not 2 <= n <= 9: 
    print("2 ~ 9 사이의 숫자를 입력해 주세요.")
    n = int(input("몇 단?"))

for i in range(1, 10):
     print(n, "*", i, "=", n*i)

for i in range(9): # 안쪽 코드를 잘 짜면
    print(n, "*", i, "=", n*(i+9))


# 정수를 입력받고 
# 그 정수보다 작은 수 중 가장 큰 제곱수를 출력하세요.

n = int(input("정수? : "))
i = 1
while True:
    # i * i
    if i ** 2 >= n:
        break
    answer = i ** 2
    i += 1
print(answer)

# [1, 2, 3, 4, 5]
# [10, 20, 30, 40, 50]
# [532, 5941, 54682, 58, 5]
# 3개의 리스트에서 같은 인덱스의 값끼리 더하여 출력하세요
  
li_1 = [1, 2, 3, 4, 5]
li_2 = [10, 20, 30, 40, 50]
li_3 = [532, 5941, 54682, 58, 5]

for i in range(5):
    print(li_1[i] + li_2[i] + li_3[i])

for x, y, z in zip(li_1, li_2, li_3):
    print(x + y + z)

i = 0
while i < 5: 
    print(li_1[i] + li_2[i] + li_3[i])
    i += 1

# zip()
# 길이가 같은 list를 묶어서 for문 등으로 사용 가능한 iterable을 반환한다.

# 정수를 입력받고 1부터 입력받은 정수까지 모두 출력하세요.
# 단, 숫자에 3, 6, 9가 들어있는 경우 짝이라고 출력하세요.

n = int(input("정수 ? "))

# "3", "6", "9"
# 931 // 100
# 931 % 100
# 31 // 10 == (931 % 100) // 10
# 931 = 9 * 10**2 + 3 * 10**1 + 1 * 10**0

for i in range(1, n + 1):
    # 3, 6, 9가 들어있으면
    # 931 --> "931"
    answer = i
    for j in str(i):
        if int(j) % 3 == 0 and j != "0":
            answer = "짝"
            break
    print(answer)


# 정수 입력받고 그 정수의 약수를 모두 출력하세요.
# 약수 : 나누었을 때 나머지가 0으로 나머지가 0으로 나누어 떨지게 하는 수


n = int(input("정수 ? "))

for i in range(1, n+1): # 1 ~ n
    if n % i == 0:
        print(i)

i = 1
while i <= n:
    if n % i ==0:
        print(i)
    i += 1