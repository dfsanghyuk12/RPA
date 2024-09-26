def sumfunc(a):
    return sum(range(1,a+1))

print('1이상의 정수를 입력하시오 :' )
a = int(input())

result = sumfunc(a)
print(f'1~ {a}까지의 합은 {result}이다')

