n = 0
total = 0
user_input = int(input())

while n <= user_input :
    print(f'n: {n}, result: {total}')
    total += n
    n += 1
print(total)