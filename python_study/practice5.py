# 거꾸로 배열해도 같은 단어 또는 문장이 되는
# 회문(palindrome)인지 판별하는 함수를 정의하세요
# 함수에 문자열을 입력받고 회문이면 True
# 아니면 False를 반환하도록 정의하세요.
# 함수 이름 : is_palindrome
# 반환 값 : True 또는 False


def is_palindrome(input_string):
    input_string = input_string.replace(" ","") # 문자열 중간에 있는 공백 제거


    # length = len(input_string)
    # for i in range(length//2):
    #     if input_string[i] != input_string[length - 1 - i]:
    #         return False
    # return True

    return input_string == input_string[::-1]


result = is_palindrome("기러기")
print(result)