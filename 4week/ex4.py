def sumfunc(a):
    return sum(range(1,a+1))

print('1이상의 정수를 입력하시오 :' )
a = int(input())

result = sumfunc(a)
print(f'1~ {a}까지의 합은 {result}이다')



#def sumfunc(num):
#  sum = 0
#  for j in range(1,num+1):
#  sum = sum + j
#  return sum
#sum = sumfunc(num)
#print(f"1~{num}까지 정수의 합은 {sum}입니다)