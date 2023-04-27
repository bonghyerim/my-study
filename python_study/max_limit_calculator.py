# my_calculator 모듈의 MyCalculator 클래스를 정의하세요.
# add, sub, mul, div 메소드를 사용하여 더하기, 빼기, 곱하기, 나누기를 할 수 있다.
# 0으로 나눴을 때 에러가 발생하지 않도록 처리한다.
# 입력되는 정수가 1개라도 100보다 크면 계산하지 않고
# 100 이하의 값을 입력하도록 안내 메세지를 출력한다.
# 계산 결과가 100보다 크면 계산하지 않고 100 이하의 결과가 나오는 값을 
# 입력하도록 안내 메시지를 출력한다.


from my_calculator import MyCalculator
class MaxLimitCalculator(MyCalculator):
    def add(self, n1, n2):
        if n1 > 100:
            print("100보다 작은 수를 입력하세요.")
        elif n2 > 100:
            print("100보다 작은 수를 입력하세요.")
        else:
            result = n1 + n2
            if result > 100:
                print("계산 결과가 100보다 작아야 합니다.")
            else:
                print(f"{n1} + {n2} = {n1+n2}")
    
    
    def sub(self, n1, n2):
        if n1 > 100:
            print("100보다 작은 수를 입력하세요.")
        elif n2 > 100:
            print("100보다 작은 수를 입력하세요.")
        else:
            result = n1 - n2
            if result > 100:
                print("계산 결과가 100보다 작아야 합니다.")
            else:
                print(f"{n1} - {n2} = {n1-n2}")    
    
    
    def mul(self, n1, n2):
        if n1 > 100:
            print("100보다 작은 수를 입력하세요.")
        elif n2 > 100:
            print("100보다 작은 수를 입력하세요.")
        else:
            result = n1 * n2
            if result > 100:
                print("계산 결과가 100보다 작아야 합니다.")
            else:
                print(f"{n1} * {n2} = {n1*n2}")
    
    
    def div(self, n1, n2):
        if n1 > 100:
            print("100보다 작은 수를 입력하세요.")
        elif n2 > 100:
            print("100보다 작은 수를 입력하세요.")
        # elif n2 == 0:
        #     print("0")

        else:
            try:
                result = n1/n2
            except ZeroDivisionError:
                print("0으로 나누지 마세요.")
            
            result = n1 / n2
            if result > 100:
                print("계산 결과가 100보다 작아야 합니다.")
            else:
                print(f"{n1} / {n2} = {n1/n2}")

my_max_limit_calculator = MaxLimitCalculator()
my_max_limit_calculator.add(100, 200)
