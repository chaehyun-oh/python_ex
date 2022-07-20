from operator import index
import sys

sys.stdin = open("./swea_input/0720input.txt", "r")

#SWEA-1933-간단한 N의 약수

# T = int(input())
# s = []

# for i in range(1, T+1):
#     if T % i == 0:
#         s.append(i)
# print(s)


#SWEA-2019-더블더블

# T = int(input())

# for i in range(T+1):
#     print(2**i, end=' ')

#SWEA-2050-알파벳을 숫자로 변환

# T = input()
# n = len(T)
# for i in range(1, n+1):
#     print(i, end=' ')


#SWEA-1986-지그재그 숫자

# T = int(input())

# for test_case in range(1, T + 1):
#     s = 0
#     n = int(input())
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             s = s - i

#         else:
#             s = s + i

#     print(f'#{test_case}', s)


#SWEA-1284-수도 요금 경쟁

T = int(input())

for test_case in range(1, T + 1):
    
    p, q, r, s, w = map(int, input().split())

    a = p * w
    #A사의 경우
    #요금 = p * w
    if w <= r:
        b = q
    else:
        b = q + s * (w - r)
    #삼항연산자로 바꿀수 도 있음
    #b = q if w <= r else q+s*(w-r)

    #B사의 경우
    #요금 w <= r 일 경우 = q , w> r 일 경우 = s * w

    if a > b:
        print(f'#{test_case}', b)
    elif a < b:
        print(f'#{test_case}', a)

    #또는 print(f'#{test_case} {min(a, b)}')