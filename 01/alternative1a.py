print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요? '))

for i in range(1, n + 1):
    if i % 2:
        print('+', end='')
    else:
        print('-', end='')

print()