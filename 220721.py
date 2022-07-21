from operator import index
import sys

sys.stdin = open("./swea_input/0721input.txt", "r")

#SWEA-1288 새로운 불면증 치료법

# T = int(input())
# nums = []
# s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# for test_case in range(1, T + 1):
#     n = int(input())

#     for i in range(1, 10):
#         n2 = n * i
#         if n2 < 10:
#             while n2 < 10:
#                 num = n2
#                 nums.append(num)
#                 n2 += 1

#             if set(nums) == s:
#                 print(f'#{test_case}', n2*i)
#                 nums = []
#                 break
#             else:
#                 continue
        
#         else:
#             while n2:
#                 num = n2 % 10
#                 nums.append(num)
#                 n2 //= 10

#             if set(nums) == s:
#                 print(f'#{test_case}', n*i)
#                 nums = []
#                 break
#             else:
#                 continue
                

#SWEA-1989 초심자의 회문 검사

# T = int(input())

# for test_case in range(1, T + 1):
#     n = input()
#     if n == n[::-1]:
#         print(f'#{test_case}', True)
#     else:
#         print(f'#{test_case}', False)



#SWEA-1976 시각 덧셈

# T = int(input())
# h = 0
# m = 0

# for test_case in range(1, T + 1):
    
#     h1, m1, h2, m2 = map(int, input().split())
    
#     if m1 + m2 >= 60:
#         h = h1 + h2 + 1
#         m = (m1 + m2) - 60
#     else:
#         h = h1 + h2
#         m = m1 + m2
    
#     print(f'#{test_case}', h, m)

#SWEA-1926 간단한 396 게임
# n = int(input())

# for i in range(1, n+1):
#     if i % 10 == 3 :
#         print('-', end=' ')
#         if i // 10 == 3:
#             print('--', end=' ')
#     elif i % 10 == 6:
#         print('-', end=' ')
#         if i // 10 == 6:
#             print('--', end=' ')
#     elif i % 10 == 9:
#         print('-', end=' ')
#         if i // 10 == 9:
#             print('--', end=' ')
#     else:
#         print(i, end=' ')
