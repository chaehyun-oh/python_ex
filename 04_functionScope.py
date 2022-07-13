def foo():
    a = 1

foo()

a, b, c = map(int, input().split())
print(a, b, c)

numbers = ['2', '4', '6']
new_numbers = map(int, numbers) #map 안에 int는 함수임
print(list(new_numbers)) #리스트로 형변환 해서 보면 확인 가능

def plus10(n):
    return n + 10

numbers = [10, 20, 30]
new_numbers = list(map(plus10, numbers))
print(new_numbers)