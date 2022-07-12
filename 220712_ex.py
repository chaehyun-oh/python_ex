#문제01. 수 구분하기
#주어진 수 n이 3의 배수이면서 짝수인 경우 ‘참’을 거짓인 경우 ‘거짓'을 출력하시오.
print('문제01--------')

n = 267

if n % 3 == 0 and n % 2 == 0:
    print('참')
else:
    print('거짓')

#문제02. 길이 구하기
#문자열 word의 길이를 출력하는 코드를 각각 작성하시오. len() 함수를 바로 쓰기보다는 반복문을 활용하세요.
print('\n문제02--------')


word = 'happy!'
n = 0

for char in word:
    n += 1
print(n)


#03 합 구하기
#1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오. sum() 함수 사용 금지
print('\n문제03--------')


i = 0
n =10 
result = 0

while i <= n:
    result += i
    i += 1
print(result)

i = 0
n =10 
result = 0

for i in range(n+1):
    #print(f'i: {i}, n: {n}')
    result += i
print(result)


#04 곱 구하기
#1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
print('\n문제04--------')


i = 1
n = 5
result = 1

while i <= n:
    result *= i
    i += 1
print(result)

i = 1
n = 5
result = 1

for i in range(n):
    result *= i+1
print(result)


#05 평균 구하기
#주어진 숫자의 평균을 구하는 코드를 작성하시오. sum(), len()  함수 사용 금지
print('\n문제05--------')


numbers = [3, 10, 20]
i = 0
totalSum = 0
avrg = 0

for ob in numbers:
    totalSum += ob
    i += 1
avrg = totalSum / i
print(int(avrg))


#06 최댓값 구하기
#주어진 리스트 numbers에서 최댓값을 구하여 출력하시오. max() 함수 사용 금지
print('\n문제06--------')

numbers= [0, 20, 100]
i = 0
mxm = numbers[0]
# numbers 안에 있는 것들 중에서 비교하기 위해서 초기값을 첫번째 값으로 지정

for i in numbers:
    if mxm < i:
        mxm = i
print(mxm)


#07 최솟값 구하기
#주어진 리스트 numbers에서 최솟값을 구하여 출력하시오. min() 함수 사용 금지
print('\n문제07--------')

numbers= [0, 20, 100]
i = 0
mnm = numbers[0]

for i in numbers:
    if mnm > i:
        mnm = i
print(mnm)



#08 두번째로 큰 수 구하기
#주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오. max() 함수 사용 금지
print('\n문제08--------')

numbers= [0, 20, 100]
i = 0
mxm = numbers[0]
mxm2 = numbers[0]
#2번째로 큰 값도 저장해둬야 함

#최대보다는 작지만 두번째로 큰 수보다는 큰 경우

for i in numbers:
    if mxm < i :
        mxm2 = mxm
        mxm = i
    elif mxm2 < i and i < mxm:
        mxm2 = i
print(mxm2)

