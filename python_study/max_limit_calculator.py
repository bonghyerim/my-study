# my_calculator 모듈의 MyCalculator 클래스를 정의하세요.
# add, sub, mul, div 메소드를 사용하여 더하기, 빼기, 곱하기, 나누기를 할 수 있다.
# 0으로 나눴을 때 에러가 발생하지 않도록 처리한다.
# 입력되는 정수가 1개라도 100보다 크면 계산하지 않고
# 100 이하의 값을 입력하도록 안내 메세지를 출력한다.
# 계산 결과가 100보다 크면 계산하지 않고 100 이하의 결과가 나오는 값을 
# 입력하도록 안내 메시지를 출력한다.


from my_calculator import MyCalculator
my_calculator = MyCalculator()
class calculator(MyCalculator):
    operator = input("원하는 계산을 입력하세요: ")
    n1 = int(input("정수 1: "))
    n2 = int(input("정수 2: "))
    if n1 >= 100 or n2 >= 100:
        print("100 이하의 값만 입력하세요")
    else:
        if operator == "1":
            my_calculator.add(n1, n2)
        elif operator == "2":
            my_calculator.sub(n1, n2)
        elif operator == "3":
            my_calculator.mul(n1, n2)
        elif operator == "4":
            if n2 == 0:
                print("0으로 나눌 수 없습니다.")    
            else :
                my_calculator.div(n1, n2)
        else:
                print("잘못 입력했습니다.")