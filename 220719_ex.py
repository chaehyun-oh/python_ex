# import sys

# sys.stdin = open("input.txt", "r")


#SWEA-2029-몫과 나머지 출력하기
# a, b = map(int, input().split())

# for i in range(n):

# print(f'{i}',a//b, a%b)


#SWEA-1545-거꾸로 출력

n = int(input())

for i in range(n+1):
    print(n-i)
    

#SWEA-2071-평균값 구하기

# nums = list(input())




#SWEA-2070-큰 놈, 작은 놈, 같은 놈

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
