#문제 14. 문자의 갯수 구하기
#문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요. count() 메서드 사용 금지
print('문제14')

word = 'apple'
i = 0
for char in word:
    if char == 'a':
        i += 1
print(i)


#문제 15. 문자의 위치 구하기
#문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요. 
#a 가 없는 경우에는 -1을 출력해주세요.
#find() index() 메서드 사용 금지
print('\n문제15')

word = 'banana'
i = 0
for char in word:
    if char == 'a':
        i += 1
        print(i)
        break
    else:
        print(-1)

#풀이1: 인덱스로 접근
word = 'banana'

for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx)
        break
else:
    print(-1)

#풀이2: a의 유/무 확인 boolean
is_a = False
for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx)
        is_a = True
        break

if not is_a :
    print(-1)


#문제 15.-1 문자의 위치 구하기
#문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요. find() index() 메서드 사용 금지
print('\n문제15-1')

#풀이: 리스트에 담기
word = 'banana'
result = []
for idx in range(len(word)):
    if word[idx] == 'a':
        result.append(idx)
print(result)




#문제 16. 모음 등장 여부 확인하기
#문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오. 모음 : a, e, i, o, u 
#count() 사용 금지
print('\n문제16')

word= 'apple'
i = 0

for char in word:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        i += 1
print(i)

#풀이
count = 0

for char in word:
    # ['a', 'e', 'i', 'o', 'u']
    if char in 'aeiou':
        count += 1
print(count)

#문제 17. 소문자-대문자 변환하기
#소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
#.upper(), .swapcase() 사용 금지
print('\n문제17')

word = 'banana'

for char in word:
    print(chr(ord(char)-32))

for char in word:
    nums = ord(char)
    nums = nums-32
    print(chr(nums))
# 알파벳을 숫자로 바꾸고
# 숫자를 -32 한 후
# 다시 숫자를 알파벳으로 바꿈

#문제 18. 알파벳 등장 갯수 구하기
#문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요
print('\n문제18')

word = 'banana'
apb = {}

for char in word:
    apb[char] += 1
    
print(apb)


#풀이
word = 'banana'
result = {}
for char in word:
    #딕셔너리에 키가 없으면 
    if not char in result:
        #키, 값을 1로 초기화
        result[char] = 1
    #딕셔너리에 키가 있으면
    else:
        result[char] = result[char] + 1
print(result)

#풀이2
result = {}
for char in word:
    result[char] = result.get(char, 0) + 1
print(result)

#출력부분
for key in result:
    print(key, result[key])