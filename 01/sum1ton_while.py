n = int(input('1부터 n까지 정수의 합을 구합니다. n값을 입력하세요. : '))

sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')