a = int(input('a부터 b까지 정수의 합을 구합니다. 정수 a를 입력하세요. :'))
b = int(input('정수 b를 입력하세요. :'))

if a > b:
    a, b = b, a

sum = 0