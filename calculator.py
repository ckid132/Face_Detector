# 사용자로부터 연산자와 피연산자를 입력받기

num1 = float(input("첫 번째 숫자를 입력하세요: "))
operator = input("연산자를 입력하세요 (+, -, *, /): ")
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 입력된 연산자에 따라 계산 수행
if operator == '+':
    result = num1 + num2                 
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        result = "0으로 나눌 수 없습니다."
    else:
        result = num1 / num2
else:
    result = "올바른 연산자를 입력하세요."

# 결과 출력
print("결과 : ", result)
