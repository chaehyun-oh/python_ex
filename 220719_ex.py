import sys

sys.stdin = open("./swea_input/input.txt", "r")
#제출시에는 위에 주석처리 or 제외
#표준입출력...


#SWEA-2029-몫과 나머지 출력하기
T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    print(f'#{test_case}',a//b, a%b)
    

#SWEA-1545-거꾸로 출력

T = int(input())

for test_case in range(1, T + 1):
    a = int(input())

    for i in range(a+1):
        print(a-i)
    

#SWEA-2071-평균값 구하기

# T = int(input())

# for test_case in range(1, T + 1):
#     
#     nums = int(input())
#   mxm = nums[0]
#     한 줄씩 최댓값 구하기
#   for i in nums:
#       if mxm < i:
#           mxm = i



#SWEA-2070-큰 놈, 작은 놈, 같은 놈
T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    if a > b:
        print('>')
    elif a < b:
        print('<')
    elif a == b:
        print('=')


#문제20. 각 자릿수의 합 구하기

n = 123
s = 0

while n:
    s += n%10
    n //= 10
    
print(s)

#풀이-divmod()
number = 123
result = 0

number, remainder = divmod(number, 10)
result += remainder

print(result)


#문제21. 숫자 뒤집기

n = 1234
s = 0
i = 0
rr = []
new_n = 0

while n:
    s = n%10
    rr.append(s)
    n //=10
    i += 1

for j in rr:
    i -= 1
    new_n += j*(10**i)
print(new_n)


#풀이
#str
number = 123
print(str(number)[::-1])

#
#number 123 = 1*100 + 2*10 + 3
#이전 결과값에 10을 곱하고 나머지를 더해주기
number = 123
result = 0

while number:
    #이전 결과에 10 곱하기
    result*= 10
    #나머지 더하기
    result += number%10
    #number 깎기
    number //= 10
print(result)
