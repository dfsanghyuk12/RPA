def sum_int(a,b): ##':'으로 정의, 블럭으로 들여쓰기
    return a+b ##여기까지 함수블록, return은 함수를 종료

num1 = 10
num2 = 20

result = sum_int(num1, num2)##함수의 호출 a에 10, b에 20이 넘어옴. result=30
print(f'{num1} + {num2} = {result}')

def mul_int(a,b): 
    return a*b

result =  mul_int(num1, num2)
print(f'{num1} X {num2} = {result}')