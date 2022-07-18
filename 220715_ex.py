#03. 예제 [오류 해결] 입력받기
print('예제03')

#오류: 입력값이 문자열인 상태에서는 sum함수 사용 불가 > 입력값을 형변환해서 해결

# numbers = input().split() --기존 코드
numbers  = map(int, input().split()) 
print(sum(numbers))


#04. 예제 [오류 해결] 입력받기2
print('예제04')

#오류: 문자열을 입력받아 단어로 나눠야하는데 입력값을 int로 형변환함 > int 형변환 제거

# words = list(map(int, input().split())) --기존코드
words = list(input().split()) 
print(words)


#05. 예제 [오류 해결] 숫자의 길이 구하기
print('예제05')

#오류: number값의 자료형이 int이기 때문에 len으로 구할 수 없음 > 문자열로 형변환해서 len 사용

# number = 22020718 --기존 코드
number = '22020718'
print(len(number))


#06. 예제 [오류 해결] 1부터 N까지의 2의 곱 저장하기
print('예제06')

#오류: 1부터 n까지의 곱이지만 0부터 시작함, answer의 자료형이 튜플로 지정되어있어 변경이 불가능함 > range 범위 수정, 리스트로 형변환

N = 10
# answer = () --기존코드
answer = []
# for number in range(N + 1): --기존코드
for number in range(1, N + 1):
    answer.append(number * 2)

print(answer)


#07. 예제 [오류 해결] 평균 구하기
print('예제07')

#오류: count를 증가시키는 코드가 for문 바깥에 있어서 리스트의 원소 갯수를 구할 수 없음, 나눈 값이 아니라 몫만 구해짐, 평균을 소수점까지 보여주지 않음 > for문 안으로 이동, 출력 값 float로 형변환, 나누는 값으로 변경

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1
    print(total, count)
# count += 1  --기존 코드

print(float(total / count))
# print(total // count)

#08. 예제 [오류 해결] 모음의 개수 찾기
print('예제08')

#오류: 현재 작성되어있는 if문의 경우 모음 중 한 가지만 찾게 됨 > 각각 찾는 것으로 변경하거나 리스트에 모음들을 넣고 확인하는 방법으로 변경

word = "HappyHacking"

aeiou = ['a', 'e', 'i', 'o', 'u']
count = 0

for char in word:
    # if char == "a" or "e" or "i" or "o" or "u":
    if char in aeiou:
        count += 1

print(count)


#09. 예제 [오류 해결] 과일 개수 구하기
print('예제09')

#오류: fruit_count 딕셔너리에 값이 추가되는 것이 아니라 for문이 돌때마다 해당 값으로 변경되고 있음, 딕셔너리 값 대입이 잘못설정 됨 > 대입이 아니라 해당 값을 딕셔너리에 추가하는 것으로 변경, 딕셔너리에 해당 값이 없으면 1로 초기화하는 것으로 변경

from operator import index
from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        # fruit_count = {fruit: 1}
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)

#10. 예제 [오류 해결] 더 큰 최댓값 찾기
print('예제10')

#오류: 첫번째 리스트의 변수명이 함수와 동일하게 설정되어 함수가 작동하지 않음 > 첫번째 리스트의 변수명 변경

number_list = [1, 23, 9, 6, 91, 59, 29]
max1 = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max1 > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max1 < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")


#11. 예제 [오류 해결] 더 큰 최댓값 찾기
print('예제11')

#문제: 함수의 return 값이 존재하지 않음 > return 값 주기

from pprint import pprint


def movie_info(movie, genres):
    genres_names = []
    genre_ids = movie["genre_ids"]
    for genre_id in genre_ids:
        for genre in genres:
            if genre_id == genre["id"]:
                genre_name = genre["name"]
                genres_names.append(genre_name)

    new_movie_info = {
        "genre_names": genres_names,
        "id": movie["id"],
        "overview": movie["overview"],
        "title": movie["title"],
        "vote_average": movie["vote_average"],
    }
    
    return new_movie_info 


if __name__ == "__main__":
    movie = {
        "adult": False,
        "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
        "genre_ids": [18, 80],
        "id": 278,
        "original_language": "en",
        "original_title": "The Shawshank Redemption",
        "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
        "popularity": 67.931,
        "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
        "release_date": "1995-01-28",
        "title": "쇼생크 탈출",
        "video": False,
        "vote_average": 8.7,
        "vote_count": 18040,
    }

    genres_list = [
        {"id": 28, "name": "Action"},
        {"id": 12, "name": "Adventure"},
        {"id": 16, "name": "Animation"},
        {"id": 35, "name": "Comedy"},
        {"id": 80, "name": "Crime"},
        {"id": 99, "name": "Documentary"},
        {"id": 18, "name": "Drama"},
        {"id": 10751, "name": "Family"},
        {"id": 14, "name": "Fantasy"},
        {"id": 36, "name": "History"},
        {"id": 27, "name": "Horror"},
        {"id": 10402, "name": "Music"},
        {"id": 9648, "name": "Mystery"},
        {"id": 10749, "name": "Romance"},
        {"id": 878, "name": "Science Fiction"},
        {"id": 10770, "name": "TV Movie"},
        {"id": 53, "name": "Thriller"},
        {"id": 10752, "name": "War"},
        {"id": 37, "name": "Western"},
    ]

    pprint(movie_info(movie, genres_list))


#문제 19. 숫자의 길이 구하기
#양의 정수 number가 주어질 때, 숫자의 길이를 구하시오  *str 사용금지
# nums를 10으로 계속 나눌때마다 n을 증가시켜서 자릿수를 구함
print('문제 19.')

nums = 758
n = 0

while nums:
    nums //= 10
    n += 1

print(n)
