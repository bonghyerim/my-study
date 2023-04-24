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
