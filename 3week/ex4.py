i = 0

num = int(input("숫자를 입락하시오"))

if num > 0 and num < 10: ## 1~9까지
    for i in range(1, 10):
        print(f"{num} X {i} = {num*i}")

else: print("1~9까지의 숫자를 입력하시오")