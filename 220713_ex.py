#예제01. 기초함수
#숫자 n을 받아 세제곱 결과를 반환하는 함수 cube를 정의하시오.  cube 함수를 호출하여 12의 세제곱 결과를 출력하시오

print('예제01')


def cube(n):
    return n**3

print(cube(12))


#예제 02. 기초 함수
#가로와 세로의 길이를 각각 a, b로 받아 사각형 넓이와 둘레를 함께 반환하는 함수 rectangle을 정의하시오. 
#사각형이 가로가 20, 세로가 30일 때의 결과를 출력하시오.
#* 사각형 넓이 : 가로 * 세로 
#* 사각형 둘레 : (가로 + 세로) * 2
print('\n예제02')

def rectangle(a, b):
    return a*b, (a+b)*2

print(rectangle(20, 30))


#문제 09. 득표수 구하기
#주어진 리스트가 반장 선거 투표 결과일 때 이영희의 총 득표수를 출력하시오.
print('\n문제09')

students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

i = 0

for vote in students:
    if vote == '이영희':
        i += 1
print(i)


#문제 10. 5의 개수 구하기
#주어진 리스트의 요소 중에서 5의 개수를 출력하시오.
print('\n문제10')

numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

i = 0

for num in numbers:
    if num == 5:
        i += 1
print(i)

#문제 11. 구구단 출력
#2단부터 9단까지 반복하여 구구단을 출력하세요.
#문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.
print('\n문제11')


for i in range(2,10):
    print(f'{i} 단')
    for j in range(1,10):
        print(f'{i}x{j} = {i*j}')


#문제 12. 문자열 조작하기
#주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.
print('\n문제12')

word = 'apple'
word2 = ''

for char in word:
    if char != 'a':
        word2 += char
print(word2)


#문제 13. 문자열 조작하기2
#주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
print('\n문제13')

word = 'apple'

word_rvs = word[::-1]
print(word_rvs)

#print(' '.join(reversed(word)))

word2 = ''
for char in word:
    word2 = char + word2
print(word2)

#알고리즘 문제푸는 방식에 익숙해지는 방식...인덱스 조율
word2 = ''
for i in range(len(word)):
    print(word[len(word)-i-1], end='')
    #end 기본값 \n 을 공백으로 변경해서 한 줄로 출력