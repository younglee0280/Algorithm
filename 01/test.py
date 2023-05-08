a = int(input('숫자 입력하세요. (a) : '))
x = int(input('숫자 입력하세요. (x) : '))
y = int(input('숫자 입력하세요. (y) : '))
c = int(input('숫자 입력하세요. (c) : '))

a = x if x > y else y #a if b else c: b를 평가한 값이 참이면 a, 거짓이면 c
print('(c)는 0입니다.' if c==0 else '(c)는 0이 아닙니다.')